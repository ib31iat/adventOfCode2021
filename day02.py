import numpy as np

def main():
    print('part one: ' , part_one())
    print('part two: ' , part_two())

def part_one():
    x = 0
    y = 0
    with open('input2.txt', 'r') as f:
        for line in f.readlines():
            line_split = line.split(' ')
            direction = line_split[0]

            if direction == 'forward':
                x += int(line_split[1])
            elif direction == 'up':
                y -= int(line_split[1])
            elif direction == 'down':
                y += int(line_split[1])

    return x*y

        

def part_two():
    x = 0
    y = 0
    aim = 0
    with open('input2.txt', 'r') as f:
        for line in f.readlines():
            line_split = line.split(' ')
            direction = line_split[0]

            if direction == 'forward':
                amount = int(line_split[1])
                x += amount
                y += aim*amount
            elif direction == 'up':
                aim -= int(line_split[1])
            elif direction == 'down':
                aim += int(line_split[1])

    return x*y

main()