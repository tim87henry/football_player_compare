This Python program scraps the wikipedia page of a required football player and then provides information about the player.
It can also be used to compare the stats of 2 football players.

I have used urllib3 for http requests and BeautifulSoup for parsing the web pages.


Sample script output:

1. Single player information
2. Two player comparison
3. Exit the program

Enter your choice : 1

Enter the name of the player : Neymar

Neymar information

Date of Birth : 5 February 1992
Place of Birth : Mogi das Cruzes, Brazil
Position : Forward
Total Matches played : 441
Total Goals scored : 270



1. Single player information
2. Two player comparison
3. Exit the program

Enter your choice : 2

Enter the name of the first player : lionel messi
Enter the name of the second player : cristiano ronaldo


                  Name :                    Lionel Messi              Cristiano Ronaldo
         Date of Birth :                     4 June 1987                5 February 1985
        Place of Birth :              Rosario, Argentina     Funchal, Madeira, Portugal
              Position :                         Forward                        Forward
  Total Matches played :                             670                            763
    Total Goals scored :                             563                            573



1. Single player information
2. Two player comparison
3. Exit the program

Enter your choice : 3
Press any key to continue . . .