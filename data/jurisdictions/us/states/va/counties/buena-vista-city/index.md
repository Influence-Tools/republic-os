---
type: Jurisdiction
title: "Buena Vista city, VA"
classification: county
fips: "51530"
state: "VA"
demographics:
  population: 6593
  population_under_18: 1971
  population_18_64: 1990
  population_65_plus: 2632
  median_household_income: 57833
  poverty_rate: 18.84
  homeownership_rate: 56.5
  unemployment_rate: 1.43
  median_home_value: 156200
  gini_index: 0.3978
  vacancy_rate: 13.39
  race_white: 5583
  race_black: 134
  race_asian: 68
  race_native: 83
  hispanic: 15
  bachelors_plus: 1339
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Buena Vista city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6593 |
| Under 18 | 1971 |
| 18–64 | 1990 |
| 65+ | 2632 |
| Median household income | 57833 |
| Poverty rate | 18.84 |
| Homeownership rate | 56.5 |
| Unemployment rate | 1.43 |
| Median home value | 156200 |
| Gini index | 0.3978 |
| Vacancy rate | 13.39 |
| White | 5583 |
| Black | 134 |
| Asian | 68 |
| Native | 83 |
| Hispanic/Latino | 15 |
| Bachelor's or higher | 1339 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
