import os
for number in range(6):
    nome = str(number)
    os.rename(nome + ".txt", nome + ".py")



