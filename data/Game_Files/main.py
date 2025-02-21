import random
import time
import json

version = 'v1.1'
print("Pokemon Minigame V1.1 par Konoaru \n")

def weighted_random_choice():
    number = int(random.expovariate(1/100))
    return min(number, 1000)

while True:
    print("Press enter for catch a pokemon ! or type help for more command !")
    press = input()

    if press == "":
        press = "1"
        print("Oh ! un buisson a bougé devans vous")
        press = "1"
        print("Vous avez lancée une pokeball !")
        press = "1"
        print("5")
        press = "1"
        time.sleep(1)
        press = "1"
        print("4")
        press = "1"
        time.sleep(1)
        press = "1"
        print("3")
        press = "1"
        time.sleep(1)
        press = "1"
        print("2")
        time.sleep(1)
        press = "1"
        print("1")
        time.sleep(1)
        press = "1"

        
        rand = random.random()
        if rand < 0.001:
            file_path = 'data/legendary.json'
            print("\033[1;33mUn pokemon LEGENDAIRE est apparu !\033[0m")
            time.sleep(3)
        else:
            if rand < 0.003:
                file_path = 'data/mythical.json'
                print("\033[1;31mUn pokemon FABULEUX est apparu !\033[0m")
                time.sleep(3)
            elif rand > 0.005:
                file_path = 'data/pokemon.json'
                print("\033[1;32mun pokemon est apparu ! \033[0m")
                time.sleep(0.5)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            chosen_line = random.choice(lines).strip()
        
        number = weighted_random_choice()
        
        with open('data/inventory.json', 'a', encoding='utf-8') as inventory_file:
            inventory_file.write(f"{chosen_line} - 'Level' {number}\n")

        print(chosen_line, "level :", number)
        press = "1"

    elif press == "help":
        print("Help command : ")
        time.sleep (0.1)
        print("enter = catch a pokemon")
        time.sleep (0.1)
        print("Close the window = end the script")
        time.sleep (0.1)
        print("inventory = Vois ton inventaire")
        time.sleep (0.1)
        print("")
        time.sleep (0.2)
        print("This game still in developement and the max level for a pokemon is 1000")
        print("")
        time.sleep (0.3)
        print("DO NOT EDIT THE CODE OR FILES OF THIS GAME")
        print("")
        print("More commands in the V2.0 See you soon :)")
        time.sleep (0.1)


    elif press == "inventory":
        with open('data/inventory.json', 'r', encoding='utf-8') as inventory_file:
            lines = inventory_file.readlines()
            pages = [lines[i:i + 25] for i in range(0, len(lines), 25)]
        
        current_page = 0
        while True:
            print(f"Page {current_page + 1}/{len(pages)}")
            for line in pages[current_page]:
                print(line.strip())
            
            command = input("Enter 'next' for next page, 'prev' for previous page, or 'exit' to leave: ")
            if command == 'next' and current_page < len(pages) - 1:
                current_page += 1
            elif command == 'prev' and current_page > 0:
                current_page -= 1
            elif command == 'exit':
                break
