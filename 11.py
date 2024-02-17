import numpy as np
Datas=np.array([[1,1000,300,1,1],
                [2,800,3,4,0],
                [3,960,30,3,0],
                [4,1000,280,1,1],
                [5,1000,90,2,1],
                [6,1000,400,3,1],
                [7,1200,60,4,0],
                [8,1000,210,3,1],
                [9,800,200,4,0],
                [10,1000,70,4,0]])
Test=np.array([11,1000,1,500])

def NBC(trainData,labels,testData):
    C={}
    for label in labels:
        if C.get(label)!=None:
            C[label]+=1
        else:
            C[label]=1
    print('分类情况：',C)
    Clen=len(labels)
    Ptc={}
    for k,c in C.items():
        c=int(c)
        Atcount={}
        for records in trainData:
            if records[-1]==k:
                print(records, k, c)
                i=0
                length=len(testData)
                while i< length:
                    if testData[i] == records[i]:
                        if Atcount.get(testData[i])!=None:
                            Atcount[testData[i]]+=1
                        else:
                            Atcount[testData[i]]=1
                    i+=1

        print('在分类', k, '情况下，各属性出现次数', Atcount)
    Pt=np.array(list(Atcount.values()))/c

    v = 1
    for p in Pt:
        if p != 0:
            v *= p
    Ptc[k] = (c / Clen) * v
    print(Ptc)
    return max(Ptc, key=Ptc.get)
if __name__=='__main__':
    NBC(Datas,Datas[:,-1],Test)
