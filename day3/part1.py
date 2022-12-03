data = open('input.txt').read().splitlines()

rucksacks = []
for line in data:
    rucksacks.append([line[:int(len(line) / 2)], line[int(len(line) / 2):]])

count = 0
for rucksack in rucksacks:
    for char in rucksack[0]:
        if char in rucksack[1]:
            if char.isupper():
                count += (ord(char) - 38)
            else:
                count += (ord(char) - 96)
            break

print(count)