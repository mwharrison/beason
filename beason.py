import pprint
import itertools

slips = {
    43.17: [
        {"number": 1, "length": 50, "power": 50},
        {"number": 2, "length": 50, "power": 50},
    ],
    39.17: [
        {"number": 3, "length": 50, "power": 50},
        {"number": 4, "length": 50, "power": 50},
    ],
    39.00: [
        {"number": 5, "length": 50, "power": 50},
        {"number": 6, "length": 50, "power": 50},
    ],
    34.17: [
        {"number": 7, "length": 50, "power": 50},
        {"number": 8, "length": 40, "power": 50},
    ],
    34.58: [
        {"number": 9, "length": 40, "power": 50},
        {"number": 10, "length": 40, "power": 50},
    ],
    35.67: [
        {"number": 11, "length": 40, "power": 50},
        {"number": 12, "length": 30, "power": 30},
    ],
    24.08: [
        {"number": 13, "length": 30, "power": 30},
        {"number": 14, "length": 30, "power": 30},
    ],
    23.67: [
        {"number": 15, "length": 30, "power": 30},
        {"number": 16, "length": 30, "power": 30},
    ],
    24.00: [
        {"number": 17, "length": 30, "power": 30},
        {"number": 18, "length": 30, "power": 30},
    ]
}

boats = [
    {"name": "Power Play", "length": 57.00, "beam": 16.00},
    {"name": "Mystera", "length": 50.00, "beam": 14.90},
    {"name": "Beachcomber", "length": 49.00, "beam": 15.00},
    {"name": "Nautilus", "length": 47.00, "beam": 14.00},
    {"name": "Marie Ellis", "length": 45.00, "beam": 15.00},
    {"name": "SeaSun Ticket", "length": 41.00, "beam": 13.90},
    {"name": "Y Knot Another", "length": 41.00, "beam": 13.60},
    {"name": "Shell Seaker", "length": 40.50, "beam": 13.50},
    {"name": "Traveling Star", "length": 40.00, "beam": 14.00},
    {"name": "Seascape", "length": 37.00, "beam": 13.50},
    {"name": "Cambria", "length": 36.00, "beam": 12.50},
    {"name": "Sterling", "length": 36.00, "beam": 12.00},
    {"name": "Morning Star", "length": 35.00, "beam": 13.00},
    {"name": "Andiamo", "length": 35.00, "beam": 11.50},
    {"name": "Rainbow", "length": 47.00, "beam": 14.87},
    {"name": "Petite Fleur", "length": 30.00, "beam": 11.00},
    {"name": "Silhouette", "length": 27.00, "beam": 9.00},
    {"name": "2 4 Fun", "length": 26.50, "beam": 8.5},
    {"name": "Spirit", "length": 32.00, "beam": 11.00},
]

count = 0
for boat_pairs in itertools.combinations(boats, 2):
    pair_beam = round(boat_pairs[0]["beam"] + boat_pairs[1]["beam"], 2)
    print(boat_pairs)
    differences = []
    for width, slip_info in slips.items():
        difference = round(width - pair_beam, 2)
        if difference > 0:
            differences.append(difference)
        #print(boat_pairs[0]["name"], "|", boat_pairs[1]["name"], "|", slip_info[0]["number"], "and", slip_info[1]["number"], "|", pair_beam, "|", width, "|", difference)

    #print(differences)
    #print(min(i for i in differences if i > 0))

    for width, slip_info in slips.items():
        difference = round(width - pair_beam, 2)
        try:
            if difference == min(i for i in differences if i > 0):
                #print("First Boat: ", boat_pairs[0]["name"])
                #print("Second Boat: ", boat_pairs[1]["name"])
                #print("Slips: ", slip_info[0]["number"], "and", slip_info[1]["number"])
                #print("Combined Beams: ", pair_beam)
                #print("Slip Width: ", width)
                #print("Remaining Space: ", difference)
                #print("------------------------------")
                count = count + 1
        except ValueError:
            pass
print("Completed with {} pairs".format(count))
