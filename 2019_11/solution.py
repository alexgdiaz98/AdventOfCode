import itertools
import matplotlib.pyplot as plt

x = []
y = []
c = []

class Intcode:
    
    def __init__(self):
        self.inp = [0]*10000
        for i, val in enumerate([3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,51,2,1008,18,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,77,1,1006,8,10,1006,0,88,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,106,1006,0,47,2,5,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,135,2,105,3,10,2,1101,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,165,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,186,1,1009,11,10,1,9,3,10,2,1003,10,10,1,107,11,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,225,1006,0,25,1,1009,14,10,1,1008,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,257,1,1006,2,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,284,2,1004,7,10,1006,0,41,2,1106,17,10,1,104,3,10,101,1,9,9,1007,9,919,10,1005,10,15,99,109,641,104,0,104,1,21101,0,937108545948,1,21102,1,336,0,1105,1,440,21102,1,386577203612,1,21102,347,1,0,1105,1,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,21478178819,1,21102,1,394,0,1106,0,440,21102,21477985447,1,1,21101,405,0,0,1105,1,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,984458351460,0,1,21101,428,0,0,1106,0,440,21101,709048034148,0,1,21102,439,1,0,1106,0,440,99,109,2,21201,-1,0,1,21101,0,40,2,21101,471,0,3,21102,461,1,0,1105,1,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1101,0,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21102,540,1,0,1106,0,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22101,0,-4,-4,1105,1,636,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1106,0,545,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,606,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22101,0,-1,1,21101,628,0,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]):
            self.inp[i] = val
        self.PC = 0
        self.relbase = 0
        self.halt = False
        self.pos = [500,500]
        self.dir = 0 # Up
        self.painted = []
        self.panels = []
        for j in range(1000):
            self.panels.append([0 for i in range(1000)])
        self.panels[self.pos[0]][self.pos[1]] = 1

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

    '''
    Takes the amplifier's phase setting as input. Returns the first ouput value.
    '''
    def runComp(self):
        color_next = True
        while not self.halt:
            instruction = str(self.inp[self.PC]).zfill(5) # Ensures instruction is at least 5 digits long
            
            # Halt Opcode
            if instruction[-2:] == '99':
                self.halt = True
                self.PC += 4
                
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
                val = self.panels[self.pos[0]][self.pos[1]]
                print(instruction, 'sensed panel at', self.pos, 'is', val)
                param1 = self.inp[self.PC+1]
                if instruction[-3:-2] == '0': # Param Position Mode
                    self.inp[param1] = int(val)
                elif instruction[-3:-2] == '2': # Param Relative Mode
                    self.inp[self.relbase+param1] = int(val)
                self.PC += 2
                
            # Output Opcode
            elif instruction[-2:] == '04':
                print(instruction, end=' ')
                param = self.getParams(instruction, 1)[0]
                if color_next:
                    self.panels[self.pos[0]][self.pos[1]] = param
                    print(self.pos)
                    if self.pos not in self.painted:
                        self.painted.append(self.pos)
                        x.append(self.pos[0])
                        y.append(self.pos[1])
                        if param == 0:
                            c.append(0)
                        else:
                            c.append(50)
                    color_next = False
                    print('painted', self.pos, param)
                else:
                    if param == 0: # Left
                        self.dir -= 1
                        if self.dir == -1:
                            self.dir = 3
                    elif param == 1: # Right
                        self.dir += 1
                        if self.dir == 4:
                            self.dir = 0
                    if self.dir == 0: # Up
                        self.pos = [self.pos[0], self.pos[1]+1]
                    elif self.dir == 1: # Right
                        self.pos = [self.pos[0]+1, self.pos[1]]
                    elif self.dir == 2: # Down
                        self.pos = [self.pos[0], self.pos[1]-1]
                    elif self.dir == 3: # Left
                        self.pos = [self.pos[0]-1, self.pos[1]]
                    color_next = True
                    print('moved to', self.pos, 'facing', self.dir)
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
print(len(robot.painted))
#print(robot.panels)
plt.scatter(x, y, c=c)
plt.show()