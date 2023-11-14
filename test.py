def parse_state(state_str):
    # 转换输入状态字符串为状态元组
    return tuple(() if peg == '0' else tuple(map(int, peg)) for peg in state_str.split())

def is_valid_move(src_peg, dest_peg):
    # 验证是否可以从一个peg移动到另一个peg
    return src_peg and (not dest_peg or src_peg[-1] < dest_peg[-1])

def get_next_states(state):
    # 生成所有可能的下一步状态
    next_states = []
    for i, src_peg in enumerate(state):
        for j, dest_peg in enumerate(state):
            if i != j and is_valid_move(src_peg, dest_peg):
                new_state = list(list(peg) for peg in state)
                ball = new_state[i].pop()
                new_state[j].append(ball)
                next_states.append(tuple(tuple(peg) for peg in new_state))
    return next_states

def bfs(start_state, end_state):
    queue = [(start_state, 0)]
    visited = set()

    while queue:
        current_state, moves = queue.pop(0)
        if current_state == end_state:
            return moves
        if current_state not in visited:
            visited.add(current_state)
            queue.extend((new_state, moves + 1) for new_state in get_next_states(current_state))
    
    return -1  # 如果没有找到解决方案，返回-1

# 输入/输出部分
initial_state_str = input("Enter the initial state: ")  # 例如输入："1 0 3 4"
final_state_str = input("Enter the final state: ")      # 例如输入："1 32 4 0"

initial_state = parse_state(initial_state_str)
final_state = parse_state(final_state_str)

minimum_moves = bfs(initial_state, final_state)
print("Output:", minimum_moves)
