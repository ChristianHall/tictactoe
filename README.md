# tictactoe

This game utilizes three levels of difficulty, in which various strategies are used against the player.

In EASY mode, the progem will try to create 3-in-a-row by checking where the player has played and where it has played.
If it can't make the next move, it will pick a random square until it encounters one that is available. 

In MEDIUM mode, the program becomes "REACTIVE". After checking to see if it can complete its own 3-in-a-row, the program
checks the player's progress, and will block the third square if a two-in-a-row made by the player is detected. If there
is none, it will try to continue its own two-in-a-row, and last resort it picks a random square.

In DIFFICULT mode, the program becomes "PROACTIVE". After checking to see if it can complete its own 3-in-a-row and
stopping the player from attaining 3-in-a -ow, the program will try to identify patterns in the board to best plan its
next move. If it finds none, it will then try to continue any 2-in-a-rows, or pick a random square as a last resort.

This is a work in progress.
