import math
def population_growth(initial,rate,time):
    def exponential_growth():
        return initial+math.exp(rate*time)
    population=exponential_growth()
    print(round(population))
population_growth(100,1,10)
