---
type: Jurisdiction
title: "Cass County, ND"
classification: county
fips: "38017"
state: "ND"
demographics:
  population: 193400
  population_under_18: 42900
  population_18_64: 125346
  population_65_plus: 25154
  median_household_income: 75555
  poverty_rate: 11.0
  homeownership_rate: 51.97
  unemployment_rate: 2.98
  median_home_value: 298000
  gini_index: 0.4659
  vacancy_rate: 5.72
  race_white: 159233
  race_black: 13496
  race_asian: 6219
  race_native: 1881
  hispanic: 6953
  bachelors_plus: 69217
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/nd/districts/senate/22"
    rel: in-district
    area_weight: 0.793
  - to: "us/states/nd/districts/senate/45"
    rel: in-district
    area_weight: 0.1404
  - to: "us/states/nd/districts/senate/27"
    rel: in-district
    area_weight: 0.0429
  - to: "us/states/nd/districts/house/22"
    rel: in-district
    area_weight: 0.793
  - to: "us/states/nd/districts/house/45"
    rel: in-district
    area_weight: 0.1404
  - to: "us/states/nd/districts/house/27"
    rel: in-district
    area_weight: 0.0429
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Cass County, ND

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 193400 |
| Under 18 | 42900 |
| 18–64 | 125346 |
| 65+ | 25154 |
| Median household income | 75555 |
| Poverty rate | 11.0 |
| Homeownership rate | 51.97 |
| Unemployment rate | 2.98 |
| Median home value | 298000 |
| Gini index | 0.4659 |
| Vacancy rate | 5.72 |
| White | 159233 |
| Black | 13496 |
| Asian | 6219 |
| Native | 1881 |
| Hispanic/Latino | 6953 |
| Bachelor's or higher | 69217 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 22](/us/states/nd/districts/senate/22.md) — 79% (state senate)
- [ND Senate District 45](/us/states/nd/districts/senate/45.md) — 14% (state senate)
- [ND Senate District 27](/us/states/nd/districts/senate/27.md) — 4% (state senate)
- [ND House District 22](/us/states/nd/districts/house/22.md) — 79% (state house)
- [ND House District 45](/us/states/nd/districts/house/45.md) — 14% (state house)
- [ND House District 27](/us/states/nd/districts/house/27.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
