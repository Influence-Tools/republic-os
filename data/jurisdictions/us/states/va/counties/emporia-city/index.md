---
type: Jurisdiction
title: "Emporia city, VA"
classification: county
fips: "51595"
state: "VA"
demographics:
  population: 5547
  population_under_18: 1660
  population_18_64: 1665
  population_65_plus: 2222
  median_household_income: 51899
  poverty_rate: 15.81
  homeownership_rate: 38.11
  unemployment_rate: 2.95
  median_home_value: 148500
  gini_index: 0.4385
  vacancy_rate: 20.87
  race_white: 1087
  race_black: 3569
  race_asian: 32
  race_native: 0
  hispanic: 436
  bachelors_plus: 797
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/83"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Emporia city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5547 |
| Under 18 | 1660 |
| 18–64 | 1665 |
| 65+ | 2222 |
| Median household income | 51899 |
| Poverty rate | 15.81 |
| Homeownership rate | 38.11 |
| Unemployment rate | 2.95 |
| Median home value | 148500 |
| Gini index | 0.4385 |
| Vacancy rate | 20.87 |
| White | 1087 |
| Black | 3569 |
| Asian | 32 |
| Native | 0 |
| Hispanic/Latino | 436 |
| Bachelor's or higher | 797 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 100% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
