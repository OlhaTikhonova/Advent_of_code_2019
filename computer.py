class Computer:
    def __init__(self, code):
        self.memory = code[:]
        self.pointer = 0
        self.relative_base = 0
    
    def halted(self):
        return self.memory[self.pointer] == 99
    
    def run(self, input_data):
        output_list=[]
        list_0=[0]

        while True:
            operation=(self.memory[self.pointer])% 100
            mode = self.memory[self.pointer] // 100
            modes = [None, mode % 10, mode //10 %10,mode // 100 % 10]

            def arg(index):
                if modes[index] == 0:
                    i=self.memory[self.pointer + index]
                elif modes[index] == 1:
                    i = self.pointer + index
                elif modes[index] == 2:
                    i= self.memory[self.pointer + index] + self.relative_base

                if i>=len(self.memory):
                    self.memory.extend(list_0*(i-len(self.memory)+1))
                return self.memory[i]

            def out(index):
                i=self.memory[self.pointer + index]
                if modes[index] == 0:
                    if i>=len(self.memory):
                        self.memory.extend(list_0*(i-len(self.memory)+1))
                    return i
                if modes[index] == 2:
                    if (i+self.relative_base)>=len(self.memory):
                        self.memory.extend(list_0*((i+self.relative_base)-len(self.memory)+1))
                    return i+self.relative_base
            if operation==1:
                self.memory[out(3)] = arg(1) + arg(2)
                self.pointer+=4
            elif operation==2: 
                self.memory[out(3)] = arg(1) * arg(2)
                self.pointer+=4
            elif operation==3:
                if len(input_data) == 0:
                    break
                self.memory[out(1)] = input_data.pop(0)
                self.pointer+=2
            elif operation==4:
                output_list.append(arg(1))
                self.pointer+=2
            elif operation==5:
                if arg(1)!=0:
                    self.pointer=arg(2)
                else:
                    self.pointer+=3
            elif operation==6:
                if arg(1)==0:
                    self.pointer=arg(2)
                else:
                    self.pointer+=3
            elif operation==7:
                if arg(1)<arg(2):
                    self.memory[out(3)]=1
                else:   
                    self.memory[out(3)]=0
                self.pointer+=4
            elif operation==8:
                if arg(1)==arg(2):
                    self.memory[out(3)]=1
                else:   
                    self.memory[out(3)]=0
                self.pointer+=4
            elif operation==9:
                self.relative_base+=arg(1)
                self.pointer+=2
            elif operation ==99:  
                break
        return output_list