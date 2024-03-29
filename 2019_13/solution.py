import itertools
import matplotlib.pyplot as plt

class Intcode:
    
    def __init__(self):
        self.inp = [0]*10000
        for i, val in enumerate([2,380,379,385,1008,2311,446010,381,1005,381,12,99,109,2312,1101,0,0,383,1102,0,1,382,20102,1,382,1,20101,0,383,2,21101,0,37,0,1106,0,578,4,382,4,383,204,1,1001,382,1,382,1007,382,38,381,1005,381,22,1001,383,1,383,1007,383,22,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1102,1,-1,384,1105,1,119,1007,392,36,381,1006,381,161,1102,1,1,384,21001,392,0,1,21102,20,1,2,21102,1,0,3,21101,0,138,0,1105,1,549,1,392,384,392,20101,0,392,1,21101,20,0,2,21102,1,3,3,21101,0,161,0,1106,0,549,1102,0,1,384,20001,388,390,1,20101,0,389,2,21102,180,1,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,20101,0,389,2,21102,205,1,0,1106,0,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21102,228,1,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,20102,1,388,1,20001,389,391,2,21102,253,1,0,1106,0,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,0,304,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20102,1,388,1,20102,1,389,2,21102,0,1,3,21101,338,0,0,1105,1,549,1,388,390,388,1,389,391,389,21002,388,1,1,21001,389,0,2,21101,0,4,3,21102,1,365,0,1106,0,549,1007,389,21,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,226,17,17,1,1,19,109,3,22102,1,-2,1,22101,0,-1,2,21101,0,0,3,21102,1,414,0,1106,0,549,21202,-2,1,1,22101,0,-1,2,21102,1,429,0,1105,1,601,2101,0,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,21202,-3,1,-7,109,-8,2105,1,0,109,4,1202,-2,38,566,201,-3,566,566,101,639,566,566,2102,1,-1,0,204,-3,204,-2,204,-1,109,-4,2106,0,0,109,3,1202,-1,38,594,201,-2,594,594,101,639,594,594,20101,0,0,-2,109,-3,2106,0,0,109,3,22102,22,-2,1,22201,1,-1,1,21102,421,1,2,21101,0,804,3,21101,836,0,4,21101,0,630,0,1105,1,456,21201,1,1475,-2,109,-3,2105,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,2,0,0,2,2,2,2,0,2,0,0,0,2,2,2,0,2,2,2,0,2,0,0,2,0,2,2,2,2,0,2,2,2,0,1,1,0,2,0,0,0,0,2,0,2,2,2,2,2,0,0,0,2,0,0,2,2,0,0,0,2,0,0,0,0,0,2,2,0,2,0,0,1,1,0,2,2,0,2,2,0,0,2,2,2,0,2,2,0,2,0,2,0,0,2,2,0,2,2,2,0,0,0,0,0,2,0,2,0,0,1,1,0,0,2,0,2,2,0,0,0,0,2,0,2,0,0,0,2,2,0,0,2,2,0,0,2,0,2,0,0,2,0,2,0,0,0,0,1,1,0,0,0,2,2,0,0,0,2,2,0,0,0,2,2,2,0,2,2,0,2,0,2,0,2,2,0,0,0,2,0,0,0,0,2,0,1,1,0,2,2,0,0,2,0,0,0,0,0,2,2,2,0,0,0,2,0,2,2,0,2,2,0,0,2,2,2,0,2,0,0,0,2,0,1,1,0,2,2,0,0,2,0,0,0,2,2,2,0,0,0,2,0,2,0,0,2,0,2,2,2,2,0,0,0,2,0,0,0,0,2,0,1,1,0,0,0,0,0,0,0,2,0,2,2,0,0,0,2,2,0,2,2,2,0,0,2,0,2,0,2,2,0,2,2,0,2,2,2,0,1,1,0,2,2,2,0,2,2,0,2,2,0,2,0,2,0,0,0,0,2,0,2,0,0,2,2,0,2,2,2,0,0,2,0,0,2,0,1,1,0,0,2,0,2,2,2,0,0,0,0,2,0,2,2,0,0,0,0,0,0,2,0,2,2,2,0,2,0,2,0,2,0,0,0,0,1,1,0,0,2,0,0,0,0,0,2,2,2,2,2,0,0,2,2,0,0,2,2,2,0,0,2,2,0,2,0,0,0,2,0,0,2,0,1,1,0,2,0,0,0,0,2,2,2,0,0,0,2,2,0,2,2,0,2,0,2,0,0,0,0,2,2,2,2,0,2,0,0,2,0,0,1,1,0,2,2,2,2,0,2,0,2,2,0,2,0,0,2,0,0,2,0,2,0,0,0,2,0,0,0,0,2,0,2,2,2,0,2,0,1,1,0,0,2,2,0,2,0,2,0,0,0,0,0,2,0,0,2,2,0,0,0,2,2,0,2,2,0,0,2,2,2,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,64,65,39,50,55,39,56,42,26,35,2,10,31,68,62,94,43,92,68,53,51,75,44,39,65,2,20,27,34,18,53,7,64,46,53,67,94,10,56,1,94,67,9,76,39,8,55,29,31,39,93,73,82,47,5,80,80,44,85,89,89,90,54,26,16,96,33,87,38,1,3,69,39,54,17,91,52,77,3,46,29,12,12,10,52,61,28,62,21,91,43,68,49,10,91,46,61,52,52,87,8,11,28,2,28,62,40,64,56,51,82,41,39,92,20,13,62,2,29,65,63,23,83,16,51,57,62,27,43,66,29,83,44,39,37,27,96,20,83,9,18,19,64,41,86,93,38,2,4,79,98,76,37,71,45,9,20,38,97,7,98,45,33,73,7,44,51,33,31,97,93,98,82,2,92,54,38,37,27,81,6,15,28,30,35,44,71,40,35,76,49,66,9,55,15,66,43,44,3,82,73,89,4,17,90,4,11,2,52,40,37,98,68,78,36,31,82,96,59,26,3,48,84,60,50,21,9,13,51,28,70,83,81,30,92,26,24,84,79,11,12,21,71,27,15,68,33,37,71,82,54,94,30,4,7,7,9,96,80,16,92,90,44,82,55,5,76,1,86,97,74,49,86,19,10,29,45,2,27,40,27,47,92,47,73,46,79,82,91,60,74,51,49,75,36,19,55,45,13,4,44,89,12,49,71,68,7,66,30,16,6,13,98,4,14,17,11,19,13,95,92,41,31,75,71,30,28,93,65,25,13,35,1,61,30,48,40,96,94,89,9,5,9,10,48,52,27,20,95,80,60,27,67,91,84,62,27,7,9,96,67,98,92,85,5,67,87,94,14,87,82,49,27,90,19,70,4,15,48,29,85,55,24,10,42,91,68,95,87,83,13,31,25,14,24,46,41,4,45,70,11,28,58,78,7,29,55,81,98,65,25,88,11,53,84,31,75,66,96,19,97,57,98,51,18,47,64,36,19,43,24,5,78,65,74,68,42,78,39,13,72,96,86,22,70,85,63,10,69,55,69,1,61,96,11,84,40,58,2,18,1,61,21,4,20,19,1,60,95,31,29,33,16,68,33,42,30,56,2,21,43,32,21,30,40,33,50,83,95,2,95,85,57,39,85,46,47,43,19,47,83,10,32,34,86,94,33,35,33,85,97,46,64,42,40,16,68,27,7,26,37,2,59,4,10,88,31,14,6,35,72,39,1,93,70,84,58,90,7,38,18,58,18,68,92,83,76,65,21,28,81,96,42,79,7,60,54,20,66,12,80,45,18,24,87,71,26,38,7,12,29,15,41,47,81,55,88,2,68,1,61,96,6,47,44,27,64,37,23,33,21,44,86,15,35,34,97,9,50,66,5,15,81,58,68,84,75,5,9,66,63,5,21,91,69,96,30,48,85,31,79,88,5,49,43,57,13,25,98,93,29,66,13,48,73,37,51,52,18,69,84,32,83,45,81,96,37,53,55,60,74,6,44,7,67,5,41,48,57,51,93,14,8,14,80,76,13,97,85,96,29,91,29,59,34,43,85,88,30,5,37,1,64,56,47,25,1,91,13,54,38,58,44,18,70,28,3,96,73,26,26,83,45,2,63,38,92,75,34,1,80,77,35,4,93,6,61,40,6,23,44,54,37,90,57,70,48,52,84,8,37,67,25,78,15,3,40,54,67,12,66,37,67,12,75,22,97,62,61,56,96,22,25,66,17,8,37,92,23,44,42,46,71,72,72,81,65,32,63,58,19,8,34,23,21,71,63,30,65,40,41,85,82,70,71,16,80,70,3,88,60,24,26,86,1,96,72,45,86,43,61,32,4,71,91,36,28,65,38,32,64,46,44,69,77,86,29,21,90,21,98,49,38,83,35,72,90,43,42,37,97,1,49,97,98,35,446010]):
            self.inp[i] = val
        self.PC = 0
        self.relbase = 0
        self.halt = False
        self.tiles = []
        self.counter = 0
        self.score = -1
        for j in range(1000):
            self.tiles.append([' ' for i in range(1000)])

    '''
    Returns a list of the first n parameters in the proper mode.

    NOTE: Do not use for write back parameters
    '''
    def getParams(self, instruction, n):
        params = []
        for i in range(n):
            if instruction[-3-i:-2-i] == '0': # Postion Mode
                params.append(self.inp[self.inp[self.PC+i+1]])
            elif instruction[-3-i:-2-i] == '1': # Immediate Mode
                params.append(self.inp[self.PC+i+1])
            elif instruction[-3-i:-2-i] == '2': # Relative Mode
                params.append(self.inp[self.relbase+self.inp[self.PC+i+1]])
        return params
    
    def print_screen(self):
        print('Score:', self.score)
        for i in range(22):
            for j in range(38):
                print(self.tiles[i][j], end='')
            print()

    '''
    Takes the amplifier's phase setting as input. Returns the first ouput value.
    '''
    def runComp(self):
        out = 0 # X-coord
        score_update = False
        x = 0
        y = 0
        paddle_x = -1
        ball_x = -1
        while not self.halt:
            instruction = str(self.inp[self.PC]).zfill(5) # Ensures instruction is at least 5 digits long
            
            # Halt Opcode
            if instruction[-2:] == '99':
                self.print_screen()
                self.halt = True
                self.PC += 4
                print(self.counter)
                
            # Add Opcode
            elif instruction[-2:] == '01':
                val = 0
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3]
                if instruction[-5:-4] == '0': # Position Mode
                    self.inp[param3] = param1 + param2
                elif instruction[-5:-4] == '2': # Relative Mode
                    self.inp[param3 + self.relbase] = param1 + param2
                self.PC += 4
                
            # Multiply Opcode
            elif instruction[-2:] == '02':
                val = 0
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3]
                if instruction[-5:-4] == '0': # Position Mode
                    self.inp[param3] = param1 * param2
                elif instruction[-5:-4] == '2': # Relative Mode
                    self.inp[param3 + self.relbase] = param1 * param2
                self.PC += 4
                
            # Store Input Opcode
            elif instruction[-2:] == '03':
                #val = int(input('input:'))
                if paddle_x < ball_x:
                    val = 1
                elif paddle_x > ball_x:
                    val = -1
                else:
                    val = 0
                param1 = self.inp[self.PC+1]
                if instruction[-3:-2] == '0': # Param Position Mode
                    self.inp[param1] = int(val)
                elif instruction[-3:-2] == '2': # Param Relative Mode
                    self.inp[self.relbase+param1] = int(val)
                self.PC += 2
                
            # Output Opcode
            elif instruction[-2:] == '04':
                param = self.getParams(instruction, 1)[0]
                if out == 0: # X-coord
                    x = param
                    out = 1
                elif out == 1: # Y-coord
                    y = param
                    out = 2
                elif out == 2: # Tile ID
                    if x == -1 and y == 0: # Score Update
                        self.score = param
                        print(self.score)
                    elif param == 0: # Empty Space
                        self.tiles[y][x] = ' '
                    elif param == 1: # Wall
                        self.tiles[y][x] = '$'
                    elif param == 2: # Block
                        self.tiles[y][x] = '#'
                        self.counter += 1
                    elif param == 3: # Horizontal Paddle
                        self.tiles[y][x] = '='
                        paddle_x = x
                    elif param == 4: # Ball
                        self.tiles[y][x] = '@'
                        ball_x = x
                        #self.print_screen()
                    out = 0
                self.PC += 2
                
            # Jump-If-True Opcode
            elif instruction[-2:] == '05':
                param1, param2 = self.getParams(instruction, 2)
                if param1 != 0:
                    self.PC = param2
                else:
                    self.PC += 3
                    
            # Jump-If-False Opcode
            elif instruction[-2:] == '06':
                param1, param2 = self.getParams(instruction, 2)
                if param1 == 0:
                    self.PC = param2
                else:
                    self.PC += 3
                    
            # Less Than Opcode
            elif instruction[-2:] == '07':
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3]
                if instruction[-5:-4] == '0': # Position Mode
                    if param1 < param2:
                        self.inp[param3] = 1
                    else:
                        self.inp[param3] = 0
                elif instruction[-5:-4] == '2': # Relative Mode
                    if param1 < param2:
                        self.inp[param3 + self.relbase] = 1
                    else:
                        self.inp[param3 + self.relbase] = 0
                self.PC += 4
                
            # Equals Opcde
            elif instruction[-2:] == '08':
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3] # Store Address must be mode 0
                if instruction[-5:-4] == '0': # Position Mode
                    if param1 == param2:
                        self.inp[param3] = 1
                    else:
                        self.inp[param3] = 0
                elif instruction[-5:-4] == '2': # Relative Mode
                    if param1 == param2:
                        self.inp[param3 + self.relbase] = 1
                    else:
                        self.inp[param3 + self.relbase] = 0
                self.PC += 4
            
            # Adjust Relbase Opcode
            elif instruction[-2:] == '09':
                param = self.getParams(instruction, 1)
                self.relbase += param[0]
                self.PC += 2
                
            # Opcode not recognized
            else:
                print('Invalid Instruction', instruction)
                self.halt = True

robot = Intcode()
robot.runComp()