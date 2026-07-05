---
type: Jurisdiction
title: "Campbell County, SD"
classification: county
fips: "46021"
state: "SD"
demographics:
  population: 1593
  population_under_18: 331
  population_18_64: 833
  population_65_plus: 429
  median_household_income: 68929
  poverty_rate: 7.67
  homeownership_rate: 76.26
  unemployment_rate: 3.13
  median_home_value: 115900
  gini_index: 0.4737
  vacancy_rate: 18.04
  race_white: 1451
  race_black: 0
  race_asian: 1
  race_native: 8
  hispanic: 125
  bachelors_plus: 529
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Campbell County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1593 |
| Under 18 | 331 |
| 18–64 | 833 |
| 65+ | 429 |
| Median household income | 68929 |
| Poverty rate | 7.67 |
| Homeownership rate | 76.26 |
| Unemployment rate | 3.13 |
| Median home value | 115900 |
| Gini index | 0.4737 |
| Vacancy rate | 18.04 |
| White | 1451 |
| Black | 0 |
| Asian | 1 |
| Native | 8 |
| Hispanic/Latino | 125 |
| Bachelor's or higher | 529 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
