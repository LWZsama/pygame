import random

def user_move(coins):
    while True:
        try:
            user_input = int(input("\n请输入您要拿的硬币数量 (1或2)："))
            if user_input in [1, 2] and user_input <= coins:
                return user_input
            else:
                print("无效的输入，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def robot_move(coins):
    if coins % 3 == 0:
        return random.choice([1, 2])
    else:
        return (coins % 3)

def play_game():
    coins = 0

    while True:
        try:
            user_input = int(input("请选择您是先手(1)还是后手(2)："))
            if user_input in [1, 2]:
                if user_input == 1:
                    coins = random.randint(10, 30)
                    if coins % 3 != 0:
                        coins = (coins//3)*3
                    print(f"您选择先手，初始硬币数量: {coins}")
                else:
                    coins = random.randint(10, 30)
                    if coins % 3 == 0:
                        coins = coins - random.randint(1, 2)
                    print(f"您选择后手，初始硬币数量: {coins}")
                    robot_coins = robot_move(coins)
                    coins -= robot_coins
                    print(f"机器人拿走了 {robot_coins} 个硬币，剩余 {coins} 个硬币。")
                break
            else:
                print("无效的输入，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

    while coins > 0:
        user_coins = user_move(coins)
        coins -= user_coins
        print(f"您拿走了 {user_coins} 个硬币，剩余 {coins} 个硬币。")

        if coins == 0:
            print("恭喜，您赢了！")
            break

        robot_coins = robot_move(coins)
        coins -= robot_coins
        print(f"机器人拿走了 {robot_coins} 个硬币，剩余 {coins} 个硬币。")

        if coins == 0:
            print("机器人赢了！")
            break

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\n要再来一局吗？(y/n)：")
        if play_again.lower() != 'y':
            break
