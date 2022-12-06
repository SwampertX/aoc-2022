with open('day6.in', 'r') as f:
    stream = f.read().strip()
    # for i in range(len(stream)-4):
    #     if len(set(stream[i:i+4])) == 4:
    #         print(i + 4)
    for i in range(len(stream)-14):
        if len(set(stream[i:i+14])) == 14:
            print(i + 14)
            break