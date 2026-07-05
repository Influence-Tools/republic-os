---
type: Jurisdiction
title: "Carter County, MO"
classification: county
fips: "29035"
state: "MO"
demographics:
  population: 5297
  population_under_18: 1286
  population_18_64: 2919
  population_65_plus: 1092
  median_household_income: 50000
  poverty_rate: 20.77
  homeownership_rate: 60.7
  unemployment_rate: 3.84
  median_home_value: 159400
  gini_index: 0.4443
  vacancy_rate: 23.84
  race_white: 4905
  race_black: 22
  race_asian: 2
  race_native: 0
  hispanic: 121
  bachelors_plus: 476
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Carter County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5297 |
| Under 18 | 1286 |
| 18–64 | 2919 |
| 65+ | 1092 |
| Median household income | 50000 |
| Poverty rate | 20.77 |
| Homeownership rate | 60.7 |
| Unemployment rate | 3.84 |
| Median home value | 159400 |
| Gini index | 0.4443 |
| Vacancy rate | 23.84 |
| White | 4905 |
| Black | 22 |
| Asian | 2 |
| Native | 0 |
| Hispanic/Latino | 121 |
| Bachelor's or higher | 476 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
