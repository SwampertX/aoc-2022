with open('day3.in', 'r') as f:
    bags = f.read().strip().split('\n')
    total = 0
    # for bag in bags:
    #     first = bag[:len(bag)//2]
    #     second = bag[len(bag)//2:]
    #     for i in range(26):
    #         char = chr(ord('a') + i)
    #         if char in first and char in second:
    #             total += i + 1
    #         char = chr(ord('A') + i)
    #         if char in first and char in second:
    #             total += i + 27
    for i in range(0, len(bags), 3):
        three_bags = bags[i:i+3]
        for i in range(26):
            char = chr(ord('a') + i)
            if all(char in comp for comp in three_bags):
                total += i + 1
            char = chr(ord('A') + i)
            if all(char in comp for comp in three_bags):
                total += i + 27
    print(total)
