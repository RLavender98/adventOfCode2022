data = open('input.txt').read().splitlines()

count = 0
for i in range(int(len(data) / 3)):
    for char in data[3 * i]:
        if char in data[3 * i + 1] and char in data[3 * i + 2]:
            if char.isupper():
                count += (ord(char) - 38)
            else:
                count += (ord(char) - 96)
            break

print(count)