import math 
import matplotlib.pyplot as mp
import numpy

if __name__ == "__main__":
    inp = range(1,101)

    result = numpy.zeros([6,len(inp)])

    for i in range(1,len(inp)):
        result[0][i] = math.factorial(i)
        result[1][i] = math.pow(2, i)
        result[2][i] = math.pow(i, 2)
        result[3][i] = i
        result[4][i] = math.sqrt(i)
        result[5][i] = math.log10(i)
        
    mp.title("Time Complexity of Algorithms")
    mp.plot(inp, result[0], label="n!")
    mp.plot(inp, result[1], label="2^n")
    mp.plot(inp, result[2], label="n^2")
    mp.plot(inp, result[3], label="n")
    mp.plot(inp, result[4], label="sqrt(n)")
    mp.plot(inp, result[5], label="log10(n)")
    mp.legend()
    mp.ylim(0,1000)
    mp.xlim(0,100)
    mp.show()