def findVals():
    for noun in range(0, 100):
        for verb in range(0, 100):
            input = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,6,23,27,1,27,5,31,2,9,31,35,1,5,35,39,2,6,39,43,2,6,43,47,1,5,47,51,2,9,51,55,1,5,55,59,1,10,59,63,1,63,6,67,1,9,67,71,1,71,6,75,1,75,13,79,2,79,13,83,2,9,83,87,1,87,5,91,1,9,91,95,2,10,95,99,1,5,99,103,1,103,9,107,1,13,107,111,2,111,10,115,1,115,5,119,2,13,119,123,1,9,123,127,1,5,127,131,2,131,6,135,1,135,5,139,1,139,6,143,1,143,6,147,1,2,147,151,1,151,5,0,99,2,14,0,0]

            halt = False
            PC = 0
            while not halt:
                if input[PC] == 99:
                    halt = True
                    PC += 4
                elif input[PC] == 1:
                    input[input[PC+3]] = input[input[PC+1]] + input[input[PC+2]]
                    PC += 4
                elif input[PC] == 2:
                    input[input[PC+3]] = input[input[PC+1]] * input[input[PC+2]]
                    PC += 4
            if input[0] == 19690720:
                val = 100 * noun + verb
                print(noun, verb, val)

findVals()