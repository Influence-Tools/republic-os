---
type: Jurisdiction
title: "Fall River County, SD"
classification: county
fips: "46047"
state: "SD"
demographics:
  population: 7258
  population_under_18: 1178
  population_18_64: 3698
  population_65_plus: 2382
  median_household_income: 67917
  poverty_rate: 16.57
  homeownership_rate: 72.44
  unemployment_rate: 2.48
  median_home_value: 193200
  gini_index: 0.4209
  vacancy_rate: 11.26
  race_white: 6089
  race_black: 14
  race_asian: 140
  race_native: 376
  hispanic: 249
  bachelors_plus: 2251
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/30"
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

# Fall River County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7258 |
| Under 18 | 1178 |
| 18–64 | 3698 |
| 65+ | 2382 |
| Median household income | 67917 |
| Poverty rate | 16.57 |
| Homeownership rate | 72.44 |
| Unemployment rate | 2.48 |
| Median home value | 193200 |
| Gini index | 0.4209 |
| Vacancy rate | 11.26 |
| White | 6089 |
| Black | 14 |
| Asian | 140 |
| Native | 376 |
| Hispanic/Latino | 249 |
| Bachelor's or higher | 2251 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 30](/us/states/sd/districts/senate/30.md) — 100% (state senate)
- [SD House District 30](/us/states/sd/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
