def sum_coins(coins, change):
    coins.sort(reverse=True)
    index = 0
    used_coins = {}

    while change > 0 and index < len(coins):
        count_current_coins = change // coins[index]
        change = change % coins[index]

        if count_current_coins > 0:
            used_coins[coins[index]] = count_current_coins
        index += 1
    result = ""
    if change != 0:
        print('Error')
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"
        for value, count in used_coins.items():
            result += f"{count} coin(s) with value {value}\n"

    return result[:-1]


coins = [int(x) for x in input().split(', ')]
target_change = int(input())

print(sum_coins(coins, target_change))