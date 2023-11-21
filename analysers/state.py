class state:

    def __init__(self,state):
        self.state=state

    def getState(self):
        return self.state

    def step(self,info):
        if(self.state):
            next=input()
            while(next!='n'):
                next=input()
            print(info)

