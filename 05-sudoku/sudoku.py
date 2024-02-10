import os


'''Global variables'''
path=os.path.dirname(__file__)
numz=[]

'''Difficulty/map selector'''
def cenzor(c):
    if c==1:
        print("easy")
    elif c==2:
        print("medium")
    elif c==3:
        print("hard")
    else:
        print("unsolvable")
    return

'''Map loading'''
def fileRead():
    f=open(f'{path}{os.sep}src{os.sep}orig.txt')
    
    for l in f:
        numz.append(l.split())
    f.close()


'''Drawing the (g)ui'''
def drawGUI():
    for i in range(len(numz)):
        for j in range(9):
            print(f'{numz[i][j]}',end=' ')    
        print()

'''Main function that handles the game states and flow'''
def main():
    fileRead()
    drawGUI()
    cenzor(1)

'''Python convention for script starting (making sure this is the main script that gets executed(?))'''
if __name__ == "__main__":
    main()
