import numpy as np

def main():
    input = []
    with open('input03.txt', 'r') as f:
        for line in f.readlines():
            input.append(list(line[:-1]))
    input = np.array(input, dtype=int)
    print('part one: ' , part_one(input))
    print('part two: ' , part_two(input))

def part_one(x):
    no_ones = sum(x)
    majority_cut = x.shape[0]/2
    gamma = ['1' if i > majority_cut else '0' for i in no_ones]
    epsilon = ['1' if i < majority_cut else '0' for i in no_ones]
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

def part_two(x):
    oxy = x
    ind = 0
    while oxy.shape[0]!=1:
        no_ones = sum(oxy)
        majority_cut = oxy.shape[0]/2
        crit = 1 if no_ones[ind] >= majority_cut else 0
        to_del = [i for i in list(range(oxy.shape[0])) if oxy[i][ind]!=crit]
        oxy = np.delete(oxy, to_del, axis=0)
        ind+=1

    co2 = x
    ind = 0
    while co2.shape[0]!=1:
        no_ones = sum(co2)
        majority_cut = co2.shape[0]/2
        crit = 1 if no_ones[ind] < majority_cut else 0
        to_del = [i for i in list(range(co2.shape[0])) if co2[i][ind]!=crit]
        co2 = np.delete(co2, to_del, axis=0)
        ind+=1


    return int(''.join(np.array(oxy[0], dtype=str)),2) * int(''.join(np.array(co2[0], dtype=str)),2)



main()