from PlayerStats import *

class DisplayInfo:
    ''' singlePlayer proc is used to display information about 
        a single player
    '''
    def singlePlayer(self,PlayerStats):
        print("\n")
        print("%25s %30s"%("Name : ",PlayerStats.player))
        print("%25s %30s"%("Date of Birth : ",PlayerStats.dob))
        print("%25s %30s"%("Place of Birth : ",PlayerStats.pob))
        print("%25s %30s"%("Position : ",PlayerStats.pos))
        print("%25s %30s"%("Total Matches played : ",PlayerStats.matches))
        print("%25s %30s"%("Total Goals scored : ",PlayerStats.goals))
        print("\n")
        print("\n")

    
    ''' twoPlayer proc is used to display information about
        the two given players
    '''
    def twoPlayer(self,plr1,plr2):
        print("\n")
        print("%25s %30s %30s"%("Name : ",plr1.player,plr2.player))
        print("%25s %30s %30s"%("Date of Birth : ",plr1.dob,plr2.dob))
        print("%25s %30s %30s"%("Place of Birth : ",plr1.pob,plr2.pob))
        print("%25s %30s %30s"%("Position : ",plr1.pos,plr2.pos))
        print("%25s %30s %30s"%("Total Matches played : ",plr1.matches,plr2.matches))
        print("%25s %30s %30s"%("Total Goals scored : ",plr1.goals,plr2.goals))
        print("\n\n")
        


