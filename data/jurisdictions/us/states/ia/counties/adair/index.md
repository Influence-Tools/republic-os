---
type: Jurisdiction
title: "Adair County, IA"
classification: county
fips: "19001"
state: "IA"
demographics:
  population: 7460
  population_under_18: 1706
  population_18_64: 4070
  population_65_plus: 1684
  median_household_income: 68092
  poverty_rate: 9.53
  homeownership_rate: 73.95
  unemployment_rate: 3.96
  median_home_value: 160400
  gini_index: 0.4601
  vacancy_rate: 9.3
  race_white: 7041
  race_black: 115
  race_asian: 23
  race_native: 13
  hispanic: 235
  bachelors_plus: 1315
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Adair County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7460 |
| Under 18 | 1706 |
| 18–64 | 4070 |
| 65+ | 1684 |
| Median household income | 68092 |
| Poverty rate | 9.53 |
| Homeownership rate | 73.95 |
| Unemployment rate | 3.96 |
| Median home value | 160400 |
| Gini index | 0.4601 |
| Vacancy rate | 9.3 |
| White | 7041 |
| Black | 115 |
| Asian | 23 |
| Native | 13 |
| Hispanic/Latino | 235 |
| Bachelor's or higher | 1315 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 23](/us/states/ia/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
