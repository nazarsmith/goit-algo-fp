import random
import matplotlib.pyplot as plt
import numpy as np

def probability(sums, sought_sum):
    num_of_sought_sums = len([i for i, x in enumerate(sums) if x == sought_sum])
    return num_of_sought_sums / len(sums) * 100

def task_7(num_experiments = 1000):
    # generate pairs of throws
    throws = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(num_experiments)]
    # get the sums of the throws
    sums = [sum(two_throws) for two_throws in throws]

    probabilities = []
    for i in range(2, 13):
        probabilities.append((i, probability(sums, sought_sum = i)))

    for p in probabilities:
        print(f"{p[0]}: {p[1]}")
    return probabilities

if __name__ == "__main__":
    probabilities = task_7(10000)
    bars = [prob[1] for prob in probabilities]
    ticks = [prob[0] for prob in probabilities]

    # build a bar chart to represent the results
    width = 0.5
    fig = plt.subplots(figsize = (10,6))
    br1 = np.arange(len(probabilities)) 
    
    plt.bar(br1, bars, color ='g', width = width, 
            edgecolor ='green', label ='Probabilities', alpha=0.7) 
    plt.xlabel('Sums', fontweight ='bold', fontsize = 12) 
    plt.ylabel('Probabilities, %', fontweight ='bold', fontsize = 12) 
    plt.xticks([r for r in range(len(probabilities))], ticks)
    
    plt.legend()
    plt.show()
