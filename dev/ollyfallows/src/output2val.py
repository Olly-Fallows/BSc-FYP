import sys
import csv

TP = 0
FP = 1
TN = 2
FN = 3

def cost(l):
    result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for a in l:
        if a[0] == a[1]:
            result[a[0]][TP] += 1
            for b in range(5):
                if a[0] == b:
                    continue
                result[b][TN] += 1
        else:
            result[a[1]][FP] += 1
            result[a[0]][FN] += 1
            for b in range(5):
                if a[0] == b or a[1] == b:
                    continue
                result[b][TN] += 1
    return result

def specificity(l):
    return l[TN]/(l[TN]+l[FP])

def sensitivity(l):
    return l[TP]/(l[TP]+l[FN])

def accuracy(l):
    return (l[TP]+l[TN])/(l[TP]+l[FP]+l[TN]+l[FN])

if __name__ == "__main__":
    input = sys.argv[1]
    a = 1
    while True:
        s = str(a)+","
        with open(input+str(a)+"-output.csv") as f:
            data = []
            r = csv.reader(f, delimiter=',')
            for row in r:
                data.append([int(row[0]), int(row[1])])
            co = cost(data)
            c = [0,0,0,0]
            sen = 0
            spe = 0
            acc = 0
            for c1 in co:
                sen += sensitivity(c1)
                spe += specificity(c1)
                acc += accuracy(c1)
                c[TP] += c1[TP]
                c[FP] += c1[FP]
                c[TN] += c1[TN]
                c[FN] += c1[FN]
            s += str(sen/5)+","
            s += str(spe/5)+","
            s += str(acc/5)
            print(s)
            a += 1
