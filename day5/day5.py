def parse_cargo(cargo_raw):
    # return a list of stacks, from index 1 onwards
    cargo_raw = (cargo_raw.strip().split('\n'))[:-1]
    cargo_list = [[] for i in range(9)]
    for line in cargo_raw:
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                cargo_list[i//4].append(line[i])
    return [[]] + cargo_list
                
def parse_commands(commands_raw):
    commands_str = commands_raw.strip().split('\n')
    import re
    r = re.compile(r'move (\d+) from (\d+) to (\d+)')
    return [(int(i) for i in r.match(command_str).groups()) for command_str in commands_str]

with open('day5.in', 'r') as f:
    cargo, commands = f.read().strip().split('\n\n')
    cargo, commands = parse_cargo(cargo), parse_commands(commands)
    for command in commands:
        amt, src, dest = command
        # to pop from stack: pop(0)
        # to push on stack: insert(0, item)
        # for _ in range(amt):
        #     item = cargo[src].pop(0)
        #     cargo[dest].insert(0, item)
        items = cargo[src][:amt]
        cargo[src] = cargo[src][amt:]
        cargo[dest][0:0] = items
    print(''.join(stack[0] for stack in cargo[1:]))
