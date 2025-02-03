building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])  # Prints 828
print(building_heights["Ping An"])        # Prints 599

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"], 
    "fire": ["Aries", "Leo", "Sagittarius"], 
    "earth": ["Taurus", "Virgo", "Capricorn"], 
    "air": ["Gemini", "Libra", "Aquarius"]
}

print(zodiac_elements["earth"])  # Prints ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])   # Prints ['Aries', 'Leo', 'Sagittarius']


building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

# Uncommenting the next line would raise a KeyError
# print(building_heights["Landmark 81"])  # Raises KeyError

key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights[key_to_check])
else:
    print(f"{key_to_check} not found in building heights.")

zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Prints "Not a Zodiac element"

building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

print(building_heights.get("Shanghai Tower"))  # Prints 632
print(building_heights.get("My House"))        # Prints None



user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)  # Prints 100019

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)  # Prints 100000



raffle = {
    223842: "Teddy Bear", 
    872921: "Concert Tickets", 
    320291: "Gift Basket", 
    412123: "Necklace", 
    298787: "Pasta Maker"
}

print(raffle.pop(320291, "No Prize"))  # Prints "Gift Basket"
print(raffle)  # Updated dictionary

print(raffle.pop(100000, "No Prize"))  # Prints "No Prize"
print(raffle)  # Prints remaining items

# Example using health points
available_items = {
    "health potion": 10, 
    "cake of the cure": 5, 
    "green elixir": 20, 
    "strength sandwich": 25, 
    "stamina grains": 15, 
    "power stew": 30
}

health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)  # Remaining items
print(health_points)    # Updated health points


test_scores = {
    "Grace": [80, 72, 90], 
    "Jeffrey": [88, 68, 81], 
    "Sylvia": [80, 82, 84], 
    "Pedro": [98, 96, 95], 
    "Martin": [78, 80, 78], 
    "Dina": [64, 60, 75]
}

print(list(test_scores.keys()))  # Prints all keys

for student in test_scores.keys():
    print(student)  # Prints each student name


for score_list in test_scores.values():
    print(score_list)

biggest_brands = {
    "Apple": 184, 
    "Google": 141.7, 
    "Microsoft": 80, 
    "Coca-Cola": 69.7, 
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(f"{company} has a value of {value} billion dollars.")

pct_women_in_occupation = {
    "CEO": 28, 
    "Engineering Manager": 9, 
    "Pharmacist": 58, 
    "Physician": 40, 
    "Lawyer": 37, 
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print(f"Women make up {percentage} percent of {occupation}s.")
