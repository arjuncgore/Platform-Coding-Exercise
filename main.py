import requests # Web-scraping library. Used to call methods from SWAPI. Python 'swapi' library wasn't importing


def get_all(endpoint): # Function to get all the data for a function.
    url = f"https://swapi.dev/api/{endpoint}/"
    results = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get("results", []))
            url = data.get("next")
        else:
            break
    return results

def get_index(name, character_list): # Function to return the index of a given character name
    for cindex in range (len(character_list)):
        if (name == character_list[cindex]["name"]):
            return cindex

def print_character(name, character_list, wanted_info): # Function to print the given information for a given character 
    c = get_index(name, character_list)

    information = character_list[c]

    for infon in wanted_info:
        print(str(infon) + ": " + str(information.get(infon, 'N/A')))

def fix_names(name_list, character_list): # Function to fix the list of names from the inputted to the real names
    new_list = []
    
    for i in range(len(name_list)):
        for cindex in range (len(character_list)):
                if ((name_list[i].title() in character_list[cindex]["name"]) and (name_list[i] != "")):
                    new_list += [character_list[cindex]["name"]]
    return new_list

def fix_attr(attr_list, character_list): # Function to fix the list of attributes from the inputted to the real attributes
    new_list = []
    
    for attr in attr_list:
        for character in character_list:
            if attr in character and attr != "" and attr != "name" and not (attr in new_list):
                new_list += [attr]
    return new_list

def url_numbers(urls):
    numbers = []
    for url in urls:
        parts = url.rstrip('/').split('/')
        if parts[-1].isdigit() and 1 <= int(parts[-1]) <= 99:
            numbers += [int(parts[-1])]
    return numbers

def print_vehicles(numbers, vehicles_list):
    for nvehicle in numbers:
        print("\n" + vehicles_list[nvehicle]["name"])
        for n in list(vehicles_list[nvehicle])[1:11]:
            print(n + ": " + vehicles_list[nvehicle][n])

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Loading Characters...")
characters = get_all("people") # Initializes list of characters


names = [] # Creating a list of all names
for character in characters:
    names += [character["name"]]

inp_name = "none"
inp_names = []
while True:
    if ((inp_name == "") or (inp_name == "all")): break
    for n in names: print (n)
    inp_name = input("\nCharacter Name (press ENTER to stop adding names, write 'all' if you want every character): ")
    inp_names += [inp_name]
    print("\n")

if "all" in inp_name: # Creating the final list of chosen characters
    chosen_names = names
else:
    chosen_names = fix_names(inp_names, characters)


attributes = [] # Creating a list of all attributes till gender
for attr in list(characters[0].keys())[:8]:
    attributes += [attr]


inp_attr = "none"
inp_attrs = []
while True:
    if ((inp_attr == "") or (inp_attr == "all")): break
    for a in attributes[1:]: print(a)
    inp_attr = input("Attribute (press ENTER to stop adding attributes, write 'all' if you want every attribute ): ")
    inp_attrs += [inp_attr]
    print("\n")


if "all" in inp_attrs: # Creating the final list of chosen attributes
    chosen_attrs = attributes[1:]
else:
    chosen_attrs = fix_attr(inp_attrs, characters)
    


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + "Character Information:" + "\n")

for name in chosen_names:
    print(name)
    print_character(name, characters, chosen_attrs)
    print("\n")

input("\nPress ENTER to continue")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Loading Vehicles...")
vehicles = get_all("vehicles") # Initializes list of vehicles

while True:
    character_vehicles = input("\nSuggest a character who's vehicles you want to learn about (press ENTER to stop):")
    print("\n")
    if character_vehicles == "": break # Ending the program

    
    try:
        chosen_char = fix_names([character_vehicles], characters)[0]
        print("Character: " + chosen_char)
        vehicle_names = characters[get_index(chosen_char, characters)]["vehicles"] # Creating a list of all vehicles of the chosen character
        vehicle_numbers = url_numbers(vehicle_names) # Getting a list of indexes of vehicle numbers
        
        if not vehicle_numbers: print("\nThis character does not exist or does not use any vehicles")
        print_vehicles(vehicle_numbers, vehicles)

    except:
        print("\nThis character does not exist or does not use any vehicles")

    print("\n\n")