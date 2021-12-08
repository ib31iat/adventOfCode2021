import numpy as np
from numpy.core.fromnumeric import shape

def main():
    input = []
    with open('input04.txt', 'r') as f:
        numbers = np.array(f.readline().split(','), dtype=int)
        lines = f.readlines()
    
    temp = []
    for l in lines:
        temp.extend(l.split(' '))

    temp = [int(x) for x in temp if x != '\n' and x != '']
    input = np.reshape(temp, newshape=(len(temp)//25, 5, 5))
    
    print('part one: ' , part_one(numbers, input))
    print('part two: ' , part_two(numbers, input))

def part_one(numbers, input):
    boards = []
    for i in input:
        boards.append(Board(i))

    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.check():
                return b.calc_score(n)
    
    
def part_two(numbers, input):
    boards = []
    for i in input:
        boards.append(Board(i))

    for n in numbers:
        eliminate = []
        for b in boards:
            b.mark(n)
            if b.check():
                if len(boards)==1:
                    return b.calc_score(n)
                else:
                    eliminate.append(b)
        for e in eliminate:
            boards.remove(e)

class Board:
    def __init__(self, matrix):
        self.drawn = np.zeros(shape=(5,5), dtype=int)
        self.matrix = matrix

    def check(self):
        rows = np.sum(self.drawn, axis=0)
        cols = np.sum(self.drawn, axis=1)

        return 5 in rows or 5 in cols

    def mark(self, x):
        for i in range(5):
            for j in range(5):
                if self.matrix[i,j] == x:
                    self.drawn[i,j] = 1

    def calc_score(self, x):
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if self.drawn[i,j] == 0:
                    unmarked_sum += self.matrix[i, j]
        return unmarked_sum*x

main()