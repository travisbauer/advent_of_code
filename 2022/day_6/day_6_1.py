file1 = open('input.txt', 'r')
lines = file1.readlines()
datastream_buffer = list(char for char in lines[0])

marker = 0
for i in range(len(datastream_buffer) - 3):
    if len([*set(datastream_buffer[i:i+4])]) == 4:
        marker = i+4
        break

print(f'marker: {marker}')