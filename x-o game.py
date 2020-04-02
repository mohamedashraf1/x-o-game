xo=[1,2,3,4,5,6,7,8,9]
z=[]
i=0
x=["x"]
o=["o"]
arr= [9,8,7,6,5,4,3,2,1,0]

for m in range(1,10):
    if (m%3==0):
        print(arr[m])
    else:
        print(arr[m],end=" | ")
pl1=input("player 1 enter x or o ")
if pl1==x[0] :
    pl2=o[0]
else :
    pl2==x[0]
while i<9:
    if i%2==0:
          pos=int(input("player 1 enter the position from 1:9"))
          if pos>9 :
              print ("you can only choose from 1:9 or the game will finish")
              pos=int(input("now please enter the number again from 1:9"))
          for r in range(i):
                 if z[r]==pos:
                      pos=int(input("enter another number"))
          z.append(pos)
          
          
    else :
        
        pos=int(input("player 2 enter the position from 1:9"))
        if pos>9 :
              print ("you can only choose from 1:9 or the game will finish")
              pos=int(input("now please enter the number again from 1:9"))
        for r in range(i):
             if z[r]==pos:
                  pos=int(input("enter another number"))
        z.append(pos)
        
    
    if i%2==0:
          
          arr[pos] = pl1
          xo[pos-1]=pl1
          for m in range(1,10):
              if (m%3==0):
                  print(arr[m])
              else:
                 print(arr[m],end=" | ")
    else:
          
          arr[pos] = pl2
          xo[pos-1]=pl2
          for m in range(1,10):
              if (m%3==0):
                  print(arr[m])
              else:
                 print(arr[m],end=" | ")    

    i+=1   
    if pl1==x[0]:
      
       if xo[0]==xo[1]==xo[2]==x[0] or xo[0]==xo[3]==xo[6]==x[0] or xo[0]==xo[4]==xo[8]==x[0] or xo[1]==xo[4]==xo[7]==x[0] or xo[2]==xo[5]==xo[8]==x[0] or xo[2]==xo[4]==xo[6]==x[0] or xo[3]==xo[4]==xo[5]==x[0] or xo[6]==xo[7]==xo[8]==x[0] :
           print ("player 1 won")
           break
       elif xo[0]==xo[1]==xo[2]==o[0] or xo[0]==xo[3]==xo[6]==o[0] or xo[0]==xo[4]==xo[8]==o[0] or xo[1]==xo[4]==xo[7]==o[0] or xo[2]==xo[5]==xo[8]==o[0] or xo[2]==xo[4]==xo[6]==o[0] or xo[3]==xo[4]==xo[5]==o[0] or xo[6]==xo[7]==xo[8]==o[0] :
           print ("player 2 won")
           break
       else:
           if i==9:
               print("the game is darw")
    
    elif(pl1==o[0]):
        if xo[0]==xo[1]==xo[2]==x[0] or xo[0]==xo[3]==xo[6]==x[0] or xo[0]==xo[4]==xo[8]==x[0] or xo[1]==xo[4]==xo[7]==x[0] or xo[2]==xo[5]==xo[8]==x[0] or xo[2]==xo[4]==xo[6]==x[0] or xo[3]==xo[4]==xo[5]==x[0] or xo[6]==xo[7]==xo[8]==x[0] :
           print ("player 2 won")
           break
        elif xo[0]==xo[1]==xo[2]==o[0] or xo[0]==xo[3]==xo[6]==o[0] or xo[0]==xo[4]==xo[8]==o[0] or xo[1]==xo[4]==xo[7]==o[0] or xo[2]==xo[5]==xo[8]==o[0] or xo[2]==xo[4]==xo[6]==o[0] or xo[3]==xo[4]==xo[5]==o[0] or xo[6]==xo[7]==xo[8]==o[0] :
           
           print ("player 1 won")
           break
         
        else:
           if i==9:
               print("the game is darw")
print ("game over")
