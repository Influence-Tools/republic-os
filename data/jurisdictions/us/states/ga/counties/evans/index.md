---
type: Jurisdiction
title: "Evans County, GA"
classification: county
fips: "13109"
state: "GA"
demographics:
  population: 10757
  population_under_18: 2704
  population_18_64: 6216
  population_65_plus: 1837
  median_household_income: 53259
  poverty_rate: 19.15
  homeownership_rate: 65.39
  unemployment_rate: 4.29
  median_home_value: 138200
  gini_index: 0.4336
  vacancy_rate: 13.26
  race_white: 5948
  race_black: 3033
  race_asian: 109
  race_native: 20
  hispanic: 1327
  bachelors_plus: 1392
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/ga/districts/senate/4"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/157"
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

# Evans County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10757 |
| Under 18 | 2704 |
| 18–64 | 6216 |
| 65+ | 1837 |
| Median household income | 53259 |
| Poverty rate | 19.15 |
| Homeownership rate | 65.39 |
| Unemployment rate | 4.29 |
| Median home value | 138200 |
| Gini index | 0.4336 |
| Vacancy rate | 13.26 |
| White | 5948 |
| Black | 3033 |
| Asian | 109 |
| Native | 20 |
| Hispanic/Latino | 1327 |
| Bachelor's or higher | 1392 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 4](/us/states/ga/districts/senate/4.md) — 100% (state senate)
- [GA House District 157](/us/states/ga/districts/house/157.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
