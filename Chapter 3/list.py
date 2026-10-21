
import random

people = [
    {
        "name": "Alice Smith", 
        "occupation": "Quantum Cryptographer", 
        "gender": "Female"
    },
    {
        "name": "Bob Jones", 
        "occupation": "Deep Sea Marine Biologist", 
        "gender": "Male"
    },
    {
        "name": "Charlie Brown", 
        "occupation": "Astrophysicist", 
        "gender": "Male"
    },
    {
        "name": "Diana Prince", 
        "occupation": "Archaeological Conservator", 
        "gender": "Female"
    },
    {
        "name": "Ethan Hunt", 
        "occupation": "Cybersecurity Penetration Tester", 
        "gender": "Male"
    },
    {
        "name": "Fiona Gallagher", 
        "occupation": "Renewable Energy Engineer", 
        "gender": "Female"
    },
    {
        "name": "George Clark", 
        "occupation": "Forensic Linguist", 
        "gender": "Male"
    },
    {
        "name": "Hannah Abbott", 
        "occupation": "Ethical AI Researcher", 
        "gender": "Female"
    },
    {
        "name": "Ian Malcolm", 
        "occupation": "Chaos Theory Mathematician", 
        "gender": "Male"
    },
    {
        "name": "Julia Roberts", 
        "occupation": "Bio-Architectural Designer", 
        "gender": "Female"
    }
]

vehicles = [
    {"name": "Ford Model T", "type": "Car"},
    {"name": "Volkswagen Beetle", "type": "Car"},
    {"name": "Ford Mustang", "type": "Car"},
    {"name": "Toyota Corolla", "type": "Car"},
    {"name": "Porsche 911", "type": "Car"},
    {"name": "Honda Super Cub", "type": "Motorcycle"},
    {"name": "Harley-Davidson Fat Boy", "type": "Motorcycle"},
    {"name": "Triumph Bonneville", "type": "Motorcycle"},
    {"name": "Honda CB750", "type": "Motorcycle"},
    {"name": "Ducati 916", "type": "Motorcycle"}
]

def article(occupation):
    firstLetter = occupation[0]

    if firstLetter == 'A':
        return 'an'
    else:
        return 'a'

def pronoun(gender):

    if gender == 'Male':
        return 'He'
    else:
        return 'She'

for person in people:

    name = person['name']
    occupation = person["occupation"]
    gender = person["gender"]

    print(f"\n This is {name}.\n {pronoun(gender)} is {article(occupation)} {occupation}.")

def operation(type):
    if type == 'Car':
        return 'Driving Car'
    else:
        return 'Riding Motocycle'

print('\n---------------------------------------------')

random.shuffle(vehicles)

for i, person in enumerate(people):

    name = person['name']
    gender = person["gender"]

    vehicle = vehicles[i]['name']
    type = vehicles[i]['type']

    print(f"\n{name} likes {vehicle}.\nBecause {pronoun(gender).lower()} love {operation(type).lower()}.")