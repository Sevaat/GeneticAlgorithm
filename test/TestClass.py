import unittest
import random

from src.models.GAParametersClass import GAParameters


from src.models.IndividualClass import Individual
from src.calculations.TargetFunctionClass import TargetFunction
from src.models.PopulationClass import Population
from src.utils.GrayCodeConverterClass import GrayCodeConverter
from src.models.EliteClass import Elite
from src.calculations.SelectionClass import Selection
from src.calculations.RecombinationClass import Recombination
from src.calculations.MutationClass import Mutation
from src.GeneticAlgorithmClass import GeneticAlgorithm


class Test():
    
    def get_ga_parameters():
        ga_parameters = GAParameters()
        ga_parameters._number_of_individuals = 5
        ga_parameters._proportion_of_elite_individuals = 0.2
        ga_parameters._number_of_eras = 2
        ga_parameters._gene_sets = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        ga_parameters._type_of_sample = 0
        ga_parameters._mutation_probability = 0.02
        ga_parameters._purpose = 0
        ga_parameters._recombination_type = 0
        
        return ga_parameters

class GrayCodeConverterClassTest(unittest.TestCase):
    def test_get_maximum_discharge(self):
        ga_parameters = Test.get_ga_parameters()
        result = GrayCodeConverter.get_maximum_discharge(ga_parameters)
        expected_result = [3, 3, 3]
        self.assertEqual(result, expected_result)
    
    def test_convert_to_code(self):
        ga_parameters = Test.get_ga_parameters()
        result = GrayCodeConverter.convert_to_code([0, 1, 2], ga_parameters)
        expected_result = '000001011'
        self.assertEqual(result, expected_result)
    
    def test_convert_from_code(self):
        ga_parameters = Test.get_ga_parameters()
        result = GrayCodeConverter.convert_from_code('000001011', ga_parameters)
        expected_result = [0, 1, 2]
        self.assertEqual(result, expected_result)

class IndividualClassTest(unittest.TestCase):
    def test_new_individual(self):
        result = str(Individual('000001011'))
        expected_result = '000001011 - None'
        self.assertEqual(result, expected_result)
    
    def test_get_new_individual(self):
        random.seed(1)
        ga_parameters = Test.get_ga_parameters()
        result = str(Individual.get_new_individual(ga_parameters))
        expected_result = '001110000 - None'
        self.assertEqual(result, expected_result)
        
    def test_transcript_individual(self):
        ga_parameters = Test.get_ga_parameters()
        individual = Individual('000001011')
        result = Individual.transcript_individual(individual ,ga_parameters)
        expected_result = [1, 7, 13]
        self.assertEqual(result, expected_result)
        
class EliteClassTest(unittest.TestCase):
    def test_get_size_elite_1(self):
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 0
        ga_parameters._number_of_individuals = 5
        result = Elite.get_size_elite(ga_parameters)
        expected_result = 1
        self.assertEqual(result, expected_result)
        
    def test_get_size_elite_2(self):
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 0
        ga_parameters._number_of_individuals = 6
        result = Elite.get_size_elite(ga_parameters)
        expected_result = 2
        self.assertEqual(result, expected_result)
    
    def test_get_size_elite_3(self):
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 1
        ga_parameters._number_of_individuals = 5
        result = Elite.get_size_elite(ga_parameters)
        expected_result = 1
        self.assertEqual(result, expected_result)
    
    def test_get_size_elite_4(self):
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 1
        ga_parameters._number_of_individuals = 6
        result = Elite.get_size_elite(ga_parameters)
        expected_result = 2
        self.assertEqual(result, expected_result)
        
class TargetFunctionClassTest(unittest.TestCase):
    def test_get_rating_for_everyone(self):
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        result = f'{population[0].rating}-{population[1].rating}-{population[2].rating}'
        expected_result = f'{1+7+13}-{2+8+14}-{3+9+15}'
        self.assertEqual(result, expected_result)

class PopulationClassTest(unittest.TestCase):
    def test_get_new_population(self):
        random.seed(1)
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._number_of_individuals = 2
        result = str(Population.get_new_population(ga_parameters))
        expected_result = '[001110000 - None, 011000010 - None]'
        self.assertEqual(result, expected_result)
        
    def test_sort_the_population_1(self):
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._purpose = 0
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        result = str(Population.sort_the_population(population, ga_parameters))
        expected_result = '[000001011 - 21, 001011010 - 24, 011010110 - 27]'
        self.assertEqual(result, expected_result)
        
    def test_sort_the_population_2(self):
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._purpose = 1
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        result = str(Population.sort_the_population(population, ga_parameters))
        expected_result = '[011010110 - 27, 001011010 - 24, 000001011 - 21]'
        self.assertEqual(result, expected_result)
        
    def test_population_environments(self):
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        result = str(Population.population_environments(population, ga_parameters))
        expected_result = '[000001011 - None]'
        self.assertEqual(result, expected_result)
        
