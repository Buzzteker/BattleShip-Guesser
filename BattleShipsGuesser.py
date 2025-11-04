import random
import numpy
import BattleShips

class A(BattleShips.BattleShips):
    def guess(self):
        
         
        if 'H' in self.map:# checks if theres a hit ship
            Hpattern = numpy.array([[False, True, False],#stores the pattern that will be used to hit adjacent cells
                                [ True, False, True],
                                [ False, True, False]])
            
            HitMap=numpy.array(self.map)# stores the self.map into HitMapo variable 
            containsHit = numpy.isin(HitMap,['H'])#gets the location of the hit ship
            HitAdjacent = BattleShips.convolve(containsHit, Hpattern)#overlaps the pattern with the hit ship and stores it in HitAdjacent variable
            
#             print(HitAdjacent)
            
            HitMap[HitAdjacent & (HitMap==' ')] = '1'#sets all the empty cells to 1 
            
#             print(HitMap)
            
            options = numpy.argwhere(HitMap == '1')# gets all the locations of the cells with a 1
            
            return options[0]#returns the options
#             containsHit = numpy.isin(m,['H'])
        

        else:
            
            x=numpy.array(self.map)
            y=numpy.array(self.map)
            for C in range(1,len(self.map)-1):#goes down in rows
                if C % 2 == 0:
                    for R in range(1,len(self.map[0])-1):#goes across in collums
                        if R % 2 != 0:
                            x[C][R]='/'
                else:
                    for R in range(1,len(self.map[0])-1):#goes across in collums
                        if R % 2 ==0:
                            x[C][R]='/'
                                

            k = numpy.array([[0, 1, 0],#coralate pattern 
                    [1, 0, 1],
                    [0, 1, 0]])

            corr = BattleShips.correlate((x == '/'), k)#corolates the pattern onto the x variable 
#             print(corr)
#             print(x)
            isIsolated = (corr>0) & (x==' ')#checks for any cell that is isolated that has a 0 and is empty on the map 

            y[isIsolated]='*'

            options = numpy.argwhere(y == ' ')
#             print(len(options))
            if len(options) == 0:
                options = numpy.argwhere(self.map == ' ')
                return random.choice(options)
            
        return random.choice(options)
    
    

    def __init__(self,N=20):
        self.N = N
        self.map = numpy.full((self.N, self.N), ' ')
        self.mode = 'auto'
        self.manualGuess = (0,0)
    def test(self, nGames=100):
        return numpy.mean(numpy.array([self.autoplay() for _ in range(nGames)])) 



