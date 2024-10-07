from src.models.IndividualClass import Individual
from src.models.GAParametersClass import GAParameters


class TargetFunction():
    
    @staticmethod
    def _get_rating_for_one(individual: Individual, ga_parameters: GAParameters) -> Individual:
        individual_parameters = individual.transcript_individual(ga_parameters)
        individual.rating = sum(individual_parameters)
        
        return individual
    
    @staticmethod
    def get_rating_for_everyone(population: [Individual], ga_parameters: GAParameters) -> [Individual]:
        for p in population:
            p = TargetFunction._get_rating_for_one(p, ga_parameters)
        
        return population