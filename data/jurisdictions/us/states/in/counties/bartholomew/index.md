---
type: Jurisdiction
title: "Bartholomew County, IN"
classification: county
fips: "18005"
state: "IN"
demographics:
  population: 83536
  population_under_18: 20102
  population_18_64: 49481
  population_65_plus: 13953
  median_household_income: 79901
  poverty_rate: 10.47
  homeownership_rate: 69.32
  unemployment_rate: 4.12
  median_home_value: 232800
  gini_index: 0.4462
  vacancy_rate: 6.47
  race_white: 66196
  race_black: 1545
  race_asian: 6174
  race_native: 70
  hispanic: 7710
  bachelors_plus: 27388
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.7296
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.2704
  - to: "us/states/in/districts/senate/41"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/59"
    rel: in-district
    area_weight: 0.5407
  - to: "us/states/in/districts/house/73"
    rel: in-district
    area_weight: 0.4089
  - to: "us/states/in/districts/house/69"
    rel: in-district
    area_weight: 0.0503
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Bartholomew County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83536 |
| Under 18 | 20102 |
| 18–64 | 49481 |
| 65+ | 13953 |
| Median household income | 79901 |
| Poverty rate | 10.47 |
| Homeownership rate | 69.32 |
| Unemployment rate | 4.12 |
| Median home value | 232800 |
| Gini index | 0.4462 |
| Vacancy rate | 6.47 |
| White | 66196 |
| Black | 1545 |
| Asian | 6174 |
| Native | 70 |
| Hispanic/Latino | 7710 |
| Bachelor's or higher | 27388 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 73% (congressional)
- [IN-09](/us/states/in/districts/09.md) — 27% (congressional)
- [IN Senate District 41](/us/states/in/districts/senate/41.md) — 100% (state senate)
- [IN House District 59](/us/states/in/districts/house/59.md) — 54% (state house)
- [IN House District 73](/us/states/in/districts/house/73.md) — 41% (state house)
- [IN House District 69](/us/states/in/districts/house/69.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
