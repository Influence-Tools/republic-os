---
type: Jurisdiction
title: "Morgan County, GA"
classification: county
fips: "13211"
state: "GA"
demographics:
  population: 21078
  population_under_18: 4661
  population_18_64: 12095
  population_65_plus: 4322
  median_household_income: 78111
  poverty_rate: 8.83
  homeownership_rate: 78.23
  unemployment_rate: 2.45
  median_home_value: 342300
  gini_index: 0.4654
  vacancy_rate: 9.04
  race_white: 15498
  race_black: 4326
  race_asian: 155
  race_native: 0
  hispanic: 797
  bachelors_plus: 6174
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/42"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/114"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Morgan County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21078 |
| Under 18 | 4661 |
| 18–64 | 12095 |
| 65+ | 4322 |
| Median household income | 78111 |
| Poverty rate | 8.83 |
| Homeownership rate | 78.23 |
| Unemployment rate | 2.45 |
| Median home value | 342300 |
| Gini index | 0.4654 |
| Vacancy rate | 9.04 |
| White | 15498 |
| Black | 4326 |
| Asian | 155 |
| Native | 0 |
| Hispanic/Latino | 797 |
| Bachelor's or higher | 6174 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 42](/us/states/ga/districts/senate/42.md) — 100% (state senate)
- [GA House District 114](/us/states/ga/districts/house/114.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
