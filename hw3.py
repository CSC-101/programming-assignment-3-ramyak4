import data
import county_demographics
import build_data

from data import CountyDemographics

# Part 1
# This function calculates the total population for 2014 across a list of counties.
# Input: list of CountyDemographics objects (info)
# Output: integer representing the total 2014 population across the counties
def population_total(info: list[CountyDemographics]) -> int:
    total_pop = 0
    for county in info:
        # Adds the 2014 population, defaulting to 0 if the key does not exist
        total_pop += county.population.get('2014 Population', 0)
    return total_pop

# Part 2
# This function filters the list of counties to include only those in a specified state.
# Input: list of CountyDemographics objects (info), state abbreviation (abbr)
# Output: list of CountyDemographics objects that match the specified state
def filter_by_state(info: list[CountyDemographics], abbr: str) -> list[CountyDemographics]:
    if len(abbr) == 2:  # Ensures the state abbreviation is 2 characters long
        return [county for county in info if county.state == abbr]
    return []  # Returns an empty list if the abbreviation length is invalid

# Part 3
# This function calculates the total population with a specified education level across counties.
# Input: list of CountyDemographics objects (county_list), education key (education_key)
# Output: float representing the total population with the specified education level
def population_by_education(county_list: list[CountyDemographics], education_key: str) -> float:
    total_pop = 0.0
    for county in county_list:
        # Checks if the education key exists, calculates the sub-population percentage
        if education_key in county.education:
            total_pop += county.population["2014 Population"] * (county.education[education_key] / 100)
    return total_pop

# This function calculates the total population for a specified ethnicity across counties.
# Input: list of CountyDemographics objects (county_list), ethnicity key (ethnicity_key)
# Output: float representing the total population for the specified ethnicity
def population_by_ethnicity(county_list: list[CountyDemographics], ethnicity_key: str) -> float:
    total_pop = 0.0
    for county in county_list:
        # Checks if the ethnicity key exists, calculates the sub-population percentage
        if ethnicity_key in county.ethnicities:
            total_pop += county.population["2014 Population"] * (county.ethnicities[ethnicity_key] / 100)
    return total_pop

# This function calculates the total population below the poverty level across counties.
# Input: list of CountyDemographics objects (county_list)
# Output: float representing the total population below the poverty level
def population_below_poverty_level(county_list: list[CountyDemographics]) -> float:
    total_pop = 0.0
    for county in county_list:
        # Checks if "Persons Below Poverty Level" key exists, calculates the sub-population percentage
        if "Persons Below Poverty Level" in county.income:
            total_pop += county.population["2014 Population"] * (county.income["Persons Below Poverty Level"] / 100)
    return total_pop

# Part 4
# This function calculates the percentage of a population with a specified education level across counties.
# Input: list of CountyDemographics objects (county_list), education key (education_key)
# Output: float representing the percentage of the total population with the specified education level
def percent_by_education(county_list: list[CountyDemographics], education_key: str) -> float:
    total_population = sum(county.population["2014 Population"] for county in county_list)
    if total_population == 0:
        return 0.0  # Prevents division by zero if there is no population
    education_population = population_by_education(county_list, education_key)
    return (education_population / total_population) * 100

# This function calculates the percentage of a specified ethnicity across counties.
# Input: list of CountyDemographics objects (county_list), ethnicity key (ethnicity_key)
# Output: float representing the percentage of the total population for the specified ethnicity
def percent_by_ethnicity(county_list: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = sum(county.population["2014 Population"] for county in county_list)
    if total_population == 0:
        return 0.0  # Prevents division by zero if there is no population
    ethnicity_population = population_by_ethnicity(county_list, ethnicity_key)
    return (ethnicity_population / total_population) * 100

# This function calculates the percentage of the population below the poverty level across counties.
# Input: list of CountyDemographics objects (county_list)
# Output: float representing the percentage of the total population below the poverty level
def percent_below_poverty_level(county_list: list[CountyDemographics]) -> float:
    total_population = sum(county.population["2014 Population"] for county in county_list)
    if total_population == 0:
        return 0.0  # Prevents division by zero if there is no population
    poverty_population = population_below_poverty_level(county_list)
    return (poverty_population / total_population) * 100

# Part 5
# The following functions filter counties based on whether an education/ethnicity/poverty level is above or below a threshold.

# Returns counties where the specified education level percentage is greater than the threshold.
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) > threshold]

# Returns counties where the specified education level percentage is less than the threshold.
def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(education_key, 0) < threshold]

# Returns counties where the specified ethnicity percentage is greater than the threshold.
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]

# Returns counties where the specified ethnicity percentage is less than the threshold.
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]

# Returns counties where the population below poverty level percentage is greater than the threshold.
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) > threshold]

# Returns counties where the population below poverty level percentage is less than the threshold.
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) < threshold]