import numpy as np

def main():
    input = np.loadtxt('input06.txt', delimiter=',', dtype=int)
    no_fish = np.zeros(shape=(9), dtype=int)
    for x in input:
        no_fish[x]+=1
    print('part one: ' , part_one(no_fish))
    print('part two: ' , part_two(no_fish))

def part_one(no_fish):
    return calc_population(no_fish, 80)
        

def part_two(no_fish):
    return calc_population(no_fish, 256)

def calc_population(no_fish, days):
    for _ in range(days):
        temp = np.zeros(shape=(9), dtype=int)
        for i, j in enumerate(no_fish[1:]):
            temp[i] = j
        temp[6] += no_fish[0]
        temp[8] = no_fish[0]
        no_fish = temp

    return sum(no_fish)


main()