from GAParametersClass import GAParameters
from IndividualClass import Individual
from EliteClass import Elite


class Population():
        
    @staticmethod
    def sort_the_population(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        sorted_population = sorted(population, key=lambda p: p.rating)
        if ga_parameters.purpose == 1:
            sorted_population.reverse()
        
        return sorted_population

    @staticmethod
    def population_environments(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        size_elite = Elite.get_size_elite(ga_parameters)
        
        return population[0:size_elite]
        
    @staticmethod
    def get_new_population(ga_parameters: GAParameters) -> [Individual]:
        population = []
        while True:
            individual = Individual.get_new_individual(ga_parameters)
            if individual not in population:
                population.append(individual)
            if len(population) == ga_parameters.number_of_individuals:
                break
            
        return population
            
    
if __name__ == "__main__":
    pass