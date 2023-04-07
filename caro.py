turn="X"
print("X")
 
a = {}
def check(p,turn):
    for i in range(1,3+1,1):
        for v in range(1,3+1,1):
            if str(i) + str(v) == str(p):
                if a[i,v] == "-":
                    if turn =="X":
                        a[i,v] = "X"
                    else:
                       a[i,v] = "O"
                else:
                    return "daco"
 
def crtable():
    for i in range(1,3+1,1):
        for v in range(1,3+1,1):
            a[i,v] = "-"
 
 
 
 
def show():
    for i in range(1,3+1,1):
        print(a[i,1],a[i,2],a[i,3])
def checkwin():
    for i in range(1,3+1,1):
        if a[i,1]==a[i,2]==a[i,3]!="-" or a[1,i]==a[2,i]==a[3,i]!="-":
            return "win"
    if a[1,1]==a[2,2]==a[3,3]!="-" or a[1,3]==a[2,2]==a[3,1]!="-":
        return "win"
 
crtable()
op=0
for i in range(1,100000000000,1):
    print("Lượt của",turn)
    p=int(input('Chọn ô'))
    if check(p,turn) == "daco":
        print("Ô đã dc chọn")
    else:
        if turn=="X":
            turn="O"
        else:
            turn="X"
        show()
        if checkwin()=="win":
            print(turn,"thắng sau ",i," lượt")
            break
        op = op+1
        if op == 9:
            print("Hoà")
            break
