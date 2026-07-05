---
type: Jurisdiction
title: "Radford city, VA"
classification: county
fips: "51750"
state: "VA"
demographics:
  population: 16726
  population_under_18: 4918
  population_18_64: 7484
  population_65_plus: 4324
  median_household_income: 57348
  poverty_rate: 28.66
  homeownership_rate: 42.29
  unemployment_rate: 8.1
  median_home_value: 220700
  gini_index: 0.5053
  vacancy_rate: 14.23
  race_white: 13781
  race_black: 1568
  race_asian: 406
  race_native: 8
  hispanic: 731
  bachelors_plus: 4240
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/42"
    rel: in-district
    area_weight: 0.997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Radford city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16726 |
| Under 18 | 4918 |
| 18–64 | 7484 |
| 65+ | 4324 |
| Median household income | 57348 |
| Poverty rate | 28.66 |
| Homeownership rate | 42.29 |
| Unemployment rate | 8.1 |
| Median home value | 220700 |
| Gini index | 0.5053 |
| Vacancy rate | 14.23 |
| White | 13781 |
| Black | 1568 |
| Asian | 406 |
| Native | 8 |
| Hispanic/Latino | 731 |
| Bachelor's or higher | 4240 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 100% (state senate)
- [VA House District 42](/us/states/va/districts/house/42.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
