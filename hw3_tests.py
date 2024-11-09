import data
import build_data
import unittest

import hw3
from data import CountyDemographics

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass
    # Part 1
    # test population_total
    def test_population_total(self):
        # Create CountyDemographics objects with population data
        county1 = CountyDemographics(
            age={}, county="County1", education={}, ethnicities={}, income={},
            population={'2014': 100000}, state="State1"
        )
        county2 = CountyDemographics(
            age={}, county="County2", education={}, ethnicities={}, income={},
            population={'2014': 200000}, state="State2"
        )
        counties = [county1, county2]

        # Expected total population for 2014 is 100000 + 200000 = 300000
        self.assertEqual(hw3.population_total(counties), 300000)

    def test_population_total2(self):
        # Test with an empty list of counties
        counties = []

        # Expected total population should be 0
        self.assertEqual(hw3.population_total(counties), 0)
    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        # Assume we create a list of CountyDemographics objects, including some in CA and others in NY
        county1 = CountyDemographics(age={}, county="County1", education={}, ethnicities={}, income={}, population={},
                                     state="CA")
        county2 = CountyDemographics(age={}, county="County2", education={}, ethnicities={}, income={}, population={},
                                     state="CA")
        county3 = CountyDemographics(age={}, county="County3", education={}, ethnicities={}, income={}, population={},
                                     state="NY")
        counties = [county1, county2, county3]

        # Only the two CA counties should be returned
        result = hw3.filter_by_state(counties, "CA")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(county.state == "CA" for county in result))

    def test_filter_by_state2(self):
        # List with counties in NY and TX but no CA
        county1 = CountyDemographics(age={}, county="County1", education={}, ethnicities={}, income={}, population={},
                                     state="NY")
        county2 = CountyDemographics(age={}, county="County2", education={}, ethnicities={}, income={}, population={},
                                     state="TX")
        counties = [county1, county2]

        # Expect an empty list when filtering for CA
        result = hw3.filter_by_state(counties, "CA")
        self.assertEqual(result, [])
    # Part 3
    # test population_by_education
    # test population_by_ethnicity
    # test population_below_poverty_level
    def test_populations(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Two or More Races": 2.5}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )

        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 25.0},
            ethnicities={"Two or More Races": 3.0}, income={"Persons Below Poverty Level": 10.0},
            population={"2014 Population": 150000}, state="CA"
        )

        counties = [county1, county2]

    # Usage of functions
        self.assertEqual(hw3.population_by_education(counties, "Bachelor's Degree or Higher"), 87,911.145 + 37500)  # Expected: 87,911.145 + 37500
        self.assertEqual(hw3.population_by_ethnicity(counties, "Two or More Races"), 6977.075 + 4500)  # Expected: 6977.075 + 4500
        self.assertEqual(hw3.population_below_poverty_level(counties),0)

    # Part 4
    # test percent_by_education
    # test percent_by_ethnicity
    # test percent_below_poverty_level
    def test_percent(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Two or More Races": 2.5}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )

        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 25.0},
            ethnicities={"Two or More Races": 3.0}, income={"Persons Below Poverty Level": 10.0},
            population={"2014 Population": 150000}, state="CA"
        )

        counties = [county1, county2]

    # Example function calls
        self.assertEqual(hw3.percent_by_education(counties, "Bachelor's Degree or Higher"), 125411.145)  # Expected percentage of total pop.
        self.assertEqual(hw3.percent_by_ethnicity(counties, "Two or More Races"), 87)  # Expected percentage of total pop.
        self.assertEqual(hw3.percent_below_poverty_level(counties), 87)

    # Part 5
    # test education_greater_than
    # test education_less_than
    # test ethnicity_greater_than
    # test ethnicity_less_than
    # test below_poverty_level_greater_than
    # test below_poverty_level_less_than
    def test_less_or_greater_than(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Hispanic or Latino": 40.0}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )

        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 65.0},
            ethnicities={"Hispanic or Latino": 20.0}, income={"Persons Below Poverty Level": 5.0},
            population={"2014 Population": 150000}, state="CA"
        )

        counties = [county1, county2]

        # Example function calls
        self.assertEqual(hw3.education_greater_than(counties, "Bachelor's Degree or Higher", 60), [county2])  # Expected: [county2]
        self.assertEqual(hw3.ethnicity_greater_than(counties, "Hispanic or Latino", 30), [county1])  # Expected: [county1]
        self.assertEqual(hw3.below_poverty_level_greater_than(counties, 10), 29.227712354020085)

import data
import build_data
import unittest

