import numpy as np
from collections import namedtuple

my_tuple = namedtuple('my_tuple', 'input output')

def main():
    input = []
    with open('input08.txt', 'r') as f:
        for line in f.readlines():
            temp = line.split('|')
            input.append(my_tuple(process_input(temp[0]), process_input(temp[1])))
    
    print('part one: ' , part_one(input))
    print('part two: ' , part_two(input))

def process_input(input):
    temp = [x for x in input.split(' ') if x != '' and x != '\n']
    return [x[:-1] if '\n' in x else x for x in temp]

def part_one(input):
    sum = 0
    
    for x in input:
        temp = x.output
        for y in temp:
            if len(y) in [2, 4, 3, 7]:
                sum+=1

    return sum
    
def part_two(input):
    output = 0
    for x in input:
        my_map = Mapping(x.input)
        my_map.find_mapping()
        converted_numbers = my_map.convert(x.output)
        output += my_map.convert_to_int(converted_numbers)
    return output

class Mapping:
    def __init__(self, input):
        self.numbers = {}
        for x in input:
            if len(x) == 2:
                self.numbers['1'] = set(x)
            elif len(x) == 4:
                self.numbers['4'] = set(x)
            elif len(x) == 3:
                self.numbers['7'] = set(x)
            elif len(x) == 7:
                self.numbers['8'] = set(x)
            elif len(x) == 5:
                self.numbers.setdefault('235', []).append(set(x))
            elif len(x) == 6:
                self.numbers.setdefault('069', []).append(set(x))

    def find_mapping(self):
        self.mapping = {}
        key1 = (self.numbers['7'] - self.numbers['1']).pop()
        self.mapping[key1] = '1'

        key3 = (self.numbers['069'][0] & self.numbers['069'][1]  & self.numbers['069'][2] & self.numbers['1']).pop()
        self.mapping[key3] = '3'

        key7 = (self.numbers['235'][0] & self.numbers['235'][1] & self.numbers['235'][2] & self.numbers['4']).pop()
        self.mapping[key7] = '7'

        key2 = (self.numbers['1'] - set(key3)).pop()
        self.mapping[key2] = '2'

        key4 = (self.numbers['235'][0] & self.numbers['235'][1] & self.numbers['235'][2] - set(key1)-set(key7)).pop()
        self.mapping[key4] = '4'

        key5 = (self.numbers['8']-self.numbers['4']-set(key1)-set(key4)).pop()
        self.mapping[key5] = '5'

        key6 = (self.numbers['4']-self.numbers['1']-set(key7)).pop()
        self.mapping[key6] = '6'

    def convert(self, input):
        output = []
        for x in input:
            temp = []
            for s in x:
                temp.append(self.mapping[s])
            output.append(temp)

        return output

    def convert_to_int(self, input):
        output = ''
        for x in input:
            if set(x) == set('123456'):
                output+='0'
            elif set(x) == set('23'):
                output+='1'
            elif set(x) == set('12754'):
                output+='2'
            elif set(x) == set('12347'):
                output+='3'
            elif set(x) == set('6723'):
                output+='4'
            elif set(x) == set('16734'):
                output+='5'
            elif set(x) == set('134567'):
                output+='6'
            elif set(x) == set('123'):
                output+='7'
            elif set(x) == set('1234567'):
                output+='8'
            elif set(x) == set('123467'):
                output+='9'
        return int(output)


main()