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
    population_by_ethnicity = 0.0
    total_2014_population = population_total(build_data.get_data())

    for idx in list:
        if ethnicity in idx.ethnicities:
            total_ethnicity_percent = idx.ethnicities[ethnicity]

        education_population = total_2014_population * (total_ethnicity_percent / 100)
        population_by_ethnicity += education_population

    return population_by_ethnicity

# DESIGN RECIPE
    # Purpose of Function: takes one parameter (list of county demographics objects) and returns the total 2014 population for those below the poverty level across all the counties provided in the list.
    # Input: list[CountyDemographics]  # Output Given Input: float
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the specified income level. I'll calculate it by finding the
    # 2014 population and finding the income percentages given the county, and then sum it all up.

def population_below_poverty_level(list: list[CountyDemographics]) -> float:
    total_population_under_poverty = 0.0

    for idx in list:
        if 'Persons Below Poverty Level' in idx.income:
            total_poverty_percentage = idx.income['Persons Below Poverty Level']

        if '2014 Population' in idx.population:
            total_2014_population = idx.population['2014 Population']

        below_poverty_population = total_2014_population * (total_poverty_percentage / 100)
        total_population_under_poverty += below_poverty_population

    return total_population_under_poverty

#PART 4
# DESIGN RECIPE
    # Purpose of Function: takes two parameters (list of county demographics objects and education as the key), returning the percentage of an education group across the 2014 population.
    # Input: list[CountyDemographics], 'Bachelor's Degree or Higher'  # Output Given Input: float
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the specified education level. I'll calculate it by finding the
    # 2014 population and finding the income percentages given the county, and then sum it all up (convert to percents by times 100).

def percent_by_education(list: list[CountyDemographics], education_level: str) -> float:
    education_population = 0.0
    total_2014_population = 0

    for idx in list:
        if education_level in idx.education:
            county_education_percentage = idx.education[education_level]

        if '2014 Population' in idx.population:
            temp = idx.population['2014 Population']

            total_2014_population += temp
            education_population += temp * (county_education_percentage / 100)

    if total_2014_population == 0:
        return 0

    return  (education_population / total_2014_population) * 100

# DESIGN RECIPE
    # Purpose of Function: takes two parameters (list of county demographics objects and ethnicity as the key), returning the percentage of an ethnic group across the 2014 population.
    # Input: list[CountyDemographics], 'Black Alone'  # Output Given Input: float
    # If I was a Computer: take the county demographics list, iterate it given the specific that the key equals the specified ethnicity. I'll calculate it by finding the
    # 2014 population and finding the ethnic percentages given the county, and then sum it all up (convert to percents by times 100).

def percent_by_ethnicity(list: list[CountyDemographics], ethnicity:str) -> float:
    ethnic_population = 0.0
    total_2014_population = 0.0

    for idx in list:
        if ethnicity in idx.ethnicities:
            county_ethnic_percentage = idx.ethnicities[ethnicity]

            if '2014 Population' in idx.population:
                temp = idx.population['2014 Population']

                total_2014_population += temp
                ethnic_population += temp * (county_ethnic_percentage / 100)

    if total_2014_population == 0:
        return 0

    return (ethnic_population / total_2014_population) * 100

# DESIGN RECIPE
    # Purpose of Function: takes a parameter (list of county demographics objects) returning the percentage of those below the poverty level across the 2014 population.
    # Input: list[CountyDemographics]  # Output Given Input: float

def percent_below_poverty_level(list:list[CountyDemographics]) -> float:
    total_population_under_poverty = 0.0
    total_2014_population = 0.0

    for idx in list:
        if 'Persons Below Poverty Level' in idx.income:
            county_poverty_percentage = idx.income['Persons Below Poverty Level']

        if '2014 Population' in idx.population:
            temp = idx.population['2014 Population']

            total_2014_population += temp
            total_population_under_poverty += temp * (county_poverty_percentage / 100)

    if total_2014_population == 0:
        return 0

    return (total_population_under_poverty / total_2014_population) * 100

# PART 5
# DESIGN RECIPE
    # Purpose of Function: takes three parameters (list of objects, education as a key, and a numeric threshold value) and returns a list of all county demographic objects for that specific key and threshold value.
    # Input: list[CountyDemographics], 'Bachelor's Degree or Higher' , 30  # Output Given Input: float
    # If I was a computer: loop through the list, find valid education key-pairs, compare if education percentage is greater or less than and add that to a list.

def education_greater_than(all_data:list[CountyDemographics], educational_level: str, threshold: int) -> list:
    above_education_threshold_list = []

    for idx in all_data:
        if educational_level in idx.education:
            county_education_percent = idx.education[educational_level]

            if county_education_percent > threshold:
                above_education_threshold_list.append(idx.county)

    return above_education_threshold_list

def education_less_than(all_data:list[CountyDemographics], educational_level: str, threshold: int) -> list:
    below_education_threshold_list = []

    for idx in all_data:
        if educational_level in idx.education:
            county_education_percent = idx.education[educational_level]

            if county_education_percent < threshold:
                below_education_threshold_list.append(idx.county)

    return below_education_threshold_list

# DESIGN RECIPE
    # Purpose of Function: takes three parameters (list of objects, ethnicity as a key, and a numeric threshold value) and returns a list of all county demographic objects for that specific key and threshold value.
    # Input: list[CountyDemographics], 'Hispanic or Latino' , 30  # Output Given Input: float

def ethnicity_greater_than(all_data:list[CountyDemographics], ethnicity: str, threshold: int) -> list:
    above_ethnic_threshold_list = []

    for idx in all_data:
        if ethnicity in idx.ethnicities:
            county_ethnic_percent = idx.ethnicities[ethnicity]

            if county_ethnic_percent > threshold:
                above_ethnic_threshold_list.append(idx.county)

    return above_ethnic_threshold_list

def ethn