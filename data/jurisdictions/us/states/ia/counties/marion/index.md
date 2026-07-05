---
type: Jurisdiction
title: "Marion County, IA"
classification: county
fips: "19125"
state: "IA"
demographics:
  population: 33642
  population_under_18: 7769
  population_18_64: 19358
  population_65_plus: 6515
  median_household_income: 78680
  poverty_rate: 8.17
  homeownership_rate: 77.7
  unemployment_rate: 2.18
  median_home_value: 233000
  gini_index: 0.4335
  vacancy_rate: 7.44
  race_white: 31760
  race_black: 141
  race_asian: 473
  race_native: 12
  hispanic: 773
  bachelors_plus: 9378
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/19"
    rel: in-district
    area_weight: 0.7006
  - to: "us/states/ia/districts/senate/11"
    rel: in-district
    area_weight: 0.2993
  - to: "us/states/ia/districts/house/37"
    rel: in-district
    area_weight: 0.7006
  - to: "us/states/ia/districts/house/21"
    rel: in-district
    area_weight: 0.2993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Marion County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33642 |
| Under 18 | 7769 |
| 18–64 | 19358 |
| 65+ | 6515 |
| Median household income | 78680 |
| Poverty rate | 8.17 |
| Homeownership rate | 77.7 |
| Unemployment rate | 2.18 |
| Median home value | 233000 |
| Gini index | 0.4335 |
| Vacancy rate | 7.44 |
| White | 31760 |
| Black | 141 |
| Asian | 473 |
| Native | 12 |
| Hispanic/Latino | 773 |
| Bachelor's or higher | 9378 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 19](/us/states/ia/districts/senate/19.md) — 70% (state senate)
- [IA Senate District 11](/us/states/ia/districts/senate/11.md) — 30% (state senate)
- [IA House District 37](/us/states/ia/districts/house/37.md) — 70% (state house)
- [IA House District 21](/us/states/ia/districts/house/21.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
