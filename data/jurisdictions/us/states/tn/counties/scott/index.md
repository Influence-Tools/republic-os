---
type: Jurisdiction
title: "Scott County, TN"
classification: county
fips: "47151"
state: "TN"
demographics:
  population: 22113
  population_under_18: 5187
  population_18_64: 13105
  population_65_plus: 3821
  median_household_income: 44711
  poverty_rate: 23.07
  homeownership_rate: 71.56
  unemployment_rate: 7.45
  median_home_value: 124900
  gini_index: 0.4607
  vacancy_rate: 11.32
  race_white: 21351
  race_black: 54
  race_asian: 75
  race_native: 42
  hispanic: 47
  bachelors_plus: 2851
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.59
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.4087
  - to: "us/states/tn/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/38"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Scott County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22113 |
| Under 18 | 5187 |
| 18–64 | 13105 |
| 65+ | 3821 |
| Median household income | 44711 |
| Poverty rate | 23.07 |
| Homeownership rate | 71.56 |
| Unemployment rate | 7.45 |
| Median home value | 124900 |
| Gini index | 0.4607 |
| Vacancy rate | 11.32 |
| White | 21351 |
| Black | 54 |
| Asian | 75 |
| Native | 42 |
| Hispanic/Latino | 47 |
| Bachelor's or higher | 2851 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 59% (congressional)
- [TN-03](/us/states/tn/districts/03.md) — 41% (congressional)
- [TN Senate District 12](/us/states/tn/districts/senate/12.md) — 100% (state senate)
- [TN House District 38](/us/states/tn/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
