---
type: Jurisdiction
title: "Noble County, IN"
classification: county
fips: "18113"
state: "IN"
demographics:
  population: 47495
  population_under_18: 11557
  population_18_64: 27818
  population_65_plus: 8120
  median_household_income: 71723
  poverty_rate: 9.15
  homeownership_rate: 77.15
  unemployment_rate: 3.16
  median_home_value: 196800
  gini_index: 0.4015
  vacancy_rate: 10.44
  race_white: 41054
  race_black: 156
  race_asian: 268
  race_native: 26
  hispanic: 5374
  bachelors_plus: 8179
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/18"
    rel: in-district
    area_weight: 0.8268
  - to: "us/states/in/districts/house/52"
    rel: in-district
    area_weight: 0.1731
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Noble County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47495 |
| Under 18 | 11557 |
| 18–64 | 27818 |
| 65+ | 8120 |
| Median household income | 71723 |
| Poverty rate | 9.15 |
| Homeownership rate | 77.15 |
| Unemployment rate | 3.16 |
| Median home value | 196800 |
| Gini index | 0.4015 |
| Vacancy rate | 10.44 |
| White | 41054 |
| Black | 156 |
| Asian | 268 |
| Native | 26 |
| Hispanic/Latino | 5374 |
| Bachelor's or higher | 8179 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 13](/us/states/in/districts/senate/13.md) — 100% (state senate)
- [IN House District 18](/us/states/in/districts/house/18.md) — 83% (state house)
- [IN House District 52](/us/states/in/districts/house/52.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
