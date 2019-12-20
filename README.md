# ConnectFourTsetlin
Predicting Win/Loss/Draw on the Connect Four dataset with Tsetlin Machines


connect4cnn3D.py 
Uses the Convolutional Tsetlin Machine, both the CTM and WCTM depending on if weighted_clauses is set to True.
                  It is set up for k-Fold and logging the results in easily manageable files, printing out clauses to files that
                  can be used by boardVisual.py to see the clauses in a 2D format.

connect4.py      
Uses the Tsetlin Machine, both the TM and CTM depending on if weighted_clauses is set to True.
                  It is set up for k-Fold and logging the results in easily manageable files, printing out clauses to files that
                  can be used by boardVisual.py to see the clauses in a 2D format.

boardVisual.py   
Can either access a claus output and visualize it on the screen, or it can print out a board from win/loss/draw 
                  split files. Note that those files have been flipped to match the input of the Tsetlin Machine.

listconvert.py   


Will take inn the connect-4 data set, flipp it so it reads from left to right starting on the top instead of bottom
                  left and upwards as the original set does. After it has been flipped it will transcribe the board into bits. Finally
                  the program will divide and output all wins, losses and draws to 3 sepparate files.

mixlists.py      Made to generate the k-Fold files. It will make 2 lists, each with 10 lists. it will divide each of the win, loss and
                  draw files into 10 blocks, each having the same percentage of all 3 types. It will also make one list with block not 
                  containing draw. It will output 40 files, 20 unique train/test files with draw included and 20 unique train/test files
                  with draw excluded. (k-Fold)
 
 /plotter/
 Contains scripts to make graphs with pyplot, it is tailored for 10-Fold and the way I decided to log the files.
          It will output a graph with the median and standard deviation and a table file that makes LaTeX code for easy and 
          safe generation of a table with the same median and standard deviation in LaTeX.
