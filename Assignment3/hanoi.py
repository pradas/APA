def hanoi_iterative(n):
    tower1 = (1,list(range(1,n+1)))
    tower2 = (2,[])
    tower3 = (3,[])

    last_tower = -1

    if tower1:
        disk = tower1[1].pop()
        if disk % 2 != 0:
            tower3[1].append(disk)
            print("Move from tower 1 to tower 3")
            last_tower = 3
        else:
            tower2[1].append(disk)
            print("Move from tower 1 to tower 2")
            last_tower = 2

    solved = not tower1[1]

    while not solved:
        if tower1[1] and last_tower != 1:
            step_res = hanoi_step(tower1, tower2, tower3)
            if step_res is not None:
                last_tower = step_res
                solved = not tower1[1] and not tower2[1]

        if not solved and tower2[1] and last_tower != 2:
            step_res = hanoi_step(tower2, tower1, tower3)
            if step_res is not None:
                last_tower = step_res
                solved = not tower1[1] and not tower2[1]

        if not solved and tower3[1] and last_tower != 3:
            step_res = hanoi_step(tower3, tower1, tower2)
            if step_res is not None:
                last_tower = step_res
                solved = not tower1[1] and not tower2[1]

def hanoi_step(source_tower, destination1_tower, destination2_tower):
    move_to_destination1 = hanoi_possible_move(source_tower, destination1_tower)
    move_to_destination2 = hanoi_possible_move(source_tower, destination2_tower)
    if move_to_destination1[0] and move_to_destination2[0]:
        if not move_to_destination1[1]:
            return hanoi_move(source_tower, destination1_tower)
        else:
            return hanoi_move(source_tower, destination2_tower)
    elif move_to_destination1[0]:
        return hanoi_move(source_tower, destination1_tower)
    elif move_to_destination2[0]:
        return hanoi_move(source_tower, destination2_tower)

def hanoi_possible_move(source_tower, destination_tower):
    if not destination_tower[1]:
        return (True, True)
    else:
        if source_tower[1][-1] > destination_tower[1][-1]:
            source_parity = source_tower[1][-1] % 2
            destination_parity = destination_tower[1][-1] % 2
            if source_parity != destination_parity:
                return (True, False)

    return (False, False)

def hanoi_move(source_tower, destination_tower):
    destination_tower[1].append(source_tower[1].pop())
    print("Move from tower %d to tower %d" %(source_tower[0], destination_tower[0]))
    return destination_tower[0]


if __name__ == "__main__":
    hanoi_iterative(5)