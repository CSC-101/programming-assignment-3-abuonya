from data import CountyDemographics


# DESIGN RECIPE
    # Purpose of Function: takes a list of county demographic objects and returns the total 2014 population from all the counties provided in the list.
    # Input: list[CountyDemographics] **of type list  # Output Given Input: 318,857,056 **of type int
    # If I was Computer: take the county list, create a new variable set at 0, iterate through the list, accessing the index 'population', extracting its key-value pair at
    # '2014 Population', and adding its associated value to the new variable I set before. Lastly, return the total sum at the end of the loop.

def population_total(list:list[CountyDemographics] ) -> int:
    sum_of_2014_population = 0   # create variable to store sum of '2014 Population' values as function iterates through the list.

    for idx in list:
            anothertemp = list[idx]
            temp = anothertemp.population['2014 Population']
            sum_of_2014_population += temp

    print (sum_of_2014_population)
    return sum_of_2014_population



