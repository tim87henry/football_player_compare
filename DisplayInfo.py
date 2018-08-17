from PlayerStats import *

class DisplayInfo:
    ''' singlePlayer proc is used to display information about 
        a single player
    '''
    def singlePlayer(self,PlayerStats):
        print("\n"+PlayerStats.player+" information\n")
        print("Date of Birth : "+str(PlayerStats.dob))
        print("Place of Birth : "+str(PlayerStats.pob))
        print("Position : "+str(PlayerStats.pos))
        print("Total Matches played : "+str(PlayerStats.matches))
        print("Total Goals scored : "+str(PlayerStats.goals))
        print("\n\n")
    
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
        


