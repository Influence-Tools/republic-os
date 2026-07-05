---
type: Jurisdiction
title: "Marshall County, IA"
classification: county
fips: "19127"
state: "IA"
demographics:
  population: 40114
  population_under_18: 10175
  population_18_64: 22638
  population_65_plus: 7301
  median_household_income: 73315
  poverty_rate: 11.15
  homeownership_rate: 75.0
  unemployment_rate: 4.28
  median_home_value: 145500
  gini_index: 0.3848
  vacancy_rate: 8.51
  race_white: 28330
  race_black: 824
  race_asian: 1652
  race_native: 506
  hispanic: 9875
  bachelors_plus: 7946
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ia/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/51"
    rel: in-district
    area_weight: 0.732
  - to: "us/states/ia/districts/house/52"
    rel: in-district
    area_weight: 0.2678
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Marshall County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40114 |
| Under 18 | 10175 |
| 18–64 | 22638 |
| 65+ | 7301 |
| Median household income | 73315 |
| Poverty rate | 11.15 |
| Homeownership rate | 75.0 |
| Unemployment rate | 4.28 |
| Median home value | 145500 |
| Gini index | 0.3848 |
| Vacancy rate | 8.51 |
| White | 28330 |
| Black | 824 |
| Asian | 1652 |
| Native | 506 |
| Hispanic/Latino | 9875 |
| Bachelor's or higher | 7946 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 26](/us/states/ia/districts/senate/26.md) — 100% (state senate)
- [IA House District 51](/us/states/ia/districts/house/51.md) — 73% (state house)
- [IA House District 52](/us/states/ia/districts/house/52.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
