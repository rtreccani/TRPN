import logging, sys, math

#logging.basicConfig(filename='TRPN.log', filemode ='w', level=logging.DEBUG

class TRPNBackend:
    stack = []

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
                print('unable to sub since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate - ultimate)

        elif(command == '*'):
            if(len(self.stack) < 2):
                print('unable to mul since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate * ultimate)

        elif(command == '/'):
            if(len(self.stack) < 2):
                print('unable to div since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate / ultimate)

        elif(command == '^'):
            if(len(self.stack) < 2):
                print('unable to power since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(math.pow(penultimate, ultimate))
        
        elif(command == '%'):
            if(len(self.stack) < 2):
                print('unable to mod since stack is too short')
            else:
                ultimate, penultimate = self.getLast2Items()
                self.stack.append(penultimate % ultimate)

        elif(command == 'q'):
            sys.exit(0)

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
        s.processCommand(command)

    s.printStack()
    

