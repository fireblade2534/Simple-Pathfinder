import math
import time

class Grid:
    def __init__(self, Width, Height):
        self.Width=Width
        self.Height=Height
        self.Grid = [[0 for i in range(Width)] for j in range(Height)]

    def __str__(self) -> str:
        Output=""
        for A,X in enumerate(self.Grid):
            for B,Y in enumerate(X):
                if Y == 0:
                    Output+="⬜"
                elif Y == 1:
                    Output+="⬛"
                    
                elif Y == 2:
                    Output+="🔹"
                elif Y == 3:
                    Output+="💠"
                elif Y == 4:
                    Output+="🔸"
                #Output+=str(Y)
            Output+="\n"
        return Output
    





    

class Bot:
    def __init__(self, X, Y, Width, Height):
        self.Position=[X,Y]
        self.Grid=Grid(Width,Height)
        self.PathHistory=[]
        self.Target=[0,0]
        self.Tick=0
        

    def SetTarget(self, X,Y):
        self.Target=[X,Y]

    @staticmethod
    def GetDistance(X1,Y1,X2,Y2):
        return math.sqrt((X2-X1)**2+(Y2-Y1)**2)
    
    def GetNextPosList(self):
        NextPos=[]
        Movement=[[0,1],[1,0],[0,-1],[-1,0]]
        for X in Movement:
            CheckPos=[self.Position[0]+X[0],self.Position[1]+X[1]]
            GetAtPos=self.Grid.Grid[CheckPos[1]][CheckPos[0]]
            #print(CheckPos,self.PathHistory)
            if GetAtPos == 0 and not CheckPos in self.PathHistory:
                #self.Grid.Grid[CheckPos[1]][CheckPos[0]]=4
                NextPos.append([CheckPos[0],CheckPos[1],Bot.GetDistance(CheckPos[0],CheckPos[1],self.Target[0],self.Target[1])])
        return NextPos


    def DecideNextMovement(self):
        if self.Position[0] != self.Target[1] or self.Position[1] != self.Target[0]:

            NextPos=self.GetNextPosList()
            if len(NextPos) == 0:
                self.PathHistory=self.PathHistory[:-2]
                self.PathHistory.append(self.Position)
                
                NextPos=self.GetNextPosList()
                
            NextPos.sort(key=lambda X: X[2])
            #self.Grid.Grid[self.Position[1]][self.Position[0]]=0
           # @self.Position=NextPos[0][:2]
            #self.Grid.Grid[self.Position[1]][self.Position[0]]=3
            self.PathHistory.append(NextPos[0][:2])
            return True, NextPos[0][0], NextPos[0][1]
        
        else:
            return False, self.Position[0], self.Position[1]
    
    def MoveToPos(self,X,Y):
        self.Grid.Grid[self.Position[1]][self.Position[0]]=0
        self.Position=[X,Y]
        self.Grid.Grid[self.Position[1]][self.Position[0]]=3
    





B=Bot(1,1,10,10)
B.SetTarget(7,7)
B.Grid.Grid[5][2]=1
B.Grid.Grid[5][3]=1
B.Grid.Grid[5][4]=1
B.Grid.Grid[5][5]=1
B.Grid.Grid[4][5]=1
B.Grid.Grid[3][5]=1
B.Grid.Grid[3][4]=1
Step=True
while Step:
    Step,NewX,NewY=B.DecideNextMovement()
    B.MoveToPos(NewX,NewY)
    print(B.Grid)
    time.sleep(0.5)

    #print(B.Grid)
    #time.sleep(0.5)

