import random
import numpy
import BattleShips




m=numpy.array([
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    ])


YWing=numpy.array([
                                        [0,1,0],
                                        [1,1,1],
                                        [1,0,1]])#ywing pattern
XWing=numpy.array([
                                        [0,1,0],
                                        [1,1,1],
                                        [0,0,0]])# x wing pattern
BWing=numpy.array([
                                        [0,1,0],
                                        [0,1,0],
                                        [0,1,0]])#b wing pattern
AWing=numpy.array([
                                        [0,1,1],
                                        [0,1,0],
                                        [0,0,0]])#a wing pattern

XYBA=[YWing,XWing,BWing,AWing]


m[m==' ']=0
m[m=='/']=1
m=m.astype(int)
m[m=='1']=-1
HeatMap=m
# print(m)
# CellEmpty= numpy.isin(m,[' '])
for Rmap in range(0,len(m)):#goes does the rows in the map array
    for Cmap in range(0,len(m)):#goes across in collums in the map array
        for ship in range(0,len(XYBA)):#goes across the XYBA variable to chose a ship for the later for loops
            for rotcon in range(4):# rotates the ship pattern in all 4 directions
                TempMap=m
                
                rotation=numpy.rot90(XYBA[ship],rotcon)# rotates the ship pattern in the direction of rotcon variable
                PossibleLocations=BattleShips.correlate((TempMap==0),rotation)# uses the correlate function in battleships to compate the pattern with the map
#                 TempMap[PossibleLocations & (TempMap==0)]=1
#                 print(TempMap)
                HeatMap+=PossibleLocations
#                 print(HeatMap)
            HeatMap+=HeatMap


HeatMapProbability= HeatMap / HeatMap.max()#finds the largest value in the heat map and divides all cells by the highest value, and sets them between 0-1 like a probability of a hotspot
print(HeatMapProbability)
print(HeatMap)       
                
   
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                