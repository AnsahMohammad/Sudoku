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

'''

arr1 = []
print("enter the Sudoku 9X9 row wise. put 0 if empty : ")
for i in range(9):
    print("enter the row {}".format(i+1))
    k = list(map(int,input().split()))
    arr1.append(k)

'''

print('hello \'n')

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
                    artemp.append(str(possible[0]))
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
        
    print(boxes)

printer(arr)
zeroAnalyzer(arr)
printer(arr1)
ViewBlocks(arr)
ViewBlocks(arr1)