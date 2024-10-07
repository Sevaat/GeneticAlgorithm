from .GAParametersClass import GAParameters

class Elite():
    
    @staticmethod 
    def get_size_elite(ga_parameters: GAParameters) -> int:

        size_elite = int(round(ga_parameters.number_of_individuals *
                               ga_parameters.proportion_of_elite_individuals)) 
        if ga_parameters.type_of_sample == 0:
            if (ga_parameters.number_of_individuals - size_elite) % 2 != 0:
                size_elite = size_elite + (ga_parameters.number_of_individuals - size_elite) % 2
        if ga_parameters.type_of_sample == 1:
            if (ga_parameters.number_of_individuals - size_elite) % 4 != 0:
                size_elite = size_elite + (ga_parameters.number_of_individuals - size_elite) % 4
        
        return size_elite
    
    
if __name__ == "__main__":
    pass