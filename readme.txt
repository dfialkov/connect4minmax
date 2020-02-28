1. Daniel Fialkov
10825432
2. Program written in Python 3 version 3.8.1. Please note that this is not the Python 2 that the starter code was written in, as I ran the starter code files through the 2to3 utility. 
3. The code's structure does not meaningfully differ from the starter code's structure. The two files needed to run the program(aside from input files) are maxconnect4.py and MaxConnect4Game.py The only new addditions that aren't just filled in stub methods are some helper methods for printing to human.txt/computer.txt and a minimax search function. 
The minimax works with alpha-beta pruning and depth limiting.
The search tree is created on the fly instead of being prepared in full before traversal, slightly reducing memory usage.
The eval function is the difference between the computer player's score and the opponent's score.
4. Please run on windows with python 3. Structure commands like the commands in the directions. For example, running with input1.txt as input with the computer as player 1 with search depth 7 looks like: "python ./maxconnect4.py interactive input1.txt computer-next 7"
You may need to do something else to use specifically python 3, but I can provide no further guidance on the matter without knowing your systems. 
For interactive mode, column numbering and move numbering starts from zero.