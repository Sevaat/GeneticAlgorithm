import random
from IndividualClass import Individual


class Recombination():
    
    @staticmethod
    def single_point_crossing(parents: [Individual]) -> [Individual]:
        point = random.randint(1, len(parents[0].code) - 2)
        children = []
        
        for i, p1 in enumerate(parents):
            for p2 in parents[i+1:]:
                children.append(Individual(p1.code[0:point] + p2.code[point:]))
                children.append(Individual(p2.code[0:point] + p1.code[point:]))
        
        return children
    
    @staticmethod
    def two_point_crossing(parents: [Individual]) -> [Individual]:
        points = []
        while True:
            point1 = random.randint(1, len(parents[0].code) - 2)
            point2 = random.randint(1, len(parents[0].code) - 2)
            if point1 != point2:
                points.append(point1)
                points.append(point2)
                break
        points = sorted(points)
        children = []
        for i, p1 in enumerate(parents):
            for p2 in parents[i+1:]:
                children.append(Individual(p1.code[0:points[0]] + p2.code[points[0]:points[1]] + p1.code[points[1]:]))
                children.append(Individual(p2.code[0:points[0]] + p1.code[points[0]:points[1]] + p2.code[points[1]:]))
        
        return children