def Recursive_Bubble_Sort(Liste):
    '''
    The recursive version of Bubble Sort has no advantage against the normal 
    version. It's just for exercising algorithms and recursion.
    '''
    for i in range(len(Liste)): 
        try: 
            if Liste[i+1] < Liste[i]: 
                Liste[i], Liste[i+1] = Liste[i+1], Liste[i] 
                Recursive_Bubble_Sort(Liste)
        except IndexError:
            pass
    return Liste 

if __name__ == '__main__':
    Liste1= [2,3,1,4,0]
    print(Recursive_Bubble_Sort(Liste1))