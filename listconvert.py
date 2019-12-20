import csv
from numpy.random import shuffle
c4win = open("c4winFlip",'w')
c4loss = open("c4lossFlip",'w')
c4draw = open("c4drawFlip",'w')

def convert(input):
    i=0
    xbit = ''
    obit = ''
    rows = ''
    while i < len(input)-1:
        if input[i] == 'x':
            xbit = xbit + '1,'
            obit = obit + '0,'
        elif input[i] == 'o':
            obit = obit + '1,'
            xbit = xbit + '0,'
        else:
            xbit = xbit + '0,'
            obit = obit + '0,'
        i+=1
    if input[len(input)-1] == 'win':
        rows = xbit+obit+'1\n'
        #c4win.write(rows)
    elif input[len(input)-1] == 'loss':
        rows = xbit+obit+'0\n'
        #c4loss.write(rows)
    else:
        rows = xbit+obit+'2\n'
        #c4draw.write(rows)
def Rearrange(list):
    output = []
    for column in range(6):
        temp = 6 - column
        for row in range(7):
            index = (6 * row) + temp
            #print(index)
            output.append(list[index - 1])
    output.append(list[42])
    print(list)
    print(output)
    #flipped.write(output)
    return output

with open("connect-4.data", newline='') as File:
    reader =csv.reader(File)
    for row in reader:
        newRow = Rearrange(row)
        convert(newRow)
        break