import math
import csv
TMopen0 = open("2D1218-0437clauses0.csv",'r')
TMopen1 = open("2D1218-0437clauses1.csv",'r')
TMopen2 = open("2D1218-0437clauses2.csv",'r')
CTMopen0 = open("3Dcnn20191220-165618clauses0.csv",'r')
CTMopen1 = open("3Dcnn20191220-165618clauses1.csv",'r')
CTMopen2 = open("3Dcnn20191220-165618clauses2.csv",'r')
TMr0 = TMopen0.readlines()
CTMr0= CTMopen0.readlines()
TMr1 = TMopen1.readlines()
CTMr1= CTMopen1.readlines()
TMr2 = TMopen2.readlines()
CTMr2= CTMopen2.readlines()
win = open("c4winFlip",'r')
loss = open("c4lossFlip",'r')
draw = open("c4drawFlip",'r')
win= win.readlines()
loss = loss.readlines()
draw= draw.readlines()

#rows = "0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1"
def returnValue(t1,t2):
    if (t1 == "1"):
        return "X"
    elif (t2 == "1"):
        return "O"
    elif (t1 == ","):
        return " "
    else:
        return "#"
#print(rows[:83])
#print(rows[84:167])
#b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,x,o,x,o,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,win
#i = 0
#newline = rows[:83]
#newline2 = rows[84:167]
#print(newline)
#print(newline2)
def makeBoard2(input, rows, columns):
    input = input[:-1]
    input = input.split(",")
    outcome = input[-1]
    inputx = input[:42]
    inputo = input[42:84]
    #print(input)
    #print(inputx)
    #print(inputo)
    i=0
    for column in range(columns):
        outline = ""
        for row in range(rows):
            output = ""
            if(inputx[i] == inputo[i]):
                output = "_"
            elif(inputx[i] == "1"):
                output = "X"
            elif(inputo[i] == "1"):
                output = "O"
            outline = outline + ","+output
            i=i+1
        print(outline)
    #print(outcome)
#for i in range(0,5,1):
#    makeBoard2(win[i],7,6)
    #print("---------------------")
#print("--------------------------")
#for i in range(9998,10003,1):
#    makeBoard2(win[i],7,6)
    #print("---------------------")
#print("--------------------------")
#for i in range(24000,24005,1):
#    makeBoard2(win[i],7,6)
    #print("---------------------")
def makeBoard(input, rows, columns):
    input = input[:-1]
    input = input.split(",")
    #print(input)
    i=0
    for column in range(columns):
        outline = ""
        for row in range(rows):
            outline = outline + ","+transform(input[i])
            i=i+1
        print(outline)
def transform(input):
    # print(input)
    if (int(input[0])==1 and int(input[2])==1) or (int(input[1])==1 and int(input[3])==1):
        return "Fa"
    elif (int(input[0])==1 and int(input[1])==1):
        return "+#"
    elif (int(input[2])==1 and int(input[3])==1):
        return "-#"
    elif int(input[0])==1:
        return "+X"
    elif int(input[1])==1:
        return "+O"
    elif int(input[2])==1:
        return "-x"
    elif int(input[3])==1:
        return "-o"
    else:
        return "?#"

for f in range(301,403,2):
    #TMrow0 =TMr0[2325]
    CTMrow0 = CTMr0[f]
    #TMrow1 =TMr1[16]
    CTMrow1 = CTMr1[f]
    #TMrow2 =TMr2[6]
    CTMrow2 = CTMr2[f]
    #print(TMrow)
    #print(CTMrow)
    #makeBoard(TMrow0,7,6)
    makeBoard(CTMrow0,4,4)
    print("----------------------0")
    #makeBoard(TMrow1,7,6)
    makeBoard(CTMrow1,4,4)
    print("----------------------1")
    #makeBoard(TMrow2,7,6)
    makeBoard(CTMrow2,4,4)
    print("----------------------2")