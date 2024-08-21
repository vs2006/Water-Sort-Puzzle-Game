import random
def GenerateTubes(N):
    main=[]
    L1=[] #list for ensuring that each color is added only 4 times.
    for i in range(1,N+1):
        individualtube=[]
        for j in range(4):
            repeat=1
            while repeat==1:
                C=random.randint(1, N)
                count=0
                for num in L1:
                    if num==C:
                        count+=1
                if count==4:
                    repeat=1
                else:
                    repeat=0
            individualtube.append(C)
            L1.append(C)
        main.append(individualtube)
    return main

def CompletedTube(main, CompleteTubes=[]):
    i=1
    for ele in main:
        count=0
        if (len(ele) != 0):
            if ((ele in CompleteTubes) or (len(ele)<4)):
                None
            else:
                color=ele[0]
                for N in ele:
                    if (N==color):
                        count+=1
            if (count==4):
                print("Good Work! Tube",i,"is complete!")
                CompleteTubes.append(ele)
        i+=1
    return CompleteTubes

def FirstCheck(main, CompleteTubes=[]):
    i=1
    for ele in main:
        count=0
        if (len(ele) != 0):
            if ((ele in CompleteTubes) or (len(ele)<4)):
                None
            else:
                color=ele[0]
                for N in ele:
                    if (N==color):
                        count+=1
            if (count==4):
                CompleteTubes.append(ele)
        i+=1
    return CompleteTubes


def Play(main, CompleteTubes=[]):
    while (len(CompleteTubes)!=(len(main)-1)):
        TubeRemove=int(input("Enter the number of tube from which you want to take out the first color: "))
        color= main[TubeRemove-1][0]
        main[TubeRemove-1].remove(color)
        while True:
            TubeAdd=int(input("Enter the number of tube to which you want to add color at the top: "))
            if (len(main[TubeAdd-1])==4):
                print("This tube is full! Please choose another tube.")
            else:
                main[TubeAdd-1].insert(0,color)
                break
        length=len(main)
        number=1
        for i in range(length):
            print(number,'. ', sep='',end='')
            print(main[i])
            number+=1
        CompleteTubes= CompletedTube(main, CompleteTubes)
    print("Congratulations! You have won the game!")


choice='Y'
while (choice.upper()=='Y'):
    numoftubes=int(input("Enter the number of tubes: "))
    main=GenerateTubes(numoftubes)
    L=[]
    main.append(L)
    length=len(main)
    number=1
    for i in range(length):
        print(number,'. ', sep='',end='')
        print(main[i])
        number+=1
    CompleteTubes=[]
    CompleteTubes= FirstCheck(main, CompleteTubes)
    Play(main, CompleteTubes)
    choice=input("Do you want to play again?(Y/N) ")

        
            
