#Computador pensa num número e utilizador tenta adivinhar
import random 
x = random.randint(0,100)

t = 1
resposta = int (input ("Adivinhe o número em que estou a pensar. Está entre 0 e 100."))


while resposta != x :
    if resposta > x : 
        resposta = int (input ("O número em que pensei é menor. Tente novamente."))
    if resposta < x :
        resposta = int (input ("O número em que pensei é maior. Tente novamente."))
    t = t + 1

print (f"Acertou! Necessitou de {t} tentativas.")