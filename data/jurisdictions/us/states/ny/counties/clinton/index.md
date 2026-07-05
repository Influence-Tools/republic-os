---
type: Jurisdiction
title: "Clinton County, NY"
classification: county
fips: "36019"
state: "NY"
demographics:
  population: 78493
  population_under_18: 14165
  population_18_64: 49415
  population_65_plus: 14913
  median_household_income: 71224
  poverty_rate: 13.69
  homeownership_rate: 69.36
  unemployment_rate: 4.06
  median_home_value: 180600
  gini_index: 0.4475
  vacancy_rate: 10.89
  race_white: 69894
  race_black: 2559
  race_asian: 1240
  race_native: 196
  hispanic: 2758
  bachelors_plus: 21536
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/115"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Clinton County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 78493 |
| Under 18 | 14165 |
| 18–64 | 49415 |
| 65+ | 14913 |
| Median household income | 71224 |
| Poverty rate | 13.69 |
| Homeownership rate | 69.36 |
| Unemployment rate | 4.06 |
| Median home value | 180600 |
| Gini index | 0.4475 |
| Vacancy rate | 10.89 |
| White | 69894 |
| Black | 2559 |
| Asian | 1240 |
| Native | 196 |
| Hispanic/Latino | 2758 |
| Bachelor's or higher | 21536 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 100% (state senate)
- [NY House District 115](/us/states/ny/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
