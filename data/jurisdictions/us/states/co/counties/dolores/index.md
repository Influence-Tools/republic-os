---
type: Jurisdiction
title: "Dolores County, CO"
classification: county
fips: "08033"
state: "CO"
demographics:
  population: 2432
  population_under_18: 340
  population_18_64: 1315
  population_65_plus: 777
  median_household_income: 64907
  poverty_rate: 21.63
  homeownership_rate: 81.34
  unemployment_rate: 2.48
  median_home_value: 247600
  gini_index: 0.4562
  vacancy_rate: 20.23
  race_white: 2029
  race_black: 0
  race_asian: 0
  race_native: 62
  hispanic: 241
  bachelors_plus: 644
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/58"
    rel: in-district
    area_weight: 0.9991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Dolores County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2432 |
| Under 18 | 340 |
| 18–64 | 1315 |
| 65+ | 777 |
| Median household income | 64907 |
| Poverty rate | 21.63 |
| Homeownership rate | 81.34 |
| Unemployment rate | 2.48 |
| Median home value | 247600 |
| Gini index | 0.4562 |
| Vacancy rate | 20.23 |
| White | 2029 |
| Black | 0 |
| Asian | 0 |
| Native | 62 |
| Hispanic/Latino | 241 |
| Bachelor's or higher | 644 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
