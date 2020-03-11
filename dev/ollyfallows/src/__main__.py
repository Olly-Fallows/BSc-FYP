from util import *
from model import *
from neat import *

import sys
import csv
import copy
import random
import json
import math
import time

def runNet(net, data, folder, start=0, end=400):
    fit = 0
    for a in range(start, start+end):
        i = list(data.keys())[a]
        img = image.load_image(folder+"/data/"+i+".jpeg")
        try:
            r = net.apply(img).mat
            result = []
            for rs in r:
                v = rs[0][0]
                if v < 0:
                    v = 0
                result.append(v)
        except:
            print("network failed")
            raise

        for b in range(len(result)):
            if int(data[i]) == b:
                fit += result[b]
            else:
                fit -= result[b]
    return fit

def fitnessCalc(net, data, folder, start=0, end=400):
    fitness = 0
    try:
        fitness = runNet(net,data,folder,start,end)
    except:
        return 0
    return fitness

def test(pop, trainData, inputFolder, gen):
    fitness = {}
    for n in pop:
        print(time.time())
        fitness[n] = fitnessCalc(n, trainData, inputFolder, gen%(int(len(trainData)/400))*400, 400)
        print(time.time())
        print(fitness[n])
    return fitness

if __name__ == "__main__":
    print(sys.path)

    inputFolder = sys.argv[1]
    outputFolder = sys.argv[2]
    basePath = sys.argv[3]

    trainData = {}
    testData = {}
    with open(inputFolder+'labels.csv') as f:
        r = csv.reader(f, delimiter=',')
        line_count = 0
        for row in r:
            if line_count == 0:
                pass
            elif line_count < 5000:
                testData[row[0]] = row[1]
            else:
                trainData[row[0]] = row[1]
            line_count+=1

    net = loader.network_from_string(file.load_file(basePath))
    print(str(net))
    pop = []
    for a in range(50):
        try:
            pop.append(mutator.mutate(copy.deepcopy(net), 0.99))
        except:
            print("Mutate Failed")
            pop.append(copy.deepcopy(net))
    print("population generated")

    gen = 0
    while True:
        gen += 1
        print("Generation "+str(gen))
        fitness = test(pop, trainData, inputFolder, gen)
        print("tested")

        csv = ""
        for a in list(fitness.values()):
            csv += str(a)+"\n"
        file.write_file(outputFolder+"/fitnesses-"+str(gen)+".csv", csv)
        b=0
        for a  in pop:
            b+=1
            file.write_file(outputFolder+"/gen-"+str(gen)+"-net"+str(b)+".json", a.json())

        ordered = {k: v for k, v in sorted(fitness.items(), key=lambda item: -item[1])}
        file.write_file(outputFolder+"/net"+str(gen)+".json", list(ordered.keys())[0].json())
        csv = ""
        l = runNet(list(ordered.keys())[0], testData, inputFolder, 0, len(testData))
        for a in l:
            csv += str(a[0])+","+str(a[1])+"\n"
        file.write_file(outputFolder+"/"+str(gen)+"-output.csv", csv)

        new_pop = []
        for a in range(len(pop)):
            for b in list(ordered.keys()):
                if ordered[b] == 0:
                    continue
                if random.random() < 0.15:
                    try:
                        new_pop.append(mutator.mutate(copy.deepcopy(b), 0.6))
                    except:
                        print("Mutate Failed")
                        pop.append(copy.deepcopy(b))
                    break
            if a >= len(new_pop):
                try:
                    new_pop.append(mutator.mutate(copy.deepcopy(list(ordered.keys())[0]), 0.25))
                except:
                    print("Mutate Failed")
                    pop.append(copy.deepcopy(list(ordered.keys())[0]))
        pop = copy.deepcopy(new_pop)
