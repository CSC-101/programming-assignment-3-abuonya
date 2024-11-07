# PART 1
# population_total(list[CountyDemographics]) -> int
#
# Define a function named population_total with one parameter (of type list[CountyDemographics]), a list of county demographics objects
# (note that this is a parameter of the function and is not necessarily the full data set). This function must return the total 2014
# Population across the set of counties in the provided list. If passed the full data set, then the expected result should be 318,857,056.

# DESIGN RECIPE
    # Purpose of Function: takes a list of county demographic objects and returns the total 2014 population from all the counties provided in the list.
    # Input: list[CountyDemographics] **of type list  # Output Given Input: 318,857,056 **of type int
    # If I was Computer: take the county list, create a new variable set at 0, iterate through the list, accessing the index 'population', extracting its key-pair at
    # '2014 Population', and adding its associated value to the new variable I set before. Lastly, return the total sum at the end of the loop.

