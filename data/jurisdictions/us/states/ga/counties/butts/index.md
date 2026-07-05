---
type: Jurisdiction
title: "Butts County, GA"
classification: county
fips: "13035"
state: "GA"
demographics:
  population: 26496
  population_under_18: 5450
  population_18_64: 16869
  population_65_plus: 4177
  median_household_income: 69241
  poverty_rate: 10.41
  homeownership_rate: 74.29
  unemployment_rate: 3.24
  median_home_value: 240600
  gini_index: 0.3894
  vacancy_rate: 8.04
  race_white: 17046
  race_black: 6497
  race_asian: 68
  race_native: 125
  hispanic: 1022
  bachelors_plus: 3828
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ga/districts/senate/25"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/house/118"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Butts County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26496 |
| Under 18 | 5450 |
| 18–64 | 16869 |
| 65+ | 4177 |
| Median household income | 69241 |
| Poverty rate | 10.41 |
| Homeownership rate | 74.29 |
| Unemployment rate | 3.24 |
| Median home value | 240600 |
| Gini index | 0.3894 |
| Vacancy rate | 8.04 |
| White | 17046 |
| Black | 6497 |
| Asian | 68 |
| Native | 125 |
| Hispanic/Latino | 1022 |
| Bachelor's or higher | 3828 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 25](/us/states/ga/districts/senate/25.md) — 100% (state senate)
- [GA House District 118](/us/states/ga/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
