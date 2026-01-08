class Board:
    def __init__(self):
        self._board =[" ","|"," ","|", " \n",
                      "-","+","-","+","-\n",
                      " ","|"," ","|", " \n",
                      "-","+","-","+","-\n",
                      " ","|"," ","|", " \n"
                     ]
        self.win = False

        
    def Display_Board(self):
        print(self._board)
    
    def SetCell(self,location,team):
        self.board[location] = team
    

    def CheckWin(self):
        if (self.board[0] and self.board[2] and self.board[4]) == (self.board[0]) or (self.board[0] and self.board[12] and self.board[24]) == (self.board[0]) or (self.board[0] and self.board[10] and self.board[20]) == (self.board[0]) or (self.board[10] and self.board[12] and self.board[14]) == (self.board[10]) or (self.board[20] and self.board[22] and self.board[24]) == (self.board[20]) or (self.board[2] and self.board[12] and self.board[22]) == (self.board[2]) or (self.board[4] and self.board[14] and self.board[24]) == (self.board[0]) or (self.board[4] and self.board[12] and self.board[20]) == (self.board[20]):
            self.win = True
            print("There is a winner")
        else:
            print("There is no winner yet")

    def PlayGame(self):
        
