from build_data import get_data
from data import CountyDemographics
import build_data



# PART 1
# DESIGN RECIPE
    # Purpose of Function: takes a list of county demographic objects and returns the total 2014 population from all the counties provided in the list.
    # Input: list[CountyDemographics] **of type list  # Output Given Input: 318,857,056 **of type int
    # If I was Computer: take the county list, create a new variable set at 0, iterate through the list, accessing the index 'population', extracting its key-value pair at
    # '2014 Population', and adding its associated value to the new variable I set before. Lastly, return the total sum at the end of the loop.
def population_total(list:list[CountyDemographics] ) -> int:
    sum_of_2014_population = 0   # create variable to store sum of '2014 Population' values as function iterates through the list.

    for idx in list:
            temp = idx.population['2014 Population']
            sum_of_2014_population += temp

    return sum_of_2014_population

# PART 2
# DESIGN RECIPE
    # Purpose of Function: takes two parameters (county demographics and state abbreivation) and returns a list of county demographics given the specified state.
    # Input: list[CountyDemographics] , CA   # Output Given Input: a list of all 58 counties
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the state abbreviation. I'd store every itereated index into a new list,
    # and return that new list.

def filter_by_state(list:list[CountyDemographics], state: str) -> list[CountyDemographics]:
    county_demographics_given_state = []

    for idx in list:
        if idx.state == state:
            county_demographics_given_state.append(idx)
    return (county_demographics_given_state)

# PART 3
# DESIGN RECIPE
    # Purpose of Function: takes two parameters (list of county demographic objects and education as the key) and returns the total 2014 population across the set of counties in the provided list
    # Input: list[CountyDemographics] , "Bachelor's Degree or Higher"   # Output Given Input: 87911.145 --> float
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the specified education level. I'd caluclate each population and percentage of education
    # given the county and sum it all together.

def population_by_education(list: list[CountyDemographics], education_level: str) -> float:
    population_by_education = 0.0
    total_2014_population = population_total(build_data.get_data())

    for idx in list:
        if education_level in idx.education:
            total_education_percent = idx.education[education_level]

        education_population = total_2014_population * (total_education_percent / 100)
        population_by_education += education_population

    return population_by_education

# DESIGN RECIPE
    # Purpose of Function: takes two parameters (list of county demographic objects and ethnicity as the key) and returns the total 2014 population across the set of counties in the provided list
    # Input: list[CountyDemographics] , "Black Alone"   # Output Given Input: float
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the specified ethnicity. I'd caluclate each population and percentage of key ethnicity
    # and given the county, sum it all together.


def population_by_ethnicity(list:list[CountyDemographics], ethnicity: str) -> float:







