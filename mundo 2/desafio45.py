"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

"""

import random

def jokenpo():
  
    user_choice = input("Escolha entre pedra, papel e tesoura: ").lower()

   
    while user_choice not in ['pedra', 'papel', 'tesoura']:
        print("Opção inválida!")
        user_choice = input("Escolha entre pedra, papel e tesoura: ").lower()


    computer_choice = random.choice(['pedra', 'papel', 'tesoura'])


    print(f"\nVocê escolheu {user_choice}.")
    print(f"O computador escolheu {computer_choice}.\n")

    if user_choice == computer_choice:
        print("Empate!")
    elif user_choice == 'pedra' and computer_choice == 'tesoura':
        print("Você ganhou!")
    elif user_choice == 'papel' and computer_choice == 'pedra':
        print("Você ganhou!")
    elif user_choice == 'tesoura' and computer_choice == 'papel':
        print("Você ganhou!")
    else:
        print("Computador ganhou!")

if __name__ == '__main__':
    jokenpo()
