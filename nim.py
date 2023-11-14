import random

def user_move(coins):
    while True:
        try:
            user_input = int(input("\nPlease enter the number of coins you want to take (1 or 2): "))
            if user_input in [1, 2] and user_input <= coins:
                return user_input
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

def robot_move(coins):
    if coins % 3 == 0:
        return random.choice([1, 2])
    else:
        return (coins % 3)

def play_game():
    coins = 0

    while True:
        try:
            user_input = int(input("Choose if you want to go first (1) or second (2): "))
            if user_input in [1, 2]:
                if user_input == 1:
                    coins = random.randint(10, 30)
                    if coins % 3 != 0:
                        coins = (coins//3)*3
                    print(f"You chose to go first, initial number of coins: {coins}")
                else:
                    coins = random.randint(10, 30)
                    if coins % 3 == 0:
                        coins = coins - random.randint(1, 2)
                    print(f"You chose to go second, initial number of coins: {coins}")
                    robot_coins = robot_move(coins)
                    coins -= robot_coins
                    print(f"The robot took {robot_coins} coins, {coins} remaining.")
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

    while coins > 0:
        user_coins = user_move(coins)
        coins -= user_coins
        print(f"You took {user_coins} coins, {coins} remaining.")

        if coins == 0:
            print("Congratulations, you won!")
            break

        robot_coins = robot_move(coins)
        coins -= robot_coins
        print(f"The robot took {robot_coins} coins, {coins} remaining.")

        if coins == 0:
            print("The robot won!")
            break

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play another round? (y/n): ")
        if play_again.lower() != 'y':
            break
