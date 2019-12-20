from pyTsetlinMachine.tm import MultiClassConvolutionalTsetlinMachine2D
import numpy as np
from time import time
import csv
import time as stime


def StartMachine(clauses,epoch,Threshold,S,Window_X,Window_Y,Shape_X,Shape_Y,Shape_Z,inndata):
    counter = 0
    timestr = stime.strftime("%Y%m%d-%H%M%S")
    results = open("results/3Dcnn" + timestr + ".csv", 'a')

    results.write(
        "MultiClassConvolutionalTsetlinMachine2D,3D,")
    resultclauses = open("results/3Dcnn" + timestr + "clauses1.csv", 'a')
    ecount = 0
    offset_y =Shape_Y -Window_Y
    offset_x = Shape_X - Window_X
    def GetOutput(tm, tm_class, clause):
        output = []
        xyz_id_old = 0
        for y in range(Window_Y):
            for x in range(Window_X):
                for z in range (Shape_Z):
                    xyz_id = offset_y+offset_x+y*Shape_X*2+x*2+z
                    outputbit = tm.ta_action(tm_class,clause,xyz_id)
                    output.append(outputbit)
                    xyz_id_old = xyz_id+1
        output = GetOutNegated(tm,tm_class,clause,xyz_id_old, output)
        return output
    def GetOutNegated(tm, tm_class, clause,xyz_id_old, output):
        for y in range(Window_Y):
            for x in range(Window_X):
                for z in range (Shape_Z):
                    xyz_id = xyz_id_old +offset_y+offset_x+y*Shape_X*2+x*2+z
                    outputbit = tm.ta_action(tm_class,clause,xyz_id)
                    output.append(outputbit)
        return output
    def Align(tm, tm_class, clause):
        output = GetOutput(tm, tm_class, clause)
        nonNegated = output[:int(len(output) / 2)]
        negated = output[int(len(output) / 2):]
        xbit = (nonNegated[:int(len(nonNegated) / 2)])
        obit = (nonNegated[int(len(nonNegated) / 2):])
        nxbit = (negated[:int(len(negated) / 2)])
        nobit = (negated[int(len(negated) / 2):])
        for i in range(Window_Y*Window_X):
            resultclauses.write(str(xbit[i]) + str(obit[i]) + str(nxbit[i]) + str(nobit[i]))
            if i < (Window_Y*Window_X-1):
                resultclauses.write(",")
            else:
                resultclauses.write("\n")
    def PrintClass(Ts, Class, clauses):
        for i in range(clauses):
            Align(Ts, Class, i)

    while ecount < epoch:
        results.write("Epoch"+str(ecount+1)+",")
        ecount+=1
    results.write("\n")
    results.write(
        "Settings:\nClauses:,%.1f\nThreshold:,%.1f\nS:,%.1f\nWindow_X:,%.1f\nWindow_Y:,%.1f\nShape_X:,%.1f\nShape_Y:,%.1f\nShape_Z:,%.1f\n" % (clauses, Threshold, S, Window_X, Window_Y,Shape_X, Shape_Y, Shape_Z))
    while counter < 10:
        numb = str(counter)
        train_data = np.loadtxt("dataset/"+inndata+numb+"trainFlip", delimiter = ",")
        #12x7 & 14x6 seems 12x7 gives much better results than 14x6
        X_train = train_data[:,0:-1].reshape(train_data.shape[0], Shape_X, Shape_Y, Shape_Z)
        Y_train = train_data[:,-1]
        test_data = np.loadtxt("dataset/"+inndata+numb+"testFlip", delimiter = ",")
        X_test = test_data[:,0:-1].reshape(test_data.shape[0], Shape_X, Shape_Y, Shape_Z)
        Y_test = test_data[:,-1]

        ctm = MultiClassConvolutionalTsetlinMachine2D(clauses, Threshold, S, (Window_X, Window_Y), boost_true_positive_feedback=1, weighted_clauses=True)
        print("-------------------------------------------------------------------------------------------")
        print("MultiClassConvolutionalTsetlinMachine2D using %s %s writen to file %s.csv (%.1f x %.1f x %.1f)\n" %(inndata,str(counter),timestr,Shape_X, Shape_Y, Shape_Z))
        print("Settings: Clauses: %.1f Threshold: %.1f S: %.1f Window_X: %.1f Window_Y: %.1f\n" % (clauses, Threshold, S, Window_X,Window_Y))
        result = np.zeros(0)
        results.write(inndata+numb+",")
        for i in range(epoch):
            start = time()
            ctm.fit(X_train, Y_train, epochs=1,incremental=True)
            stop = time()
            timestamp = stime.strftime("%H:%M:%S")
            result = np.append(result, 100*(ctm.predict(X_test) == Y_test).mean())
            print("#%d Time: %s Count: %.1f Mean Accuracy (%%): %.2f; Std.dev.: %.2f; Training Time: %.1f ms/epoch" % (i+1,timestamp, counter, np.mean(result), np.std(result), (stop-start)/5.0))
            results.write(",%.4f" % (np.mean(result)))
        results.write("\n")

        counter+=1
        if(counter==1): #only saving one of the k-Folds clauses for now
            PrintClass(ctm, 1, clauses)
            resultclauses.close()
            resultclauses = open("results/3Dcnn" + timestr + "clauses0.csv", 'a')
            PrintClass(ctm, 0, clauses)
            resultclauses.close()
            if(inndata == "draw"):
                resultclauses = open("results/3Dcnn" + timestr + "clauses2.csv", 'a')
                PrintClass(ctm, 2, clauses)
                resultclauses.close()
    results.close()

    #resultclauses.close()
