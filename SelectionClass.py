import random
from PopulationClass import Population
from GAParametersClass import GAParameters
from IndividualClass import Individual


class Selection():
    
    @staticmethod
    def standart_selection(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        elements = population
        weights = [p.rating for p in population]
        if ga_parameters.purpose == 0:
            weights.reverse()
        while True:
            parents = random.choices(elements, weights=weights, k=2)
            if parents[0] != parents[1]:
                return parents
    
    @staticmethod
    def stochastic_universal_sampling(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        elements = population
        weights = [p.rating for p in population]
        if ga_parameters.purpose == 0:
            weights.reverse()
        total_weight = sum(weights)
        pointer_distance = total_weight / 4
        points = [random.uniform(0, total_weight)]
        new_point = points[0]
        for i in range(3):
            new_point += pointer_distance
            if new_point > total_weight:
                new_point = 0 + new_point - total_weight
            else:
                points.append(new_point)
        points = sorted(points)
        j = 0
        current_weight = 0
        parents = []
        for i, w in enumerate(weights):
            current_weight += w
            if current_weight >= points[j]:
                parents.append(elements[i])
                j += 1
        
        return parents