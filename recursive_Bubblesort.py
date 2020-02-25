def recursive_Bubblesort(Liste):
    for i, num in enumerate(Liste): 
        try: 
            if Liste[i+1] < num: 
                Liste[i] = Liste[i+1] 
                Liste[i+1] = num 
                recursive_Bubblesort(Liste)
        except IndexError:
            pass
    return Liste 

if __name__ == '__main__':
    Liste1= [2,3,1,4,0]
    print(recursive_Bubblesort(Liste1))