def show_instructions():
    print("""
    Welcome to the Adventure Game!
    Commands:
      go [direction]
      get [item]
    """)

def show_status():
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("---------------------------")

# An inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    }
}
