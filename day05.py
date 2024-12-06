import numpy as np

def main():
    lines = []
    with open('input05.txt', 'r') as f:
         for line in f.readlines():
            line_split = line.split(',')
            line_split2 = line_split[1].split('->')
            lines.append(Line(int(line_split[0]), int(line_split2[0]), int(line_split2[1]), int(line_split[2])))
    print('part one: ' , part_one(lines))
    print('part two: ' , part_two(lines))


def part_one(lines):
    crossings = {}
    for l in lines:
        for p in l.covers(t2=False):
            crossings[p] = crossings.setdefault(p, 0)+1

    counter = 0
    for v in crossings.values():
        if v >= 2:
            counter += 1
    return counter
            

def part_two(lines):
    crossings = {}
    for l in lines:
        for p in l.covers(t2=True):
            crossings[p] = crossings.setdefault(p, 0)+1

    counter = 0
    for v in crossings.values():
        if v >= 2:
            counter += 1
    return counter

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def covers(self, t2=False):
        coords = []
        if self.x1 == self.x2:
            y1 = min(self.y1, self.y2)
            y2 = max(self.y1, self.y2)+1
            for y in range(y1, y2, 1):
                coords.append((self.x1, y))
        elif self.y1 == self.y2:
            x1 = min(self.x1, self.x2)
            x2 = max(self.x1, self.x2)+1
            for x in range(x1, x2, 1):
                coords.append((x, self.y1))
        elif self.x1 < self.x2 and self.y1 < self.y2 and t2:
            x = self.x1
            y = self.y1
            while x <= self.x2 and y <= self.y2:
                coords.append((x, y))
                x+=1
                y+=1
        elif self.x1 < self.x2 and self.y1 > self.y2 and t2:
            x = self.x1
            y = self.y1
            while x <= self.x2 and y >= self.y2:
                coords.append((x, y))
                x+=1
                y-=1
        elif self.x1 > self.x2 and self.y1 < self.y2 and t2:
            x = self.x1
            y = self.y1
            while x >= self.x2 and y <= self.y2:
                coords.append((x, y))
                x-=1
                y+=1
        elif self.x1 > self.x2 and self.y1 > self.y2 and t2:
            x = self.x1
            y = self.y1
            while x >= self.x2 and y >= self.y2:
                coords.append((x, y))
                x-=1
                y-=1

        return coords

main()