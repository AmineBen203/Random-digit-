import random 
N = int(input("Enter range of how many digits you want: "))
print(''.join(random.choice('0123456789ABCDEF')for i in range(N)))