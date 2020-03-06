def Selection_Sort(Liste):
    def min(Liste):
        min = Liste[0]
        index_min=0
        for j in range(len(Liste)):
            if Liste[j] < min:
                min = Liste[j]
                index_min = j
        return index_min

    for i in range(len(Liste)):
        if len(Liste[i:])>1:
            index_min = min(Liste[i:])+i
            if Liste[index_min] is not Liste[i]:
                Liste[i], Liste[index_min] = Liste[index_min], Liste[i]
    return Liste

if __name__=='__main__':

    Liste1=[4,3,5,2,6,1,0]
    print(Selection_Sort(Liste1), '\n')

    Liste2=[1,9,8,7,6,5,0,4,3,2,1,2]
    print(Selection_Sort(Liste2), '\n')

    Liste3=[0,1,2,3,4,5]
    print(Selection_Sort(Liste3), '\n')