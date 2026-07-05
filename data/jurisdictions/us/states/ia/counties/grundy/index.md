---
type: Jurisdiction
title: "Grundy County, IA"
classification: county
fips: "19075"
state: "IA"
demographics:
  population: 12384
  population_under_18: 2905
  population_18_64: 6879
  population_65_plus: 2600
  median_household_income: 87205
  poverty_rate: 6.52
  homeownership_rate: 84.48
  unemployment_rate: 1.96
  median_home_value: 198800
  gini_index: 0.3944
  vacancy_rate: 6.93
  race_white: 11777
  race_black: 71
  race_asian: 59
  race_native: 58
  hispanic: 219
  bachelors_plus: 3049
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/54"
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

# Grundy County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12384 |
| Under 18 | 2905 |
| 18–64 | 6879 |
| 65+ | 2600 |
| Median household income | 87205 |
| Poverty rate | 6.52 |
| Homeownership rate | 84.48 |
| Unemployment rate | 1.96 |
| Median home value | 198800 |
| Gini index | 0.3944 |
| Vacancy rate | 6.93 |
| White | 11777 |
| Black | 71 |
| Asian | 59 |
| Native | 58 |
| Hispanic/Latino | 219 |
| Bachelor's or higher | 3049 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 27](/us/states/ia/districts/senate/27.md) — 100% (state senate)
- [IA House District 54](/us/states/ia/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
