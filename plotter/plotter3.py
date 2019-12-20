from matplotlib import pyplot
from statistics import stdev ,median
XLABEL = "epochs"
YLABEL = "accuracy"
OFFSET = 200
CI = True
table = open("table",'w')
for FILENAME in ["4000c 9000t without draw", "4000c 9000t with draw"]:
    m = []
    s = []
    c = 0
    counter =0
    tab = []
    with open(f"{FILENAME}", 'r') as file:
        lined=[]
        for line in file.readlines():
            counter+=1
            #if c < 100:
            #    c+=1
            #    continue
            if counter > 5:
                line = [float(x) for x in line.strip().split(',')[2:]]
                tab.append(line)
            else:
                lines = [x for x in line.strip().split(',')]
                lined.append(lines)
        for i in range(len(line)):
            m.append(median([tab[0][i],tab[1][i],tab[2][i],tab[3][i],tab[4][i],tab[5][i],tab[6][i],tab[7][i],tab[8][i],tab[9][i]]))
            s.append(stdev([tab[0][i],tab[1][i],tab[2][i],tab[3][i],tab[4][i],tab[5][i],tab[6][i],tab[7][i],tab[8][i],tab[9][i]]))
            #print(lines)
            #print(str(lines[5][1]))
        backslash = "\ "
        backslash = backslash[:1]
        #temp2 = lined[5][1]
        #window = str(temp2[:1])
        #temp2 = lined[6][1]
        #window = window +"x"+str(temp2[:1])
        table.write(backslash+"begin{tabular}[c]{@{}l@{}} "+"draw"+"\end{tabular}\n")
        table.write("&"+backslash+"begin{tabular}[c]{@{}l@{}}"+str(round(m[0],2))+backslash+"%$"+backslash+"pm"+str(round(s[0],2))+backslash+"%$"+backslash+"end{tabular}\n")
        table.write("&"+backslash+"begin{tabular}[c]{@{}l@{}}"+str(round(m[49],2))+backslash+"%$"+backslash+"pm"+str(round(s[49],2))+backslash+"%$"+backslash+"end{tabular}\n")
        table.write("&"+backslash+"begin{tabular}[c]{@{}l@{}}"+str(round(m[99],2))+backslash+"%$"+backslash+"pm"+str(round(s[99],2))+backslash+"%$"+backslash+"end{tabular}\n")
        table.write("&"+backslash+"begin{tabular}[c]{@{}l@{}}"+str(round(m[124],2))+backslash+"%$"+backslash+"pm"+str(round(s[124],2))+backslash+"%$"+backslash+"end{tabular}\n")
        table.write("&" + backslash + "begin{tabular}[c]{@{}l@{}}" + str(round(m[149], 2)) + backslash + "%$" + backslash + "pm" + str(round(s[149],2)) + backslash + "%$" + backslash + "end{tabular}" + backslash + backslash + " " + backslash + "hline\n")

    x = [i for i in range(len(m))]
    if CI:
        CI_low = [(m[i]-2*s[i]) for i in x]
        CI_high =[(m[i]+2*s[i]) for i in x]
        pyplot.fill_between(x, CI_low, CI_high, alpha=0.4)
    pyplot.plot(x, m, lw=1, label=f"{FILENAME}")
    x = [(i+OFFSET) for i in x]

pyplot.legend(loc='best')
TITLE = ""
pyplot.title(TITLE)
pyplot.xlabel(XLABEL)
pyplot.ylabel(YLABEL)
pyplot.savefig('4000c0-500', dpi=300)
pyplot.show()

for FILENAME in ["3x3w 1000c 9000t", "4x4w 1000c 9000t", "5x5w 1000c 9000t", "7x6w 1000c 9000t"]:
    m = []
    s = []
    c = 0
    with open(f"{FILENAME}", 'r') as file:
        for line in file.readlines():
            #if c < 100:
            #    c+=1
            #    continue
            line = [float(x) for x in line.strip().split(',')[1:]]
            m.append(median(line))
            s.append(stdev(line))
    x = [i for i in range(len(m))]
    if CI:
        CI_low = [(m[i]-2*s[i]) for i in x]
        CI_high =[(m[i]+2*s[i]) for i in x]
        pyplot.fill_between(x[OFFSET:], CI_low[OFFSET:], CI_high[OFFSET:], alpha=0.4)
    pyplot.plot(x[OFFSET:], m[OFFSET:], lw=1, label=f"M {FILENAME}")
    x = [(i+OFFSET) for i in x]

pyplot.legend(loc='best')
TITLE = ""
pyplot.title(TITLE)
pyplot.xlabel(XLABEL)
pyplot.ylabel(YLABEL)
pyplot.savefig('4000c200-500', dpi=300)
pyplot.show()