def runner():
    # Settings
    clauses = 1000
    epoch = 50
    Threshold = 9000
    S = 27
    Window_X = 4
    Window_Y = 4
    Shape_X = 7

    Shape_Y = 6
    Shape_Z = 2
    inndata = "nodraw"
    #StartMachine(clauses,epoch,Threshold,S,Window_X,Window_Y, Shape_X,Shape_Y, Shape_Z,inndata)
    #StartMachine(2000, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z,inndata)
    #StartMachine(clauses, epoch, Threshold, S, 3, 3, Shape_X, Shape_Y, Shape_Z,inndata)
    #StartMachine(2000, epoch, Threshold, S, 3, 3, Shape_X, Shape_Y, Shape_Z,inndata)
    #StartMachine(2000, epoch, Threshold, S, 5, 5, Shape_X, Shape_Y, Shape_Z,inndata)
    #StartMachine(clauses, epoch, Threshold, S, 5, 5, Shape_X, Shape_Y, Shape_Z,inndata)
    #StartMachine(clauses,epoch,Threshold,S,Window_X,Window_Y, Shape_X,Shape_Y, Shape_Z,"draw")
    #StartMachine(2000, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z,"draw")
    #StartMachine(clauses, epoch, Threshold, S, 3, 3, Shape_X, Shape_Y, Shape_Z,"draw")
    #StartMachine(2000, epoch, Threshold, S, 3, 3, Shape_X, Shape_Y, Shape_Z,"draw")
    #StartMachine(2000, epoch, Threshold, S, 5, 5, Shape_X, Shape_Y, Shape_Z, "draw")
    #StartMachine(clauses, epoch, Threshold, S, 5, 5, Shape_X, Shape_Y, Shape_Z, "draw")
    #StartMachine(clauses, epoch, 9000, S, 7, 6, Shape_X, Shape_Y, Shape_Z, "nodraw")
    #StartMachine(clauses, epoch, 9000, S, 7, 6, Shape_X, Shape_Y, Shape_Z, "draw")
    StartMachine(clauses, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z, "draw")
    #StartMachine(clauses, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z, inndata)
    #StartMachine(clauses, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z, "nodraw")
    #StartMachine(clauses, epoch, Threshold, S, Window_X, Window_Y, Shape_X, Shape_Y, Shape_Z, "nodraw")

    #StartMachine(clauses, epoch, 9000, S, 4, 4, Shape_X, Shape_Y, Shape_Z, "nodraw")
    #StartMachine(clauses, epoch, 9000, S, 4, 4, Shape_X, Shape_Y, Shape_Z, "draw")

runner()