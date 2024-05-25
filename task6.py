from colorama import Fore
import copy


def greedy_algorithm(meals: dict(dict()), value: int):
    
    # Let's calculate the answer through the calories-cost ratio
    sorted_by_ratio = {key: value for key, value in sorted(meals.items(), key=lambda item: item[1]['calories']/item[1]['cost'], reverse=True)}
    # print(sorted_by_ratio)
    # print()
    
    total_calories = 0
    total_cost = 0
    bought_meal = []

    for name, stats in sorted_by_ratio.items():
        if value >= stats['cost']:
            value -= stats['cost']
            bought_meal.append(name)
            total_cost += stats['cost']
            total_calories += stats['calories']
    return "Food bought: " + ', '.join(bought_meal) + "\n" + f"Total calories: {total_calories}" + '\n' + f"Total cost: {total_cost}"


def dynamic_programming(value, meals: dict, n):
    
    # Створюємо таблицю K для зберігання оптимальних значень підзадач
    # Елементом таблиці є список. Першим елементом списку є оптимальний набір калорій на задану кількість грошей.
    # Другим елементом списку є перелік їжі, яку для цього треба купити
    K = [[[0, []] for _ in range(value + 1)] for _ in range(n + 1)]

    for i, meal_name in enumerate(meals.keys()):
        
        # Перебираємо всі ціни щоразу, коли дивимось на новий предмет для покупки
        for cost_goal in range(value + 1):
            if cost_goal == 0:
                K[i+1][cost_goal][0] = 0
            
            # Якщо в нас вистачає грошей це купити, то перевіряємо, краще з цим предметом чи без нього:     max(з предметом, без предмету)
            if meals[meal_name]['cost'] <= cost_goal:
                # K[i+1][cost_goal][0] = max(meals[meal_name]['calories'] + K[i][cost_goal - meals[meal_name]['cost']][0], K[i][cost_goal][0])
                if meals[meal_name]['calories'] + K[i][cost_goal - meals[meal_name]['cost']][0] >= K[i][cost_goal][0]:
                    K[i+1][cost_goal][0] = meals[meal_name]['calories'] + K[i][cost_goal - meals[meal_name]['cost']][0]
                    K[i+1][cost_goal][1] = copy.copy(K[i][cost_goal - meals[meal_name]['cost']][1])
                    K[i+1][cost_goal][1].append(meal_name)
                else:
                    K[i+1][cost_goal][0] = K[i][cost_goal][0]
                    K[i+1][cost_goal][1] = K[i][cost_goal][1]
                    
                
            # Якщо не вистачає грошей, то предмет ми не можемо додати - результат такий же, як і до цього
            else:
                K[i+1][cost_goal][0] = K[i][cost_goal][0]
                K[i+1][cost_goal][1] = K[i][cost_goal][1]
        #     print(K[i][cost_goal], end=' ')
        # print()

    # return K[n][value]
    return "Food bought: " + ', '.join(K[n][value][1]) + "\n" + f"Total calories: {K[n][value][0]}" + '\n' + f"Total cost: {sum([meals[bought_meal]['cost'] for bought_meal in K[n][value][1]])}"            


if __name__ == "__main__":

    meals = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }


    value = int(input("How much money do we have? "))
    print()
    print()

    print(Fore.YELLOW + "Results of greedy algorithm:\n" + Fore.RESET)
    print(greedy_algorithm(meals, value))
    
    print()
    print()
    
    print(Fore.YELLOW + "Results of dynamic algorithm:\n" + Fore.RESET)
    print(dynamic_programming(value, meals, len(meals)), end=' ')
    print()
    