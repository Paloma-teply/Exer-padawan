from random import shuffle, random

frutas = ["banana", "jabuticaba", "pitanga", "mirtilo", "morango", "abacaxi", "cereja"]
shuffle(frutas)
palavra = frutas[0]

digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Não tem essa letra!")

     print("" if erros >= 1 else "")
     linha2 = ""
     if erros == 2:
         linha2 = ""
     elif erros == 3:
         linha2 = ""
     elif erros >= 4:
         linha2 = ""
     linha3 = ""
     if erros == 5:
         linha3 += ""
     elif erros >= 6:
         linha3 += ""
     print("")
     if erros == 6:
         print("Que pena você perdeu!")
         break
