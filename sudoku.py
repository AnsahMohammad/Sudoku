import numpy as np
from time import time

global flag_
flag_ = 1
arr = [
    [0,7,0,0,2,0,0,4,6],
    [0,6,0,0,0,0,8,9,0],
    [2,0,0,8,0,0,7,1,5],
    [0,8,4,0,9,7,0,0,0],
    [7,1,0,0,0,0,0,5,9],
    [0,0,0,1,3,0,4,8,0],
    [6,9,7,0,0,2,0,0,8],
    [0,5,8,0,0,0,0,6,0],
    [4,3,0,0,8,0,0,7,0]
]

def takeInput():
    arr = []
    for i in range(9):
        k = list(map(int,input().split()))
        arr.append(k)
    
    return arr

arr = takeInput()

start = time()


# To print the sudoku with UI

def printer(arr):
    global flag_
    fin = ""
    fin += "-"*19
    fin += "\n"
    row=0
    for i in range(1,10):
        count=0
        for j in range(19):
            if(j%2==0):
                fin+= "|"
            else:
                fin += str(arr[row][count])
                count += 1
        row += 1
        fin += "\n"

    fin += "-"*19

    print(fin)

#removing common elemnts from row and column

def zeroAnalyzer(arr):
    global flag_
    arrx = []
    for i in range(9):
        artemp = []
        for j in range(9):
            if(arr[i][j] == 0):
                
                k = []
                for l in range(9):
                    if arr[l][j] != 0:
                        k.append(arr[l][j])
                        
                possible1 = [ f for f in range(1,10) if f not in k and f not in arr[i]]
                temp = []
                
                if(j%3==0):
                    if(i%3==0):
                        temp.append(arr[i+1][j+1])
                        temp.append(arr[i+1][j+2])
                        
                        temp.append(arr[i+2][j+1])
                        temp.append(arr[i+2][j+2])
                    elif i%3 == 1:
                        temp.append(arr[i-1][j+1])
                        temp.append(arr[i-1][j+2])
                        
                        temp.append(arr[i+1][j+1])
                        temp.append(arr[i+1][j+2])
                    else:
                        temp.append(arr[i-1][j+1])
                        temp.append(arr[i-1][j+2])
                        
                        temp.append(arr[i-2][j+1])
                        temp.append(arr[i-2][j+2])
                elif j%3 == 1:
                    if(i%3==0):
                        temp.append(arr[i+1][j-1])
                        temp.append(arr[i+1][j+1])
                        
                        temp.append(arr[i+2][j-1])
                        temp.append(arr[i+2][j+1])
                    elif i%3 == 1:
                        temp.append(arr[i-1][j-1])
                        temp.append(arr[i-1][j+1])
                        
                        temp.append(arr[i+1][j-1])
                        temp.append(arr[i+1][j+1])
                    else:
                        temp.append(arr[i-1][j-1])
                        temp.append(arr[i-1][j+1])
                        
                        temp.append(arr[i-2][j-1])
                        temp.append(arr[i-2][j+1])
                else:
                    if(i%3==0):
                        temp.append(arr[i+1][j-1])
                        temp.append(arr[i+1][j-2])
                        
                        temp.append(arr[i+2][j-1])
                        temp.append(arr[i+2][j-2])
                    elif i%3 == 1:
                        temp.append(arr[i-1][j-1])
                        temp.append(arr[i-1][j-2])
                        
                        temp.append(arr[i+1][j-1])
                        temp.append(arr[i+1][j-2])
                    else:
                        temp.append(arr[i-1][j-1])
                        temp.append(arr[i-1][j-2])
                        
                        temp.append(arr[i-2][j-1])
                        temp.append(arr[i-2][j-2])
                #print(temp)
                possible = [f for f in possible1 if f not in temp]
                #print(possible,end = ' ')
                if(len(possible) == 1):
                    artemp.append(possible[0])
                    
                    print("printed "+str(possible[0]))
                    flag_ += 1
                    print(flag_)
                else:
                    artemp.append(possible)
            else:
                #print(" {} ".format(arr[i][j]),end='')
                artemp.append(arr[i][j])
        arrx.append(artemp)
    return arrx

#removing duplicates

def layer3(arr):
    global flag_
    for i in range(0,9,3):
        for j in range(0,9,3):
            #considering each 3x3 blocks
            uniques_ = []
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if str(type(arr[k][l])) != "<class 'list'>":
                        uniques_.append(arr[k][l])
            uniques_ = list(set(uniques_))
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if str(type(arr[k][l])) == "<class 'list'>":
                        t = [f for f in arr[k][l] if f not in uniques_]
                        arr[k][l] = t
                        if(len(arr[k][l]) == 1):
                                arr[k][l] = arr[k][l][0]
                                flag_ += 1
                                print(flag_)
    return arr

#removing duplicates

def layer4(arr):
    global flag_
    for i in range(9):
        uniques_ = []
        for j in range(9):
            if str(type(arr[i][j])) != "<class 'list'>":
                uniques_.append(arr[i][j])
        for j in range(9):
            if str(type(arr[i][j])) == "<class 'list'>":
                k = [f for f in arr[i][j] if f not in uniques_]
                if len(k) == 1:
                    arr[i][j] = k[0]
                    flag_ += 1
                else:
                    arr[i][j] = k
    
    arrNu = np.array(arr)
    arr2 = np.transpose(arrNu)
    arr2_ = arr2.tolist()
    
    for i in range(9):
        uniques_ = []
        for j in range(9):
            if str(type(arr2_[i][j])) != "<class 'list'>":
                uniques_.append(arr2_[i][j])
        for j in range(9):
            if str(type(arr2_[i][j])) == "<class 'list'>":
                k = [f for f in arr2_[i][j] if f not in uniques_]
                if len(k) == 1:
                    arr2_[i][j] = k[0]
                    flag_ += 1
                    print(flag_)
                else:
                    arr2_[i][j] = k

    arr2Nu = np.array(arr2_)
    arr = np.transpose(arr2Nu).tolist()            
    return arr

def removeList(arr):
    for i in range(9):
        for j in range(9):
            if (str(type(arr[i][j])) == "<class 'list'>"):
                arr[i][j] = 0

arr1 = zeroAnalyzer(arr)
printer(arr1)

arr1 = layer3(arr1)
printer(arr1)

arr1 = layer4(arr1)
printer(arr1)

removeList(arr1)
printer(arr1)


while(flag_ != 0):
    flag_ = 0
    arr1 = zeroAnalyzer(arr1)
    arr1 = layer3(arr1)
    arr1 = layer4(arr1)
    removeList(arr1)
    arr1 = zeroAnalyzer(arr1)
    arr1 = layer3(arr1)    
printer(arr1)

end = time()
print("Time taken = {}".format(end-start))