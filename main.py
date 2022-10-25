import boyrazb
import dicefight
import shop




def game(player_hp, player_name, player_money, player_potions):
    print("1 - битва с разбойником")
    print("2 - игра в кости")
    print("3 - лавка ведьмы")


    while True:
        answer = input("Введите номер варианта и нажмите ENTER: ")
        if answer == "1" or answer == "2" or answer == "3":
            break
    # битва с разбойником
    if answer == "1":
        boyrazb.boyrazb(player_hp, player_name, player_money, player_potions)
    # кости
    elif answer == "2":
        dicefight.dice(player_hp, player_name, player_money, player_potions)
    # магаз
    elif answer == "3":
        shop.shop(player_hp, player_name, player_money, player_potions)

   # создаём героя
player_hp = 100
player_name  = "Александр Чергов"
player_money = 500
player_potions = 1



game(player_hp, player_name, player_money, player_potions)
