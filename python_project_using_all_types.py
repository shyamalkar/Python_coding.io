import random

def play_alien_game():
    # 1. Numeric types: int (health, score), float (item weight)
    player_health = 100
    score = 0
    item_weight = 1.5

    # 2. Sequence types: list (inventory), string (name), range (for loop)
    inventory = ["Laser Gun"]
    locations = ("Crater", "Ship", "Tunnel")
    
    # 3. Mapping type: dict (location info)
    planet_map = {
        "Crater": "A deep, dark hole.",
        "Ship": "An abandoned alien vessel.",
        "Tunnel": "A narrow, glowing tunnel."
    }

    # 4. Set type: set (unique items collected)
    unique_treasures = set()

    # 5. Boolean type: bool (game state)
    game_over = False

    # 6. Binary type: bytes (encoded secret message)
    secret_code = b"x80x00alien" 

    print("Welcome to Alien Treasure Hunt!")

    while not game_over:
        print(f"\nHealth: {player_health} | Score: {score}")
        print(f"Inventory: {inventory}")
        
        # Using a list (sequence) to pick a random location
        current_loc = random.choice(locations)
        print(f"\nYou are in the: {current_loc}")
        print(f"Description: {planet_map[current_loc]}")

        action = input("Do you want to (s)earch or (q)uit? ").lower()

        if action == 's':
            # Numeric type usage
            damage = random.randint(10, 30)
            player_health -= damage
            
            # Sequence (list) update
            found_item = "Alien Crystal"
            inventory.append(found_item)
            unique_treasures.add(found_item) # Set usage
            score += 50
            print(f"You found an {found_item}! You took {damage} damage.")

        elif action == 'q':
            game_over = True # Boolean toggle

        # Check for game over condition
        if player_health <= 0:
            print("You have been defeated by the alien environment!")
            game_over = True

    print(f"\nGame Over. Final Score: {score}")
    print(f"Unique Treasures Collected: {len(unique_treasures)}")

if __name__ == "__main__":
    play_alien_game()
