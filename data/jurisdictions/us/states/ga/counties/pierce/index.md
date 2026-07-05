---
type: Jurisdiction
title: "Pierce County, GA"
classification: county
fips: "13229"
state: "GA"
demographics:
  population: 20202
  population_under_18: 4982
  population_18_64: 11765
  population_65_plus: 3455
  median_household_income: 60517
  poverty_rate: 13.83
  homeownership_rate: 76.46
  unemployment_rate: 2.58
  median_home_value: 153300
  gini_index: 0.4743
  vacancy_rate: 10.98
  race_white: 17037
  race_black: 2002
  race_asian: 0
  race_native: 59
  hispanic: 1070
  bachelors_plus: 4291
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/house/178"
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

# Pierce County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20202 |
| Under 18 | 4982 |
| 18–64 | 11765 |
| 65+ | 3455 |
| Median household income | 60517 |
| Poverty rate | 13.83 |
| Homeownership rate | 76.46 |
| Unemployment rate | 2.58 |
| Median home value | 153300 |
| Gini index | 0.4743 |
| Vacancy rate | 10.98 |
| White | 17037 |
| Black | 2002 |
| Asian | 0 |
| Native | 59 |
| Hispanic/Latino | 1070 |
| Bachelor's or higher | 4291 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 178](/us/states/ga/districts/house/178.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
