---
type: Jurisdiction
title: "Fountain County, IN"
classification: county
fips: "18045"
state: "IN"
demographics:
  population: 16617
  population_under_18: 3690
  population_18_64: 9644
  population_65_plus: 3283
  median_household_income: 62542
  poverty_rate: 12.37
  homeownership_rate: 74.64
  unemployment_rate: 4.74
  median_home_value: 143400
  gini_index: 0.4144
  vacancy_rate: 11.86
  race_white: 15522
  race_black: 112
  race_asian: 36
  race_native: 9
  hispanic: 501
  bachelors_plus: 2390
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.5489
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.4511
  - to: "us/states/in/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.815
  - to: "us/states/in/districts/house/42"
    rel: in-district
    area_weight: 0.185
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Fountain County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16617 |
| Under 18 | 3690 |
| 18–64 | 9644 |
| 65+ | 3283 |
| Median household income | 62542 |
| Poverty rate | 12.37 |
| Homeownership rate | 74.64 |
| Unemployment rate | 4.74 |
| Median home value | 143400 |
| Gini index | 0.4144 |
| Vacancy rate | 11.86 |
| White | 15522 |
| Black | 112 |
| Asian | 36 |
| Native | 9 |
| Hispanic/Latino | 501 |
| Bachelor's or higher | 2390 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 55% (congressional)
- [IN-04](/us/states/in/districts/04.md) — 45% (congressional)
- [IN Senate District 23](/us/states/in/districts/senate/23.md) — 100% (state senate)
- [IN House District 13](/us/states/in/districts/house/13.md) — 82% (state house)
- [IN House District 42](/us/states/in/districts/house/42.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
