import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish)

    objvec = np.array(numvec, dtype=object)

    objvec[numvec % 3 == 0] = "fizz"
    objvec[numvec % 5 == 0] = "buzz"
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = "fizzbuzz"
    
    # Convert the object array to a list
    fizzbuzz_list = objvec.tolist()
    
    return fizzbuzz_list
