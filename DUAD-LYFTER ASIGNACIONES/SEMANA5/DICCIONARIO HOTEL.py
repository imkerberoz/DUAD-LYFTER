Hotel_Manson  = {
	'Name' : 'Manson',
	'Star Numbers': 4,
	'Room' : [
            {'Room Number': 1,'Floor': 9,'Price': 500.0,},
            {'Room Number': 44,'Floor': 1,'Price': 40.0,},
            {'Room Number': 20,'Floor': 5,'Price': 100.0,},
            {'Room Number': 30,'Floor': 2,'Price': 75.0,}
            ]
}

# ITERATE ROOMS AND SHOW PRICES AND FLOORS
for room in Hotel_Manson["Room"]:
    print(f"Room {room['Room Number']} : ${room['Price']}")

# ITERATE ROOMS AND SHOW ROOM NUMBERS AND FLOORS
for room in Hotel_Manson["Room"]:
    print(f"Room {room['Room Number']} : {room['Floor']}")

# SHOW HOTEL NAME AND STAR NUMBER
    print(f"{Hotel_Manson['Name']} : {Hotel_Manson['Star Numbers']} stars")

