import random

def simulate():
    return random.choice([1, -1, 0])

def mcts(iterations=1000):
    wins = 0
    for _ in range(iterations):
        result = simulate()
        wins += result
    return wins / iterations

if __name__ == "__main__":
    print("MCTS Result:", mcts())
