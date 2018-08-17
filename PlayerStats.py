from bs4 import BeautifulSoup
import urllib3
import re

class PlayerStats:
    # Obtain user name and assign it
    def __init__(self,player):
        self.player=player

    def getstats(self):
        try:
            # Disable urllib3 InsecureRequestWarning message
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            http=urllib3.PoolManager()

            # Open relevant wikipedia page and parse it using BeautifulSoup
            page_data=http.request('GET',"https://en.wikipedia.org/wiki/"+self.player)
            page_content=BeautifulSoup(page_data.data,"html.parser")
            
            # Extract the required info from the page contents
            dobmatch=re.search(r"(\s)*Date of birth\n(.*)((\d{1,2}) ([A-Za-z]{3,10}) (\d{4}))(.*)Place of birth",page_content.text)
            self.dob=dobmatch.group(3)
            pobmatch=re.search(r"(\s)*Place of birth\n(.*)Height",page_content.text)
            self.pob=pobmatch.group(2)
            posmatch=re.search(r"(\s)*Playing position\n(.*)Club",page_content.text)
            self.pos=posmatch.group(2)
            smatch=re.search(r"(\s)*Career total(\n([\d])*)*",page_content.text)
            lines=smatch.group(0).split('\n')
            stats=[]
            for line in lines:
                if line.isdigit():
                    stats.append(line)
            ln=len(stats)
            self.matches=stats[ln-2]
            self.goals=stats[ln-1]
        except:
            # Catch exception in case the name is wrong
            print("\nPlease check the player's name\n")
            return 99
