

def greedy_algorithm(items: dict, budget: int):
    items = sorted(items.items(), key = lambda i: i[1]["cost"], reverse = True)
    total_order = []
    for item in items:
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_order.append([item[0], item[1]["cost"], item[1]["calories"]])
    return total_order

def dynamic_programming(items: dict, budget: int):

    items = sorted(items.items(), key = lambda i: i[1]["cost"], reverse = True)
    calories = [item[1]["calories"] for item in items]
    costs = [item[1]["cost"] for item in items]
    n = len(costs)

    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif costs[i - 1] <= w:
                K[i][w] = max(calories[i - 1] + K[i - 1][w - costs[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][budget]

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    total_greedy_order = greedy_algorithm(items, 135)
    print("Total calories (GREEDY):", sum([item[-1] for item in total_greedy_order]))

    total_dynamic_calories = dynamic_programming(items, 135)
    print("Total calories (DYNAMIC):", total_dynamic_calories)