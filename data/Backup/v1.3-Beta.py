import discum, re, time, multiprocessing, json, datetime, random

version = 'v1.1'
print("Pokemon Minigame V1.1 by konoaru \nA FOSS pokemon game")

print("Press enter to catch pokemon !!! and help for more command")

press = input()

if press == "":
    print("A new wild pokemon has appeared !")
    print("You have the pokemon in : ")
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    
    # Choisir un fichier en fonction des probabilités
    rand = random.random()
    if rand < 0.0001:
        file_path = 'data/mythical.json'
    elif rand < 0.0003:
        file_path = 'data/legendary.json'
    else:
        file_path = 'data/pokemon.json'
    
    # Lire une ligne aléatoire du fichier choisi
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        chosen_line = random.choice(lines).strip()
    
    print(chosen_line)
    
    # Ajouter la ligne au fichier inventory.json
    with open('data/inventory.json', 'a', encoding='utf-8') as inventory_file:
        inventory_file.write(chosen_line + '\n')
    
    # Choisir un nombre entre 1 et 100 avec les probabilités spécifiées
    number = random.choices(range(1, 101), weights=range(100, 0, -1))[0]
    
    # Ajouter le nombre au fichier inventory.json
    with open('data/inventory.json', 'a', encoding='utf-8') as inventory_file:
        inventory_file.write(f"{chosen_line} - {number}\n")

elif press == "help":
    print("Help command : ")
    print("enter = catch a pokemon")
    print("Close the picture = end the script")
    print("DONT EDIT THE SCRIPT AND DELETE FILES INTO THE FILES")
    print("")
    print("More commands in the V2.0 See you soon :)")

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
