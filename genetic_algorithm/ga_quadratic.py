#! /usr/bin/env python

"""
Very simple demo in which organisms try to minimise
the output value of a function
"""

from pygene.gene import FloatGene, FloatGeneMax
from pygene.organism import Organism, MendelOrganism
from pygene.population import Population

# parameters for quadratic equation
# has roots 3 and 5
a = 2
b = -16
c = 30


class XGene(FloatGene):
    """
    Gene which represents the numbers used in our organism
    Organism is a number of genes. 
    FloatGene is a data structure reprenting a floating point number.
    So our answer will be two of these genes (as we're looking for two roots. 

    Variables:
    mutAmt - default 0.1 - amount by which to mutate. The gene will will move this
        proportion towards its permissible extreme values
    randMin - default -1.0 - minimum possible value for this gene. Mutation will
        never allow the gene's value to be less than this
    randMax - default 1.0 - maximum possible value for this gene. Mutation will
        never allow the gene's value to be greater than this
    mutProb - default 0.01 - probability of a mutation occurring 
    """
    # genes get randomly generated within this range
    randMin = -100.0
    randMax = 100.0
    
    # probability of mutation
    mutProb = 0.1
    
    # degree of mutation
    mutAmt = 0.1

def quad(x):
    return a * x ** 2 + b * x + c

class QuadraticSolver(Organism):
    """
    Implements the organism which tries
    to solve a quadratic equation

    Variables:
    genome - a dict mapping gene names to gene classes
    mutateOneOnly - default False - dictates whether mutation affects one randomly chosen gene unconditionally,
        or all genes subject to the genes' individual mutation settings
    crossoverRate - default .5 - proportion of genes to split out to first child in each pair resulting from a mating

    """
    genome = {'x1':XGene, 'x2':XGene}
    
    def fitness(self):
        """
        Implements the 'fitness function' for this species.
        Organisms try to evolve to minimise this function's value
        """
        x1 = self['x1']
        x2 = self['x2']
        
        # this formula punishes for roots being wrong, also for
        # roots being the same
        badness_x1 = abs(quad(x1)) # punish for incorrect first root
        badness_x2 = abs(quad(x2)) # punish for incorrect second root
        badness_equalroots = 1.0 / (abs(x1 - x2)) # punish for equal roots
        return badness_x1 + badness_x2 + badness_equalroots

    def __repr__(self):
        return "<fitness=%f x1=%s x2=%s>" % (
            self.fitness(), self['x1'], self['x2'])


class QPopulation(Population):
    """
    A population of organisms. 

    Variables:
    species - Organism class or subclass, being the 'species' of organism comprising this population
    initPopulation - size of population to randomly create if no organisms are passed in to constructor
    childCull - cull to this many children after each generation
    childCount - number of children to create after each generation
    incest - max number of best parents to mix amongst the kids for next generation, default 10
    numNewOrganisms - number of random new orgs to add each generation, default 0
    initPopulation - initial population size, default 10
    mutants - default 0.1 - if mutateAfterMating is False, then this sets the percentage of mutated
        versions of children to add to the child population; children to mutate are selected based on fitness
    """

    species = QuadraticSolver
    initPopulation = 2
    
    # cull to this many children after each generation
    childCull = 5

    # number of children to create after each generation
    childCount = 50


# create a new population, with randomly created members

pop = QPopulation()


# now a func to run the population
def main():
    try:
        generations = 0
        while True:
            # execute a generation
            pop.gen()
            generations += 1

            # and dump it out
            #print [("%.2f %.2f" % (o['x1'], o['x2'])) for o in pop.organisms]
            best = pop.organisms[0]
            print("fitness=%f x1=%f x2=%f" % (best.get_fitness(), best['x1'], best['x2']))
            if best.get_fitness() < 0.5:
                break

    except KeyboardInterrupt:
        pass
    print("Executed", generations, "generations")


if __name__ == '__main__':
    main()


