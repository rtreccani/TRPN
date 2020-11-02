import logging, sys, math, random

#logging.basicConfig(filename='TRPN.log', filemode ='w', level=logging.DEBUG

class TRPNBackend:
    stack = []

    angleSchema = 'deg'
 
    def popFromBOS(self):
        return(self.stack.pop())

    def getLast2Items(self):
        return self.stack.pop(), self.stack.pop()


    def printStack(self):
        for index, stackElement in enumerate(self.stack):
            print(index, ':' , stackElement)

    def processCommand(self, command):
        if(command == '+'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to add since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate + ultimate)

        elif(command == '-'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to sub since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate - ultimate)

        elif(command == '*'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to mul since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate * ultimate)

        elif(command == '/'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to div since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate / ultimate)

        elif(command == '^'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to power since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(math.pow(penultimate, ultimate))
        
        elif(command == '%'):
            if(len(self.stack) < 2):
                logging.getLogger(__name__).warning('unable to mod since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate % ultimate)
        
        elif(command == 'e'):
            self.stack.append(math.e)
        
        elif(command == 'p'):
            self.stack.append(math.pi)
        
        elif(command == 'l'):
            if(len(self.stack) < 1):
                logging.getLogger(__name__).warning('unable to ln since stack is too short')
            else:
                a = self.stack.pop()
                if(a<=0):
                    self.stack.append(a)
                    logging.getLogger(__name__).warning("can't ln <= 0")
                else:
                    self.stack.append(math.log(a, math.e))
        
        elif(command == 'r'):
            if(len(self.stack) < 1):
                logging.getLogger(__name__).warning('unable to random since stack too short')
            else:
                a = self.stack.pop()
                if(a == 0):
                    self.stack.append(a)
                    logging.getLogger(__name__).warning("can't random from 0")
                else:
                    self.stack.append(random.randrange(int(a)))
        
        elif(command == 's'):
            if(len(self.stack) < 1):
                logging.getLogger(__name__).warning('unable to sin since stack too short')
            else:
                self.stack.append(math.sin(self.stack.pop()))
        
        elif(command == 'c'):
            if(len(self.stack) < 1):
                logging.getLogger(__name__).warning('unable to cos since stack too short')
            else:
                self.stack.append(math.cos(self.stack.pop()))
        
        elif(command == 't'):
            if(len(self.stack) < 1):
                logging.getLogger(__name__).warning('unable to tan since stack too short')
            else:
                self.stack.append(math.tan(self.stack.pop()))



    def pushToStack(self, newVal):
        if(type(newVal) == float):
            self.stack.append(newVal)
        else:
            logging.getLogger(__name__).warning('stack was passed non-float value. Fuck you.')

s = TRPNBackend()


while True:
    command = input("TRPN>")
    try:
        commandFloat = float(command)
        s.pushToStack(commandFloat)
    except:
        #print("command not in float format. attempting to process as a command:  ")
        if(command == 'q'):
            sys.exit(0)
        elif(command == '.'):
            print(s.popFromBOS())
        else:
            s.processCommand(command)

    s.printStack()
    

