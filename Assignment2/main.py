from scipy.spatial import distance
import sys
import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point (X:%.1f, Y:%.1f)" %(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def get_vector(self):
        return [self.x, self.y]

class DnaCount:
    def __init__(self, chromosome, arm):
        self.chromosome = chromosome
        self.arm = arm
        self.count = 0

    def __str__(self):
        return "%d%s\t%d" %(self.chromosome, self.arm, self.count)

    def __eq__(self, other):
        if self.chromosome == other.data.chromosome and self.arm == other.data.arm:
            return True
        return False

    def __lt__(self, other):
        if self.chromosome < other.chromosome:
            return True
        if self.chromosome == other.chromosome and self.arm < other.arm:
            return True
        return False

class DnaData:
    def __init__(self, read_id, chromosome, arm, position, x, y):
        self.id = read_id
        self.chromosome = chromosome
        self.arm = arm
        self. position = position
        self.point = Point(x, y)
    
    def __str__(self):
        out = "----\n"
        out += "id: %s\n" %self.id
        out += "loci: %d%s%.2f\n" %(self.chromosome, self.arm, self.position)
        out += "point: %s\n" %str(self.point)
        return out
    
    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False

    def __lt__(self, other):
        if self.chromosome < other.chromosome:
            return True
        if self.chromosome == other.chromosome and self.arm < other.arm:
            return True
        if self.chromosome == other.chromosome and self.arm == other.arm and self.position < other.position:
            return True
        return False
    
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

class LinkedList:
    def __init__(self):
        self.first_node = None
        self._num_nodes = 0
    
    def __str__(self):
        out = ""
        node = self.first_node
        while node is not None:
            out += str(node)
            node = node.next

        return out

    def __len__(self):
        return self._num_nodes
    
    def add_node(self, other):
        if self.first_node is None:
            self.first_node = other
            self._num_nodes += 1
        else:
            node = self.first_node
            previous_node = None

            if other < node:
                self.first_node = other
                other.next = node
                self._num_nodes += 1
                return True
            previous_node = node
            node = node.next
            while node is not None:
                if other < node:
                    previous_node.next = other
                    other.next = node
                    self._num_nodes += 1
                    return True
                previous_node = node
                node = node.next
            previous_node.next = other

    def remove_node(self, other):
        if self.first_node is not None:
            node = self.first_node
            previous_node = None

            if node == other:
                self.first_node = node.next
                del(node)
                self._num_nodes -= 1
                return True
            previous_node = node
            node = node.next
            while node is not None:
                if node == other:
                    previous_node.next = node.next
                    del(node)
                    self._num_nodes -= 1
                    return True
                previous_node = node
                node = node.next
        return False

def line_to_node(line):
    line_split = line.split("\t")
    read_id = line_split[0]
    loci = re.compile(r"(\d*)([pq])(.*)").split(line_split[1])
    point = re.compile(r"\((\d*.+\d*),(\d*.+\d*)\)").split(line_split[2])

    dna = DnaData(read_id, int(loci[1]), loci[2], float(loci[3]), float(point[1]), float(point[2]))
    return LinkedListNode(dna)

if __name__ == "__main__":
    filename = sys.argv[1]
    threshold = float(sys.argv[2])

    linked_list = LinkedList()
    with open(filename, "r") as fd:
        for line in fd:
            linked_list.add_node(line_to_node(line))

    result = LinkedList()
    node_i = linked_list.first_node
    node_result_data = DnaCount(node_i.data.chromosome, node_i.data.arm)
    result.add_node(LinkedListNode(node_result_data))
    while node_i is not None:
        if node_result_data != node_i:
            node_result_data = DnaCount(node_i.data.chromosome, node_i.data.arm)
            result.add_node(LinkedListNode(node_result_data))
        node_j = node_i.next
        while node_j is not None and node_result_data == node_j:
            if distance.euclidean(node_i.data.point.get_vector(), node_j.data.point.get_vector()) <= threshold:
                node_result_data.count += 1
            node_j = node_j.next
        node_i = node_i.next

    filename = "output.txt"
    fd = open(filename, 'w')
    node_result = result.first_node
    while node_result is not None:
        fd.write("%s\n" %str(node_result))
        node_result = node_result.next
    fd.close()