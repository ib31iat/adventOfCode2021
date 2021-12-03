import numpy as np

def main():
    input = np.loadtxt('input1.txt')
    print('part one: ' , part_one(input))
    print('part two: ' , part_two(input))

def tester():
    test1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7
    test2 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5

    if test1[1] == part_one(np.array(test1[0])):
        print('passed part one')
    else:
        print('failed part one')

    if test2[1] == part_two(np.array(test2[0])):
        print('passed part two')
    else:
        print('failed part two')

def part_one(l):
    if l.shape[0] == 0:
        return 0

    inc_list = [1 if x<y else 0 for x,y in zip(l, l[1:])]

    return sum(inc_list)

def part_two(l):
    if l.shape[0] == 0:
        return 0

    tripplets = list(zip(l, l[1:], l[2:]))
    inc_list = [1 if sum(list(x))<sum(list(y)) else 0 for x,y in zip(tripplets, tripplets[1:])]

    return sum(inc_list)


main()