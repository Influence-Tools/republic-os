---
type: Jurisdiction
title: "Charlotte County, VA"
classification: county
fips: "51037"
state: "VA"
demographics:
  population: 11422
  population_under_18: 2454
  population_18_64: 6372
  population_65_plus: 2596
  median_household_income: 58000
  poverty_rate: 18.94
  homeownership_rate: 74.72
  unemployment_rate: 2.39
  median_home_value: 144100
  gini_index: 0.4761
  vacancy_rate: 21.25
  race_white: 7812
  race_black: 2847
  race_asian: 22
  race_native: 0
  hispanic: 295
  bachelors_plus: 2343
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/50"
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

# Charlotte County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11422 |
| Under 18 | 2454 |
| 18–64 | 6372 |
| 65+ | 2596 |
| Median household income | 58000 |
| Poverty rate | 18.94 |
| Homeownership rate | 74.72 |
| Unemployment rate | 2.39 |
| Median home value | 144100 |
| Gini index | 0.4761 |
| Vacancy rate | 21.25 |
| White | 7812 |
| Black | 2847 |
| Asian | 22 |
| Native | 0 |
| Hispanic/Latino | 295 |
| Bachelor's or higher | 2343 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 9](/us/states/va/districts/senate/9.md) — 100% (state senate)
- [VA House District 50](/us/states/va/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
