---
type: Jurisdiction
title: "Sheridan County, ND"
classification: county
fips: "38083"
state: "ND"
demographics:
  population: 1303
  population_under_18: 219
  population_18_64: 667
  population_65_plus: 417
  median_household_income: 62639
  poverty_rate: 10.14
  homeownership_rate: 84.0
  unemployment_rate: 1.06
  median_home_value: 110300
  gini_index: 0.4416
  vacancy_rate: 19.45
  race_white: 1260
  race_black: 0
  race_asian: 7
  race_native: 5
  hispanic: 5
  bachelors_plus: 211
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Sheridan County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1303 |
| Under 18 | 219 |
| 18–64 | 667 |
| 65+ | 417 |
| Median household income | 62639 |
| Poverty rate | 10.14 |
| Homeownership rate | 84.0 |
| Unemployment rate | 1.06 |
| Median home value | 110300 |
| Gini index | 0.4416 |
| Vacancy rate | 19.45 |
| White | 1260 |
| Black | 0 |
| Asian | 7 |
| Native | 5 |
| Hispanic/Latino | 5 |
| Bachelor's or higher | 211 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 100% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