class SelectionClassTest(unittest.TestCase):
    def test_standart_selection_1(self):
        random.seed(1)
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 0
        ga_parameters._purpose = 0
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        population = Population.sort_the_population(population, ga_parameters)
        result = str(Selection.standart_selection(population, ga_parameters))
        expected_result = [
            Individual('000001011'),
            Individual('011010110')
            ]
        expected_result = str(TargetFunction.get_rating_for_everyone(expected_result, ga_parameters))
        self.assertEqual(result, expected_result)
        
    def test_standart_selection_2(self):
        random.seed(1)
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 0
        ga_parameters._purpose = 1
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        population = Population.sort_the_population(population, ga_parameters)
        result = str(Selection.standart_selection(population, ga_parameters))
        expected_result = [
            Individual('011010110'),
            Individual('000001011')
            ]
        expected_result = str(TargetFunction.get_rating_for_everyone(expected_result, ga_parameters))
        self.assertEqual(result, expected_result)
        
    def test_stochastic_universal_sampling_1(self):
        random.seed(1)
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110'),
            Individual('110110110'),
            Individual('000000000')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 1
        ga_parameters._purpose = 0
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        population = Population.sort_the_population(population, ga_parameters)
        result = str(Selection.stochastic_universal_sampling(population, ga_parameters))
        expected_result = [
            Individual('000000000'),
            Individual('000001011'),
            Individual('001011010'),
            Individual('110110110')
            ]
        expected_result = str(TargetFunction.get_rating_for_everyone(expected_result, ga_parameters))
        self.assertEqual(result, expected_result)
        
    def test_stochastic_universal_sampling_2(self):
        random.seed(1)
        population = [
            Individual('000001011'),
            Individual('001011010'),
            Individual('011010110'),
            Individual('110110110'),
            Individual('000000000')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._type_of_sample = 1
        ga_parameters._purpose = 1
        population = TargetFunction.get_rating_for_everyone(population, ga_parameters)
        population = Population.sort_the_population(population, ga_parameters)
        result = str(Selection.stochastic_universal_sampling(population, ga_parameters))
        expected_result = [
            Individual('110110110'),
            Individual('011010110'),
            Individual('001011010'),
            Individual('000000000')
            ]
        expected_result = str(TargetFunction.get_rating_for_everyone(expected_result, ga_parameters))
        self.assertEqual(result, expected_result)
        
class RecombinationClassTest(unittest.TestCase):
    def test_single_point_crossing_1(self):
        random.seed(1)
        population = [Individual('000001011'), Individual('001011010')]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._recombination_type = 0
        result = str(Recombination.single_point_crossing(population))
        expected_result = str([Individual('001011010'), Individual('000001011')])
        self.assertEqual(result, expected_result)
    
    def test_single_point_crossing_2(self):
        random.seed(1)
        population = [
            Individual('001011010'),
            Individual('011010110'),
            Individual('110110110'),
            Individual('000000000')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._recombination_type = 0
        result = str(Recombination.single_point_crossing(population))
        expected_result = str([
            Individual('001010110'),
            Individual('011011010'),
            Individual('000110110'),
            Individual('111011010'),
            Individual('000000000'),
            Individual('001011010'),
            Individual('010110110'),
            Individual('111010110'),
            Individual('010000000'),
            Individual('001010110'),
            Individual('110000000'),
            Individual('000110110')
            ])
        self.assertEqual(result, expected_result)
        
    def test_two_point_crossing(self):
        random.seed(1)
        population = [Individual('001011010'), Individual('011010110')]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._recombination_type = 0
        result = str(Recombination.two_point_crossing(population))
        expected_result = str([Individual('001011010'), Individual('011010110')])
        self.assertEqual(result, expected_result)
        
class MutationClassTest(unittest.TestCase):
    def test_all_mutation_1(self):
        random.seed(1)
        population = [Individual('000000110')]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._mutation_probability = 0
        Mutation.all_mutation(population, ga_parameters)
        result = str(population)
        expected_result = str([Individual('000000110')])
        self.assertEqual(result, expected_result)
        
    def test_all_mutation_2(self):
        random.seed(1)
        population = [
            Individual('000000110'),
            Individual('000110110')
            ]
        ga_parameters = Test.get_ga_parameters()
        ga_parameters._mutation_probability = 0.5
        population = Mutation.all_mutation(population, ga_parameters)
        result = str(population)
        expected_result = str([
            Individual('011000110'),
            Individual('000000000')
            ])
        self.assertEqual(result, expected_result)
        
class GeneticAlgorithmClassTest(unittest.TestCase):
    def test_search(self):
        random.seed(1)
        ga_parameters = Test.get_ga_parameters()
        result = str(GeneticAlgorithm.search(ga_parameters))
        individual = Individual('001000010')
        individual.rating = 22
        expected_result = str([individual])
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()