import random
import time
import json
import colorama

version = 'v1.1'
print("Pokemon Minigame V1.1 par Konoaru \n")

def weighted_random_choice():
    # Générer un nombre entre 1 et 1000 avec une distribution biaisée
    number = int(random.expovariate(1/200))
    return min(number, 1000)

while True:
    print("Appuie sur entrée pour attraper un pokemon !!! et tape help pour + de commande et d'info")
    press = input()

    if press == "":
        print("Oh ! un buisson a bougé devans vous")
        print("Vous avez lancee une pokeball !")
        print("5")
        time.sleep(0.5)
        print("4")
        time.sleep(0.5)
        print("3")
        time.sleep(0.5)
        print("2")
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        
        # Choisir un fichier en fonction des probabilités
        rand = random.random()
        if rand < 0.0001:
            file_path = 'data/mythical.json'
            print("\033[1;31mUn pokémon FABULEUX est apparu !\033[0m")
        elif rand < 0.0003:
            file_path = 'data/legendary.json'
            print("\033[1;33mUn pokemon LEGENDAIRE est apparu !\033[0m")
        else:
            file_path = 'data/pokemon.json'
            print("\033[1;32mun pokemon est apparu ! \033[0m")
        
        # Lire une ligne aléatoire du fichier choisi
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            chosen_line = random.choice(lines).strip()
        
        # Générer un nombre biaisé entre 1 et 1000
        number = weighted_random_choice()
        
        # Ajouter le nombre au fichier inventory.json
        with open('data/inventory.json', 'a', encoding='utf-8') as inventory_file:
            inventory_file.write(f"{chosen_line} - 'Level' {number}\n")

        print(chosen_line, "level :", number)

    elif press == "help":
        print("Help command : ")
        time.sleep (0.1)
        print("enter = attrape un pokemon")
        time.sleep (0.1)
        print("Ferme la fenetre = fini le script")
        time.sleep (0.1)
        print("inventory = Vois ton inventaire")
        time.sleep (0.1)
        print("")
        time.sleep (0.2)
        print("Sachez que le jeu est encore en dev !!! et que le Level max est 1000 !")
        print("")
        time.sleep (0.3)
        print("NE MODIFIEZ PAS LE CODE DU JEU ET NE MODIFIEZ PAS LE FICHIER DU JEU")
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
