from TestClass import Test
from GeneticAlgorithmClass import GeneticAlgorithm


def main():
    ga_parameters = Test.get_ga_parameters()
    results = GeneticAlgorithm.search(ga_parameters)
    for r in results:
        print(f'Вариант {r.transcript_individual(ga_parameters)} с целевым параметром {r.rating}')
    
    
if __name__ == '__main__':
    main()