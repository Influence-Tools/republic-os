---
type: Jurisdiction
title: "Rabun County, GA"
classification: county
fips: "13241"
state: "GA"
demographics:
  population: 17312
  population_under_18: 2812
  population_18_64: 9508
  population_65_plus: 4992
  median_household_income: 67493
  poverty_rate: 13.13
  homeownership_rate: 77.12
  unemployment_rate: 1.33
  median_home_value: 295200
  gini_index: 0.5051
  vacancy_rate: 37.9
  race_white: 15091
  race_black: 145
  race_asian: 152
  race_native: 47
  hispanic: 1525
  bachelors_plus: 6084
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/10"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Rabun County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17312 |
| Under 18 | 2812 |
| 18–64 | 9508 |
| 65+ | 4992 |
| Median household income | 67493 |
| Poverty rate | 13.13 |
| Homeownership rate | 77.12 |
| Unemployment rate | 1.33 |
| Median home value | 295200 |
| Gini index | 0.5051 |
| Vacancy rate | 37.9 |
| White | 15091 |
| Black | 145 |
| Asian | 152 |
| Native | 47 |
| Hispanic/Latino | 1525 |
| Bachelor's or higher | 6084 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 10](/us/states/ga/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
