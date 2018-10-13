class Virus(object):
    '''
    Because every one of our simulations and tests will be
    utilizing specific virus paramters, it will be helpful
    for us to create a simple Virus class to minimize
    boilerplate code
    Plus... it is good practice :)

    We will be passing an intialize method into this class,
    taking in the following parameters:

    name: the name of the virus
    mortality_rate: the deadliness of the virus
    contagiousness: the contagiousness of the virus

    In our simulations, we will be using statistics from:
    https://www.theguardian.com/news/datablog/ng-interactive/2014/oct/15/visualised-how-ebola-compares-to-other-infectious-diseases

    We will also include a simple test to see if our viruse
    objects are properly being created
    '''

    def __init__(self, name, mortality_rate, contagiousness):
        self.name = name
        self.mortality_rate = mortality_rate
        self.contagiousness = contagiousness


def test_was_virus_created():
    virus = Virus("HIV", 0.8, 3.5)
    print(virus.name)
    print(virus.mortality_rate)
    print(virus.contagiousness)


# test_was_virus_created()
