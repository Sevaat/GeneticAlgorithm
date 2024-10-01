class GAParameters():
    def __init__(self):
        self._number_of_individuals = None
        self._proportion_of_elite_individuals = None
        self._number_of_eras = None
        self._gene_sets = None
        self._type_of_sample = None
        self._mutation_probability = None
        self._purpose = None
        self._recombination_type = None
        
    @property
    def number_of_individuals(self):
        return self._number_of_individuals
    
    @property
    def proportion_of_elite_individuals(self):
        return self._proportion_of_elite_individuals
    
    @property
    def number_of_eras(self):
        return self._number_of_eras
    
    @property
    def gene_sets(self):
        return self._gene_sets
    
    @property
    def type_of_sample(self):
        return self._type_of_sample
    
    @property
    def mutation_probability(self):
        return self._mutation_probability
    
    @property
    def purpose(self):
        return self._purpose
    
    @property
    def recombination_type(self):
        return self._recombination_type
    
    def __str__(self):
        text = 'НАСТРОЙКИ ГЕНЕТИЧЕСКОГО АЛГОРИТМА\n'
        text = f'{text}\n'
        text = f'{text}Количество особей в популяции: {self.number_of_individuals}\n'
        text = f'{text}Доля элитных особей от общего числа: {self.proportion_of_elite_individuals}\n'
        text = f'{text}Количество эпох ГА: {self.number_of_eras}\n'
        text = f'{text}Варианты генов: {self.gene_sets}\n'
        text = f'{text}Тип выборки (0-стандартная выборка; 1-стохастическая универсальная выборка): {self.type_of_sample}\n'
        text = f'{text}Вероятность мутации: {self.mutation_probability}\n'
        text = f'{text}Цель поиска (0-минимум; 1-максимум): {self.purpose}\n'
        text = f'{text}Тип рекомбинации (0-одноточечная; 1-двухточечная): {self._recombination_type}'
        
        return text
    
    
if __name__ == "__main__":
    from TestClass import Test
    ga_parameters = Test.get_ga_parameters()
    print(ga_parameters)