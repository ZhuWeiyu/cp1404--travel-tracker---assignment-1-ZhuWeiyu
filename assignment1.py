"""
CP1404 2023 Assignment 1
Replace the contents of this module docstring with your own details
Name: Weiyu Zhu
Date started: 26/4/2023
https://github.com/JCUS-CP1404/cp1404--travel-tracker---assignment-1-ZhuWeiyu.git
"""

import csv
import random
FILENAME = 'places.csv'

def loadFile():
    with open(FILENAME) as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def saveFile(places):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow(place)

def count_unvisited(places):
    return sum(place[3] == "n" for place in places)

def list_places(places):
    for i, place in enumerate(places):
        print(f"*{i + 1}. {place[0]:<8} in {place[1]:<12} {place[2]:<2}")
    notVisted = count_unvisited(places)
    if notVisted == 0:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(places)} places. You still want to visit {notVisted} places.")

def recommend_place(places):
    notVisited = [place for place in places if place[3] == "n"]
    if len(notVisited) == 0:
        print("No places left to visit!")
    else:
        place = random.choice(notVisited)
        print(f"How about... {place[0]} in {place[1]}?")

def add_place(places):
    name, country, priority = '', '', ''
    while not name or not country or not priority.isdigit():
        if not name:
            name = input("Name: ")
            if not name:
                print("Input can not be blank")
        elif not country:
            country = input("Country: ")
            if not country:
                print("Input can not be blank")
        else:
            priority = input("Priority: ")
            if not priority:
                print("Input can not be blank")
            elif not priority.isdigit():
                print("Invalid input; enter a valid number")
            else:
                priority = int(priority)
                places.append((name, country, priority, "n"))
                print(f"{name} in {country} ({priority}) added to Travel Tracker")
                break

def mark_place(places):
    unvisited_count = count_unvisited(places)
    if unvisited_count == 0:
        print("You have visited all the places!")
        return

    list_places(places)
    while True:
        choice = input("Enter the number of the place you want to mark as visited: ")
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        pos = int(choice)
        if pos < 1 or pos > len(places):
            print(f"Invalid input. Please enter a number between 1 and {len(places)}.")
            continue
        break

    name, city, country, status = places[pos - 1]
    if status == "v":
        print(f"You have already visited {name} in {city}, {country}.")
    else:
        places[pos - 1][3] = "v"
        print(f"Congratulations! You have marked {name} in {city}, {country} as visited.")

def showMenu():
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")

def main():
    print("Travel Tracker 1.0 - by Weiyu Zhu")

    places = loadFile()
    print(f"{len(places)} places loaded from places.csv")
    while True:
        showMenu()
        menuChoice = input(">>> ")

        if menuChoice == "L":
            list_places(places)
        elif menuChoice == "R":
            recommend_place(places)
        elif menuChoice == "A":
            add_place(places)
        elif menuChoice == "M":
            mark_place(places)
        elif menuChoice == "Q":
            break
        else:
            print("Invalid menu choice")

    saveFile(places)
    print(f"{len(places)} places saved to {FILENAME}")
    print("Have a nice day :)")

main()