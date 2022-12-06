data = open('input.txt').read()

for i in range(len(data) - 3):
    if len({data[i], data[i+1], data[i+2], data[i+3]}) == 4:
        print(i+3+1)
        break
