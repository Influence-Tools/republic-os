---
type: Jurisdiction
title: "Kossuth County, IA"
classification: county
fips: "19109"
state: "IA"
demographics:
  population: 14516
  population_under_18: 3198
  population_18_64: 7632
  population_65_plus: 3686
  median_household_income: 67697
  poverty_rate: 8.23
  homeownership_rate: 78.62
  unemployment_rate: 1.92
  median_home_value: 148300
  gini_index: 0.4179
  vacancy_rate: 9.19
  race_white: 13429
  race_black: 104
  race_asian: 60
  race_native: 19
  hispanic: 654
  bachelors_plus: 2966
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/9"
    rel: in-district
    area_weight: 0.7483
  - to: "us/states/ia/districts/house/10"
    rel: in-district
    area_weight: 0.2517
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Kossuth County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14516 |
| Under 18 | 3198 |
| 18–64 | 7632 |
| 65+ | 3686 |
| Median household income | 67697 |
| Poverty rate | 8.23 |
| Homeownership rate | 78.62 |
| Unemployment rate | 1.92 |
| Median home value | 148300 |
| Gini index | 0.4179 |
| Vacancy rate | 9.19 |
| White | 13429 |
| Black | 104 |
| Asian | 60 |
| Native | 19 |
| Hispanic/Latino | 654 |
| Bachelor's or higher | 2966 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 5](/us/states/ia/districts/senate/5.md) — 100% (state senate)
- [IA House District 9](/us/states/ia/districts/house/9.md) — 75% (state house)
- [IA House District 10](/us/states/ia/districts/house/10.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
