file1 = open('input.txt', 'r')
lines = file1.readlines()
datastream_buffer = list(char for char in lines[0])

marker = 0
for i in range(len(datastream_buffer) - 13):
    if len([*set(datastream_buffer[i:i+14])]) == 14:
        marker = i+14
        break

print(f'marker: {marker}')