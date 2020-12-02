from operator import add
y1,x1=y,x=4,8
alphabet=" .o+=*BOX@%&#/^SE"
sample="d4:d3:fd:ca:c4:d3:e9:94:97:cc:52:21:3b:e4:ba:e9"
board=[[0 for _ in range(17)] for _ in range(9) ]
def movement(YX):
    return {"00":(-1,-1),"01":(-1,+1),"10":(+1,-1),"11":(+1,+1),}[YX]
def draw():
    print("+-----------------+")
    for j in range(len(board)):
        print("|",end="")
        for i in range(len(board[0])):
            print(alphabet[board[j][i]],end="")
        print('|')
    print("+-----------------+")
def move(YX):
    global y
    global x
    yy,xx=map(add,movement(YX),(y,x))
    if 0<=xx<=16:x=xx
    if 0<=yy<=8: y=yy
    board[y][x]=board[y][x]+1
l=list(''.join(sample.split(":")))
sample=list(map(lambda x:'{0:04b}'.format(int(x,16)),l))
sample=''.join([sample[i+1][2:4]+sample[i+1][0:2]+sample[i][2:4]+sample[i][0:2] for i in range(0,len(sample),2) ])
sample=[sample[i]+sample[i+1] for i in range(0,len(sample),2)]
list(map(lambda xy:move(xy),sample))
board[y1][x1]=15
board[y][x]=16
draw()