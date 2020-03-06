def Bubble_Sort(Liste):
    for i in range(len(Liste)):
        for j in range(len(Liste)-i-1):
            if Liste[j] > Liste[j+1]:
                Liste[j+1],Liste[j] = Liste[j],Liste[j+1]
    return Liste

if __name__ == '__main__':
    Liste1= [2,3,1,4,0]
    print(Bubble_Sort(Liste1))