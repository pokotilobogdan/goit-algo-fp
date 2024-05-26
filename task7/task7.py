from random import randint
import matplotlib.pyplot as plt


def roll_dices(number_of_dices):
    return [randint(1,6) for _ in range(number_of_dices)]

def calculate_probabilities(statistics: dict):
    probabilities = {}
    for key, value in statistics.items():
        if key == 'Total rolls':
            continue
        probabilities[key] = value/statistics['Total rolls']
    return {key: value for key, value in sorted(probabilities.items(), key=lambda item: item[0])}


if __name__ == '__main__':

    results = {'Total rolls': 0}
    
    number_of_dices = int(input("Скільки кубиків кидаємо? "))
    number_of_rolls = int(input("Скільки разів їх кидаємо? "))
    print()
    
    for _ in range(number_of_rolls):
        results['Total rolls'] += 1
        sum_value = sum(roll_dices(number_of_dices))
        if sum_value not in results.keys():
            results[sum_value] = 0
        results[sum_value] += 1

    probs = calculate_probabilities(results)
    

    # VISUALIZING TABLE WITH RESULTS

    for key, value in probs.items():
        print(f"{key:<5}{round(value*100, 2)}%")
    print()

    
    # VISUALIZING STASTISTICS
    
    plt.bar(probs.keys(), probs.values(), width=1, color='g', edgecolor='black')
    plt.show()
