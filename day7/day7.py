with open('day7/day7.in', 'r') as f:
    lines = f.read().strip().split('\n')
    root = dict()
    cwd = root
    path = [root]
    line_no = 0
    limit = 100_000
    while line_no in range(len(lines)):
        line = lines[line_no]
        cmd = line.strip().split(' ')[1:]
        match cmd[0]:
            case "ls":
                next_cmd = line_no + 1
                while next_cmd < len(lines) and '$' not in lines[next_cmd]:
                    next_cmd += 1
                files_dirs_lines = lines[line_no+1: next_cmd]
                files_lines = [line for line in files_dirs_lines if 'dir ' != line[:4]]
                files = [(int(line.split(' ')[0]), line.split(' ')[1]) for line in files_lines]
                cwd['files'] = files

                dirs = [line.split(' ')[1] for line in files_dirs_lines if 'dir ' == line[:4]]
                for d in dirs:
                    cwd[d] = dict()
                    cwd[d]['files'] = []

                # jump directly
                line_no = next_cmd
                continue
            case "cd":
                dest = cmd[1] 
                match dest:
                    case "..":
                        path = path[:-1]
                        cwd = path[-1]
                    case "/":
                        cwd = root
                        path = [root]
                    case other:
                        cwd = cwd[dest]
                        path.append(cwd)
            case other:
                pass
        line_no += 1

    def get_size_tree(fs):
        if len(fs) == 1:
            # each file is (size, children)
            return [sum(f[0] for f in fs['files']), []]
        else:
            # children = [[size, [...]], [size, ...]]
            children = [get_size_tree(fs[d]) for d in fs.keys() if d != 'files']
            my_own_files = sum(f[0] for f in fs['files'])
            return [my_own_files + sum(child[0] for child in children), children]
    
    size_tree = get_size_tree(root)

    def count_tree(tree, limit):
        if tree[1] == []:
            return int(tree[0] <= limit) * tree[0]
        else:
            return int(tree[0] <= limit) * tree[0] + sum(count_tree(t, limit) for t in tree[1])
    
    print(count_tree(size_tree, limit))

    disk = 70000000
    need = 30000000
    used = size_tree[0]
    to_free = need - (disk - used)

    smallest = disk + 1
    # find the smallest directory whose size is >= to_free.

    def smallest_tree(tree, limit):
        if tree[1] == []:
            return tree[0] if tree[0] >= limit else disk + 1
        else:
            me = tree[0] if tree[0] >= limit else disk + 1
            return min(me, min(smallest_tree(t, limit) for t in tree[1]))
    
    print(f'used: {used}, free:{disk - used}, need to free:{to_free}')
    print(smallest_tree(size_tree, to_free))