# Platform Coding Exercise - Star Wars API (SWAPI)
This repo is my submission for the platform coding exercise as a display of my capablities as a programmer.

## Name
Arjun Gore

## Setup
The user's device must have the program installed and should be connected to the internet. It must also have Python 3 installed.

To use the `requests` library for API searches, the user must install `requests` using pip. This can be done with the following terminal command:
```sh
% pip install requests
```

## Usage
To run the program, navigate to the directory containing the script and execute it using Python:
```sh
% python main.py
```
Follow the on-screen prompts to interact with the program. The program is designed to be user-friendly and will guide you through each step.

## Program Explanation
Part 1:
It begins by listing every character in the database and asks the user to type any character they wish to find information for. If the user types "all", it will select every character. The user is allowed to type parts of their name, and it will work (e.g., typing "anakin" will choose "Anakin Skywalker"). When the user doesn't want to pick any more characters, they can just press ENTER to move on.
After the character selection, the program then lists all attributes the user would like to choose from. The user can type any of the given attributes to select them, and once again they may type "all" to choose every attribute. When the user is done picking attributes, they may press ENTER to move on.
After this, the program prints out each of the characters' names with their attributes in a nested list under each name.
The program will then ask the user to continue by pressing ENTER, moving the program to the second part.

Part 2:
The second part of the program allows the user to print out a list of every vehicle a chosen character operates, along with information about each vehicle.
The program will prompt the user to type a character's name. Similar to part 1, the user doesn't need to type the full name.
After the user selects a character, the program prints out each vehicle the character operates with every attribute provided by the API under.
Part 2 then repeats until the user doesn't enter a character name and simply presses ENTER.

## Next Steps
For this project, I spent around 2 hours learning about the SWAPI api and working on the functionality of this project. I then spent another 1-2 hours polishing it as much as I could.
I really enjoyed applying my knowledge in Python into manipulating data off a new API that I've never worked with before.However, I feel like my final printed outputs in this product could've looked slightly better.
If I had more time to work on this, I would try to arrange the data in a table format, which is hard to do without external libraries.
Additionally, if I had access to further libraries, I would have either created a Tkinter GUI to make a Wikipedia-esc application, or made the printed outputs in the format of a printed database.

## Platform
This project made me extremely excited to work with the Platform Integration and Automation team at Stevens. I've never had the opportunity to answer such an open-ended question to show off my skills, but it really played to my competitive personality. I found this work extremely fulfilling, and it was genuinely something I enjoyed programming. 
I really hope this project showcased my coding prowess well, and I get the opportunity to work with you!
