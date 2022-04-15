import numpy as np
from time import time

start = time()

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

def firstLayer(arr):
    boxes = []
    column = 0
    rows = 0
    for bxCount in range(9):
        box = []
        for row in range(rows,rows+3):
            row_ = []
            for col in range(column,column+3):
                row_.append(arr[row][col])
            box.append(row_)
        boxes.append(box)
        
        column += 3
        if(bxCount%3 == 2):
            rows += 3
            column = 0
        
    print(boxes)

def printer(arr):
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

arr1 = []
def zeroAnalyzer(arr):
    count  = 0
    for i in range(9):
        artemp = []
        for j in range(9):
            if(arr[i][j] == 0):
                k = []
                for l in range(9):
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
                
                possible = [f for f in possible1 if f not in temp]
                #print(possible,end = ' ')
                if(len(possible) == 1):
                    artemp.append((possible[0]))
                else:
                    artemp.append(possible)
            else:
                #print(" {} ".format(arr[i][j]),end='')
                artemp.append(arr[i][j])
        arr1.append(artemp)

def ViewBlocks(arr):
    boxes = []
    column = 0
    rows = 0
    for bxCount in range(9):
        box = []
        for row in range(rows,rows+3):
            row_ = []
            for col in range(column,column+3):
                row_.append(arr[row][col])
            box.append(row_)
        boxes.append(box)
        
        column += 3
        if(bxCount%3 == 2):
            rows += 3
            column = 0
        
    return boxes

printer(arr)
zeroAnalyzer(arr)
printer(arr1)
ViewBlocks(arr)
boxes = ViewBlocks(arr1)


for count in range(9):
    hash = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for row in boxes[count]:
        for column in row:
            if str(type(column)) == "<class 'list'>":
                for element in column:
                    hash[element] += 1

    uniques = []
    for i in range(1,10):
        if hash[i] == 1:
            uniques.append(i)
            
    for row__ in range(3):
        for coulumn__ in range(3):
            if(str(type(boxes[count][row__][coulumn__])) == "<class 'list'>"):
                for commonEl in uniques:
                    if (commonEl in boxes[count][row__][coulumn__]):
                        if(count == 0):
                            arr1[row__][coulumn__] = commonEl
                        elif(count == 1):
                            arr1[row__][coulumn__+3] = commonEl
                        elif(count == 2):
                            arr1[row__][coulumn__+6] = commonEl
                        elif(count == 3):
                            arr1[row__+3][coulumn__] = commonEl
                        elif(count == 4):
                            arr1[row__+3][coulumn__+3] = commonEl
                        elif(count == 5):
                            arr1[row__+3][coulumn__+6] = commonEl
                        elif(count == 6):
                            arr1[row__+6][coulumn__] = commonEl
                        elif(count == 7):
                            arr1[row__+6][coulumn__+3] = commonEl
                        elif(count == 8):
                            arr1[row__+6][coulumn__+6] = commonEl
                        else:
                            raise "Unexpected Error 101"

printer(arr1)

for count in range(9):
    hash = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for rowEl in arr1[count]:
        if str(type(rowEl)) == "<class 'list'>":
            for element in rowEl:
                hash[element] += 1

    uniques = []
    for i in range(1,10):
        if hash[i] == 1:
            uniques.append(i)
            
    for coulumn__ in range(9):
        if(str(type(arr1[count][coulumn__])) == "<class 'list'>"):
            for commonEl in uniques:
                if commonEl in arr1[count][coulumn__]:
                    arr1[count][coulumn__] = commonEl
                    break
printer(arr1)

# column wise :

arrNu = np.array(arr1)
arr2 = np.transpose(arrNu)
arr2_ = arr2.tolist()

for count in range(9):
    hash = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for rowEl in arr2_[count]:
        if str(type(rowEl)) == "<class 'list'>":
            for element in rowEl:
                hash[element] += 1

    uniques = []
    for i in range(1,10):
        if hash[i] == 1:
            uniques.append(i)
            
    for coulumn__ in range(9):
        if(str(type(arr2_[count][coulumn__])) == "<class 'list'>"):
            for commonEl in uniques:
                if commonEl in arr2_[count][coulumn__]:
                    arr2_[count][coulumn__] = commonEl
                    break
arr2Nu = np.array(arr2_)
arr1 = np.transpose(arr2Nu).tolist()

printer(arr1)
end = time()

# --------------------------------------------------------------------------------------- #
# cycle and an error in column wise unique cycle

print("Total time taken : {}".format(end-start))
