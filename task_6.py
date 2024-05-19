

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

    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif costs[i - 1] <= w:
                K[i][w] = max(calories[i - 1] + K[i - 1][w - costs[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    selected_items = {}
    budget_copy = budget
    for i in range(n, 0, -1):
        if K[i][budget_copy] != K[i - 1][budget_copy]:
            item_name = items[i - 1][0]
            selected_items[item_name] = items[i - 1][1]
            budget_copy -= costs[i - 1]

    return K[n][budget], selected_items

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
    print("Dishes (GREEDY):", [{item[0]: item[1]} for item in total_greedy_order])

    total_dynamic_calories, selected_items = dynamic_programming(items, 135)
    print("\nTotal calories (DYNAMIC):", total_dynamic_calories)
    print("Dishes (DYNAMIC):", [{item: vals["cost"]} for item, vals in selected_items.items()])