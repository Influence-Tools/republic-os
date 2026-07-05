---
type: Jurisdiction
title: "Nelson County, ND"
classification: county
fips: "38063"
state: "ND"
demographics:
  population: 3016
  population_under_18: 625
  population_18_64: 1538
  population_65_plus: 853
  median_household_income: 67193
  poverty_rate: 7.16
  homeownership_rate: 75.11
  unemployment_rate: 1.11
  median_home_value: 139700
  gini_index: 0.4965
  vacancy_rate: 24.96
  race_white: 2795
  race_black: 14
  race_asian: 22
  race_native: 29
  hispanic: 89
  bachelors_plus: 813
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/29"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/nd/districts/house/29"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Nelson County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3016 |
| Under 18 | 625 |
| 18–64 | 1538 |
| 65+ | 853 |
| Median household income | 67193 |
| Poverty rate | 7.16 |
| Homeownership rate | 75.11 |
| Unemployment rate | 1.11 |
| Median home value | 139700 |
| Gini index | 0.4965 |
| Vacancy rate | 24.96 |
| White | 2795 |
| Black | 14 |
| Asian | 22 |
| Native | 29 |
| Hispanic/Latino | 89 |
| Bachelor's or higher | 813 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 29](/us/states/nd/districts/senate/29.md) — 100% (state senate)
- [ND House District 29](/us/states/nd/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
