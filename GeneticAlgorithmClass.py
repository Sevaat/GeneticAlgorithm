from GAParametersClass import GAParameters
from PopulationClass import Population
from TargetFunctionClass import TargetFunction
from SelectionClass import Selection
from RecombinationClass import Recombination
from IndividualClass import Individual
from MutationClass import Mutation


class GeneticAlgorithm():
    
    @staticmethod
    def search(ga_parameters: GAParameters) -> [Individual]:
        population = Population.get_new_population(ga_parameters)
        best_individuals = []
        
        for era in range(ga_parameters.number_of_eras):
            population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
            population = Population.sort_the_population(population, ga_parameters)
            population = population[:ga_parameters.number_of_individuals]
            
            #сохранение лучших особей
            best_individuals = best_individuals + Population.population_environments(population, ga_parameters)
            best_individuals = Population.sort_the_population(best_individuals, ga_parameters)
            best_individuals = Population.population_environments(best_individuals, ga_parameters)
            
            if era == ga_parameters.number_of_eras-1:
                return best_individuals
            
            children = []
            while True:
                parents = None
                if ga_parameters.type_of_sample == 0:
                    parents = Selection.standart_selection(population, ga_parameters)
                else:
                    parents = Selection.stochastic_universal_sampling(population, ga_parameters)
                new_individual = None
                if ga_parameters.recombination_type == 0:
                    new_individual = Recombination.single_point_crossing(parents)
                else:
                    new_individual = Recombination.two_point_crossing(parents)
                for ni in new_individual:
                    if ni not in children:
                        children.append(ni)
                
                if len(children) >= ga_parameters.number_of_individuals:
                    break
            
            population = Population.population_environments(population, ga_parameters)
            for c in children:
                if c not in population:
                    population.append(c)
            
            #добор особей, если после скрещивания их меньше, чем величина популяции
            if len(population) < ga_parameters.number_of_individuals:
                while True:
                    new_individual = Individual.get_new_individual(ga_parameters)
                    if new_individual not in population:
                        population.append(new_individual)
                    if len(population) == ga_parameters.number_of_individuals:
                        break
            
            population = Mutation.all_mutation(population, ga_parameters)
            
            
if __name__ == '__main__':
    pass