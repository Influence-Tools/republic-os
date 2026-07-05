---
type: Jurisdiction
title: "Lee County, IA"
classification: county
fips: "19111"
state: "IA"
demographics:
  population: 32893
  population_under_18: 6989
  population_18_64: 18595
  population_65_plus: 7309
  median_household_income: 62382
  poverty_rate: 13.09
  homeownership_rate: 76.34
  unemployment_rate: 4.45
  median_home_value: 141400
  gini_index: 0.4465
  vacancy_rate: 9.31
  race_white: 29953
  race_black: 815
  race_asian: 185
  race_native: 35
  hispanic: 1145
  bachelors_plus: 6670
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ia/districts/senate/50"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ia/districts/house/100"
    rel: in-district
    area_weight: 0.8245
  - to: "us/states/ia/districts/house/99"
    rel: in-district
    area_weight: 0.175
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Lee County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32893 |
| Under 18 | 6989 |
| 18–64 | 18595 |
| 65+ | 7309 |
| Median household income | 62382 |
| Poverty rate | 13.09 |
| Homeownership rate | 76.34 |
| Unemployment rate | 4.45 |
| Median home value | 141400 |
| Gini index | 0.4465 |
| Vacancy rate | 9.31 |
| White | 29953 |
| Black | 815 |
| Asian | 185 |
| Native | 35 |
| Hispanic/Latino | 1145 |
| Bachelor's or higher | 6670 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 50](/us/states/ia/districts/senate/50.md) — 100% (state senate)
- [IA House District 100](/us/states/ia/districts/house/100.md) — 82% (state house)
- [IA House District 99](/us/states/ia/districts/house/99.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
