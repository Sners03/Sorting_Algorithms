def BubbleSort(Liste):
    changes = 1
    while changes != 0:
        changes = 0
        i=1
        while i < len(Liste):
            if Liste[i-1] > Liste[i]:
                Liste[i-1],Liste[i] = Liste[i],Liste[i-1]
                changes+=1
            i+=1
    return Liste

if __name__ == '__main__':
    Liste1= [2,3,1,4,0]
    print(BubbleSort(Liste1))