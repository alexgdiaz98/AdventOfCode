import itertools

class Amplifier:
    
    def __init__(self, phase, amp_out):
        self.inp = [3,8,1001,8,10,8,105,1,0,0,21,30,47,64,81,98,179,260,341,422,99999,3,9,1001,9,5,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,102,3,9,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,1001,9,5,9,1002,9,3,9,1001,9,3,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99]
        self.PC = 0
        self.phase = phase
        self.amp_out = amp_out
        self.input = None
        self.asked_for_phase = False
        self.last_output = None
        self.halt = False
    
    def __repr__(self):
        return str(self.phase) + '->' + str(self.amp_out.phase)

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
        return params

    '''
    Takes the amplifier's phase setting as input. Returns the first ouput value.
    '''
    def continue_AMP(self):
        asked_for_input = False
        while not self.halt:
            instruction = str(self.inp[self.PC]).zfill(5) # Ensures instruction is at least 5 digits long
            
            # Halt Opcode
            if instruction[-2:] == '99':
                self.halt = True
                return last_output
                self.PC += 4
                
            # Add Opcode
            elif instruction[-2:] == '01':
                val = 0
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3] # Store Address must be mode 0
                self.inp[param3] = param1 + param2
                self.PC += 4
                
            # Multiply Opcode
            elif instruction[-2:] == '02':
                val = 0
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3] # Store Address must be mode 0
                self.inp[param3] = param1 * param2
                self.PC += 4
                
            # Store Input Opcode
            elif instruction[-2:] == '03':
                if not self.asked_for_phase:
                    val = self.phase
                    self.asked_for_phase = True
                else:
                    if asked_for_input:
                        return 'continue' # Return and continue next amp. This instruction will repeat when this amp is continued
                    val = self.input
                    asked_for_input = True
                param = self.inp[self.PC+1]
                if instruction[-3:-2] == '0': # Param Position Mode
                    self.inp[param] = val
                self.PC += 2
                
            # Output Opcode
            elif instruction[-2:] == '04':
                param = self.getParams(instruction, 1)[0]
                #print('output:', param)
                if self.amp_out is None:
                    return param
                last_output = param
                #print('setting', self.amp_out.phase, 'to', param)
                self.amp_out.input = param
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
                param3 = self.inp[PC+3] # Store Address must be mode 0
                if param1 < param2:
                    self.inp[param3] = 1
                else:
                    self.inp[param3] = 0
                self.PC += 4
                
            # Equals Opcde
            elif instruction[-2:] == '08':
                param1, param2 = self.getParams(instruction, 2)
                param3 = self.inp[self.PC+3] # Store Address must be mode 0
                if param1 == param2:
                    self.inp[param3] = 1
                else:
                    self.inp[param3] = 0
                self.PC += 4
                
            # Opcode not recognized
            else:
                print('Invalid Instruction', instruction)
                self.halt = True

max_setting_val = 0
max_setting = []
perms = [x for x in itertools.permutations(range(5, 10), 5)]
for perm in perms:
    i, j, k, l, m = perm
    if max_setting == []:
        max_setting = [i, j, k, l, m]
        m_amp = Amplifier(m, None)
        l_amp = Amplifier(l, m_amp)
        k_amp = Amplifier(k, l_amp)
        j_amp = Amplifier(j, k_amp)
        i_amp = Amplifier(i, j_amp)
        m_amp.amp_out = i_amp # Connect last amplifier to first
        i_amp.input = 0 # Initial Input
        cont = True
        val = -1
        while cont:
            i_amp.continue_AMP()
            j_amp.continue_AMP()
            k_amp.continue_AMP()
            l_amp.continue_AMP()
            val = m_amp.continue_AMP()
            if val != 'continue':
                cont = False
        max_setting_val = val
    else:
        m_amp = Amplifier(m, None)
        l_amp = Amplifier(l, m_amp)
        k_amp = Amplifier(k, l_amp)
        j_amp = Amplifier(j, k_amp)
        i_amp = Amplifier(i, j_amp)
        m_amp.amp_out = i_amp
        i_amp.input = 0
        cont = True
        val = -1
        while cont:
            i_amp.continue_AMP()
            j_amp.continue_AMP()
            k_amp.continue_AMP()
            l_amp.continue_AMP()
            val = m_amp.continue_AMP()
            if val != 'continue':
                cont = False
        if val > max_setting_val:
            max_setting = [i, j, k, l, m]
            max_setting_val = val
print(max_setting_val, max_setting)
                    