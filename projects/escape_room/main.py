print("You woke up in a strange and dark bedroom.")
print("You look around and see an old wardrobe, a tiny wooden table with two drawers, and a strange painting on the wall.")
print("You get up from the bed and try to leave the room, but the door is locked. Maybe the key is somewhere around here...")
while True:
    command = input("Where should i look first? (wardrobe/table/bed/painting) ").strip().lower()

    match command:
        case 'wardrobe':
            print('You walk to the wardrobe...')
            #inspect

        case 'table':
            print('You approach the wooden table...')
            #inspect
        
        case 'bed':
            print('You look under the bed...')
            #inspect