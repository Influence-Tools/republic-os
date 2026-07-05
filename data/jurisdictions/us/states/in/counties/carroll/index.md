---
type: Jurisdiction
title: "Carroll County, IN"
classification: county
fips: "18015"
state: "IN"
demographics:
  population: 20535
  population_under_18: 4470
  population_18_64: 11810
  population_65_plus: 4255
  median_household_income: 65645
  poverty_rate: 8.75
  homeownership_rate: 82.19
  unemployment_rate: 3.07
  median_home_value: 180900
  gini_index: 0.4155
  vacancy_rate: 15.42
  race_white: 19302
  race_black: 53
  race_asian: 34
  race_native: 96
  hispanic: 942
  bachelors_plus: 3334
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/22"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/house/38"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Carroll County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20535 |
| Under 18 | 4470 |
| 18–64 | 11810 |
| 65+ | 4255 |
| Median household income | 65645 |
| Poverty rate | 8.75 |
| Homeownership rate | 82.19 |
| Unemployment rate | 3.07 |
| Median home value | 180900 |
| Gini index | 0.4155 |
| Vacancy rate | 15.42 |
| White | 19302 |
| Black | 53 |
| Asian | 34 |
| Native | 96 |
| Hispanic/Latino | 942 |
| Bachelor's or higher | 3334 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 22](/us/states/in/districts/senate/22.md) — 100% (state senate)
- [IN House District 38](/us/states/in/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
