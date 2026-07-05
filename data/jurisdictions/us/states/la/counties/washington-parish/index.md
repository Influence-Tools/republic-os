---
type: Jurisdiction
title: "Washington Parish, LA"
classification: county
fips: "22117"
state: "LA"
demographics:
  population: 45120
  population_under_18: 10711
  population_18_64: 25723
  population_65_plus: 8686
  median_household_income: 45380
  poverty_rate: 24.32
  homeownership_rate: 69.3
  unemployment_rate: 9.89
  median_home_value: 155700
  gini_index: 0.4903
  vacancy_rate: 17.37
  race_white: 28473
  race_black: 12151
  race_asian: 37
  race_native: 224
  hispanic: 1508
  bachelors_plus: 5156
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/la/districts/senate/12"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/la/districts/house/75"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Washington Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45120 |
| Under 18 | 10711 |
| 18–64 | 25723 |
| 65+ | 8686 |
| Median household income | 45380 |
| Poverty rate | 24.32 |
| Homeownership rate | 69.3 |
| Unemployment rate | 9.89 |
| Median home value | 155700 |
| Gini index | 0.4903 |
| Vacancy rate | 17.37 |
| White | 28473 |
| Black | 12151 |
| Asian | 37 |
| Native | 224 |
| Hispanic/Latino | 1508 |
| Bachelor's or higher | 5156 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 12](/us/states/la/districts/senate/12.md) — 100% (state senate)
- [LA House District 75](/us/states/la/districts/house/75.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
