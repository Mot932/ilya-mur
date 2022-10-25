import main
import os

def shop(player_hp, player_name, player_money, player_potions):
    while True:
        os.system("cls")
        print(f"{player_name} приехал в лавку ведьмы.")
        print(f"здоровье {player_money}")
        print(f"валюты {player_money}")
        print(f"зелья {player_potions}")
        print("1 - купить зелье за 200 валюты")
        print("2 - уйти")

        while True:
            answer = input("Введите номер варианта и нажмите ENTER: ")
            if answer == "1" or answer == "2":
                break

        if answer == "1":
            if player_money >= 200:
                player_money -= 200
                player_potions += 1
                print(f"{player_name} купил зелье")
            else:
                print("У вас нет столько монет!")


        elif answer == "2":
            main.game(player_hp, player_name, player_money, player_potions) # уехал от камня)
