with open('day1.in', 'r') as f:
    chunks = f.read().strip().split('\n\n')
    intchunks = [[int(i) for i in chunk.strip().split('\n')] for chunk in chunks]
    bags = [sum(chunk) for chunk in intchunks]
    # print(max(bags))
    m1, m2, m3 = -1,-1,-1
    for bag in bags:
        if bag >= m1:
            m1, m2, m3 = bag, m1, m2
        elif bag >= m2:
            m2, m3 = bag, m2
        elif bag >= m3:
            m3 = bag
    print(m1 + m2 + m3)
