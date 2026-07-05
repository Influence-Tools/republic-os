---
type: Jurisdiction
title: "Colorado County, TX"
classification: county
fips: "48089"
state: "TX"
demographics:
  population: 21006
  population_under_18: 4899
  population_18_64: 11197
  population_65_plus: 4910
  median_household_income: 66377
  poverty_rate: 10.68
  homeownership_rate: 79.51
  unemployment_rate: 2.88
  median_home_value: 209800
  gini_index: 0.4518
  vacancy_rate: 21.43
  race_white: 12532
  race_black: 2159
  race_asian: 141
  race_native: 106
  hispanic: 6409
  bachelors_plus: 4375
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/85"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Colorado County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21006 |
| Under 18 | 4899 |
| 18–64 | 11197 |
| 65+ | 4910 |
| Median household income | 66377 |
| Poverty rate | 10.68 |
| Homeownership rate | 79.51 |
| Unemployment rate | 2.88 |
| Median home value | 209800 |
| Gini index | 0.4518 |
| Vacancy rate | 21.43 |
| White | 12532 |
| Black | 2159 |
| Asian | 141 |
| Native | 106 |
| Hispanic/Latino | 6409 |
| Bachelor's or higher | 4375 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 100% (state senate)
- [TX House District 85](/us/states/tx/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
