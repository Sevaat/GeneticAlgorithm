from GAParametersClass import GAParameters
import random
from GrayCodeConverterClass import GrayCodeConverter


class Individual():
    
    def __init__(self, code):
        self.code = code
        self.rating = None
        
    @classmethod
    def get_new_individual(cls, ga_parameters: GAParameters):
        new_individual = []
        for parameter_set in ga_parameters.gene_sets:
            individual_parameter = random.randint(0, len(parameter_set)-1)
            new_individual.append(individual_parameter)
        
        return cls(GrayCodeConverter.convert_to_code(new_individual, ga_parameters))
    
    def transcript_individual(self, ga_parameters: GAParameters):
        parameters = GrayCodeConverter.convert_from_code(self.code, ga_parameters)
        parameters = [ga_parameters.gene_sets[i][p] for i, p in enumerate(parameters)]
        
        return parameters
    
    def __str__(self):
        return f'{self.code} - {self.rating}'
    
    def __repr__(self):
        return f'{self.code} - {self.rating}'
    
    
if __name__ == "__main__":
    pass