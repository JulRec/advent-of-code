with open("input.txt") as f:
    parsed_input = f.read().splitlines()

# get the path to each folder
directory_sizes = {}
path = [""]

for line in parsed_input:
    split_line = line.split()

    if "ls" in split_line or "dir" in split_line or "/" in split_line:
        continue

    elif "cd" in line:
        if ".." in line:
            path.pop()
        else:
            path.append(line[-1])

    # found a file, add it's size to all parents
    else:
        # print(line)
        # print(path)
        file_size = int(line.split()[0])
        print("file_size", file_size)

        # continue

        parents = "/".join(path)
        print(parents)

        while len(parents) > 0:
            # print(parents, len(parents))
            if parents in directory_sizes:
                directory_sizes[parents] += file_size
            else:
                print("initializing key", parents)
                directory_sizes[parents] = file_size
            parents = parents[:-2]
            # print(parents)

            # print(directory_sizes)
            print("-----")

    print(path)
print(directory_sizes)

total_directory_size = 0
for _, size in directory_sizes.items():
    if size <= 100000:
        total_directory_size += size

print(
    "Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?"
)
print(total_directory_size)

# 1029024 too low


currentPath = []
folders = {}


def pathToString(pathList):
    out = ""
    if len(pathList) == 1:
        return "/"
    for e in pathList:
        if out == "":
            out = e
        elif out[-1] == "/":
            out += e
        else:
            out += "/" + e
    return out


for l in parsed_input:
    if "$ cd .." in l:
        currentFolder = currentPath.pop()
        strPath = pathToString(currentPath)
    elif "$ cd" in l:
        currentFolder = l.split()[-1]
        currentPath.append(currentFolder)
        strPath = pathToString(currentPath)
        if strPath not in folders.keys():
            folders[strPath] = 0
    elif l.split()[0].isdigit():
        fsize, fname = l.split()
        for i in range(len(currentPath) - 1, 0, -1):
            parentPath = pathToString(currentPath[:i])
            folders[parentPath] += int(fsize)
        folders[strPath] += int(fsize)
# part 1
totalSum = 0
for f in folders.keys():
    if folders[f] <= 100000:
        totalSum += folders[f]
print("part1: ", totalSum)

# part 2
freeMem = 70000000 - folders["/"]
minSize = freeMem
for f in folders.keys():
    if folders[f] + freeMem >= 30000000:
        if folders[f] < minSize:
            minSize = folders[f]
print("Part2: ", minSize)
