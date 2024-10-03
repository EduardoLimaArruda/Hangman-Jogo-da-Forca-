import random
from hangmanWords import ListaPalavra
from hangmanArt import stages, logo


vidas = 6

print(logo)

print("Jogo da forca :D")

ChooseWord = random.choice(ListaPalavra)

placeholder = ""
ListaPalavras = len(ChooseWord)
for position in range(ListaPalavras):
    placeholder += "_"
print(placeholder)

GameOver = False
LetraCerta = []

while not GameOver:
    Guess = input("\nDigite uma Letra: ").lower()

    if Guess in LetraCerta:
        print(f"Você já tentou: {Guess}")

    display = ""

    for Letra in ChooseWord:
        if Letra == Guess:
            display += Letra
            LetraCerta.append(Guess)
        elif Letra in LetraCerta:
            display += Letra
        else: 
            display += "_"

    print("Palavra para adivinhar " + display)

    if Guess not in ChooseWord:
        vidas -= 1
        print(f"Você tentou {Guess}, não está na palavra. Você perdeu uma vida")
        if vidas == 0:
            GameOver = True
            print("Você perdeu")

    if "_" not in display:
        GameOver = True
        print("Você ganhou")

    print(stages[vidas])


exit = input("Pressione Enter para encerrar!")