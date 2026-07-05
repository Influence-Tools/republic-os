---
type: Jurisdiction
title: "Taylor County, WI"
classification: county
fips: "55119"
state: "WI"
demographics:
  population: 20024
  population_under_18: 4618
  population_18_64: 11130
  population_65_plus: 4276
  median_household_income: 69350
  poverty_rate: 9.57
  homeownership_rate: 79.7
  unemployment_rate: 2.62
  median_home_value: 197100
  gini_index: 0.4016
  vacancy_rate: 15.63
  race_white: 18903
  race_black: 67
  race_asian: 63
  race_native: 40
  hispanic: 599
  bachelors_plus: 3111
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/house/68"
    rel: in-district
    area_weight: 0.8136
  - to: "us/states/wi/districts/house/69"
    rel: in-district
    area_weight: 0.1864
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Taylor County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20024 |
| Under 18 | 4618 |
| 18–64 | 11130 |
| 65+ | 4276 |
| Median household income | 69350 |
| Poverty rate | 9.57 |
| Homeownership rate | 79.7 |
| Unemployment rate | 2.62 |
| Median home value | 197100 |
| Gini index | 0.4016 |
| Vacancy rate | 15.63 |
| White | 18903 |
| Black | 67 |
| Asian | 63 |
| Native | 40 |
| Hispanic/Latino | 599 |
| Bachelor's or higher | 3111 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 100% (state senate)
- [WI House District 68](/us/states/wi/districts/house/68.md) — 81% (state house)
- [WI House District 69](/us/states/wi/districts/house/69.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
