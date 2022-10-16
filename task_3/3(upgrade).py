massive = [2,4,5,7,8,5,9]
multi = []
multi = [ i*j for (i,j) in zip(massive [0: int(len(massive)/2+1): 1], 
                               massive [-1: int(len(massive)/2-1): -1])]

print(f"произведения пар чисел списка равна -{multi} \nпарой считаем первый и последний элемент, второй и предпоследний и.т.д. ") 