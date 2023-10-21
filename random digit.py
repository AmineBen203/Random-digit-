import random
X, N = int(input("Entrez combien de fois vous souhaite d'effectue tache: ")), int(input("Entrez combien des digit vous voulez: "))
for i in range(1, X+1, 1):
    print(''.join(random.choice('0123456789ABCDEF')for i in range(N)))
    


 