import hw3
from data import CountyDemographics

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass
    # Part 1
    # test population_total
    def test_population_total(self):
        # Create CountyDemographics objects with population data
        county1 = CountyDemographics(
            age={}, county="County1", education={}, ethnicities={}, income={},
            population={'2014': 100000}, state="State1"
        )
        county2 = CountyDemographics(
            age={}, county="County2", education={}, ethnicities={}, income={},
            population={'2014': 200000}, state="State2"
        )
        counties = [county1, county2]

        # Expected total population for 2014 is 100000 + 200000 = 300000
        self.assertEqual(hw3.population_total(counties), 300000)

    def test_population_total2(self):
        # Test with an empty list of counties
        counties = []

        # Expected total population should be 0
        self.assertEqual(hw3.population_total(counties), 0)
    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        # Assume we create a list of CountyDemographics objects, including some in CA and others in NY
        county1 = CountyDemographics(age={}, county="County1", education={}, ethnicities={}, income={}, population={},
                                     state="CA")
        county2 = CountyDemographics(age={}, county="County2", education={}, ethnicities={}, income={}, population={},
                                     state="CA")
        county3 = CountyDemographics(age={}, county="County3", education={}, ethnicities={}, income={}, population={},
                                     state="NY")
        counties = [county1, county2, county3]

        # Only the two CA counties should be returned
        result = hw3.filter_by_state(counties, "CA")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(county.state == "CA" for county in result))

    def test_filter_by_state2(self):
        # List with counties in NY and TX but no CA
        county1 = CountyDemographics(age={}, county="County1", education={}, ethnicities={}, income={}, population={},
                                     state="NY")
        county2 = CountyDemographics(age={}, county="County2", education={}, ethnicities={}, income={}, population={},
                                     state="TX")
        counties = [county1, county2]

        # Expect an empty list when filtering for CA
        result = hw3.filter_by_state(counties, "CA")
        self.assertEqual(result, [])
    # Part 3
    # test population_by_education
    # test population_by_ethnicity
    # test population_below_poverty_level
    def test_populations(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Two or More Races": 2.5}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )
        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 25.0},
            ethnicities={"Two or More Races": 3.0}, income={"Persons Below Poverty Level": 10.0},
            population={"2014 Population": 150000}, state="CA"
        )
        counties = [county1, county2]

        # Calculate expected population by education, ethnicity, and poverty level
        expected_pop_edu = (0.315 * 279083) + (0.25 * 150000)
        expected_pop_ethnicity = (0.025 * 279083) + (0.03 * 150000)
        expected_pop_poverty = (0.12 * 279083) + (0.1 * 150000)

        # Assertions
        self.assertAlmostEqual(hw3.population_by_education(counties, "Bachelor's Degree or Higher"), expected_pop_edu, delta=1)
        self.assertAlmostEqual(hw3.population_by_ethnicity(counties, "Two or More Races"), expected_pop_ethnicity, delta=1)
        self.assertAlmostEqual(hw3.population_below_poverty_level(counties), expected_pop_poverty, delta=1)

    # Usage of functions
        self.assertEqual(hw3.population_by_education(counties, "Bachelor's Degree or Higher"), 87,911.145 + 37500)  # Expected: 87,911.145 + 37500
        self.assertEqual(hw3.population_by_ethnicity(counties, "Two or More Races"), 6977.075 + 4500)  # Expected: 6977.075 + 4500
        self.assertEqual(hw3.population_below_poverty_level(counties),0)

    # Part 4
    # test percent_by_education
    # test percent_by_ethnicity
    # test percent_below_poverty_level
    def test_percent(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Two or More Races": 2.5}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )
        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 25.0},
            ethnicities={"Two or More Races": 3.0}, income={"Persons Below Poverty Level": 10.0},
            population={"2014 Population": 150000}, state="CA"
        )
        counties = [county1, county2]

        # Calculate expected percentages by education, ethnicity, and poverty level
        total_population = 279083 + 150000
        expected_percent_edu = ((0.315 * 279083) + (0.25 * 150000)) / total_population * 100
        expected_percent_ethnicity = ((0.025 * 279083) + (0.03 * 150000)) / total_population * 100
        expected_percent_poverty = ((0.12 * 279083) + (0.1 * 150000)) / total_population * 100

        # Assertions
        self.assertAlmostEqual(hw3.percent_by_education(counties, "Bachelor's Degree or Higher"), expected_percent_edu, delta=0.01)
        self.assertAlmostEqual(hw3.percent_by_ethnicity(counties, "Two or More Races"), expected_percent_ethnicity, delta=0.01)
        self.assertAlmostEqual(hw3.percent_below_poverty_level(counties), expected_percent_poverty, delta=0.01)

    # Part 5
    # test education_greater_than
    # test education_less_than
    # test ethnicity_greater_than
    # test ethnicity_less_than
    # test below_poverty_level_greater_than
    # test below_poverty_level_less_than
    def test_less_or_greater_than(self):
        county1 = CountyDemographics(
            age={}, county="County1", education={"Bachelor's Degree or Higher": 31.5},
            ethnicities={"Hispanic or Latino": 40.0}, income={"Persons Below Poverty Level": 12.0},
            population={"2014 Population": 279083}, state="CA"
        )

        county2 = CountyDemographics(
            age={}, county="County2", education={"Bachelor's Degree or Higher": 65.0},
            ethnicities={"Hispanic or Latino": 20.0}, income={"Persons Below Poverty Level": 5.0},
            population={"2014 Population": 150000}, state="CA"
        )

        counties = [county1, county2]

        # Example function calls
        self.assertEqual(hw3.education_greater_than(counties, "Bachelor's Degree or Higher", 60), [county2])  # Expected: [county2]
        self.assertEqual(hw3.ethnicity_greater_than(counties, "Hispanic or Latino", 30), [county1])  # Expected: [county1]
        self.assertEqual(hw3.below_poverty_level_greater_than(counties, 10), 29.227712354020085)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
