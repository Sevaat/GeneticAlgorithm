from IndividualClass import Individual
import random
from GAParametersClass import GAParameters
from GrayCodeConverterClass import GrayCodeConverter


class Mutation():
    
    @staticmethod
    def _mutation(individual: Individual, ga_parameters: GAParameters) -> Individual:
        p1 = ga_parameters.mutation_probability * 100
        p2 = 100 - p1
        while True:
            new_code = ''
            code = individual.code
            for c in list(code):
                new_c = None
                if c == '1':
                    new_c = random.choices(['0', '1'], weights=[p1, p2], k=1)
                else:
                    new_c = random.choices(['0', '1'], weights=[p2, p1], k=1)
                new_code = f'{new_code}{new_c[0]}'
                
            #проверка на корректные значения после мутации
            values = GrayCodeConverter.convert_from_code(new_code, ga_parameters)
            
            if all([v < len(ga_parameters.gene_sets[i]) for i, v in enumerate(values)]):
                return Individual(new_code)
    
    @staticmethod
    def all_mutation(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        new_population = []
        for ind in population:
            new_population.append(Mutation._mutation(ind, ga_parameters))
        
        return new_population
            
            
if __name__ == '__main__':
    pass