data = open('input.txt').read()

for i in range(len(data) - 13):
    if len({data[i], data[i+1], data[i+2], data[i+3],data[i+4], data[i+5], data[i+6], data[i+7], data[i+8], data[i+9], data[i+10], data[i+11], data[i+12], data[i+13]}) == 14:
        print(i+13+1)
        break
