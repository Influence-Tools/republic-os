---
type: Jurisdiction
title: "Miner County, SD"
classification: county
fips: "46097"
state: "SD"
demographics:
  population: 2300
  population_under_18: 547
  population_18_64: 508
  population_65_plus: 1245
  median_household_income: 76140
  poverty_rate: 11.24
  homeownership_rate: 84.76
  unemployment_rate: 0.25
  median_home_value: 142600
  gini_index: 0.521
  vacancy_rate: 21.02
  race_white: 2208
  race_black: 16
  race_asian: 4
  race_native: 17
  hispanic: 30
  bachelors_plus: 347
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/8"
    rel: in-district
    area_weight: 0.8111
  - to: "us/states/sd/districts/senate/20"
    rel: in-district
    area_weight: 0.1889
  - to: "us/states/sd/districts/house/8"
    rel: in-district
    area_weight: 0.8111
  - to: "us/states/sd/districts/house/20"
    rel: in-district
    area_weight: 0.1889
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Miner County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2300 |
| Under 18 | 547 |
| 18–64 | 508 |
| 65+ | 1245 |
| Median household income | 76140 |
| Poverty rate | 11.24 |
| Homeownership rate | 84.76 |
| Unemployment rate | 0.25 |
| Median home value | 142600 |
| Gini index | 0.521 |
| Vacancy rate | 21.02 |
| White | 2208 |
| Black | 16 |
| Asian | 4 |
| Native | 17 |
| Hispanic/Latino | 30 |
| Bachelor's or higher | 347 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 8](/us/states/sd/districts/senate/8.md) — 81% (state senate)
- [SD Senate District 20](/us/states/sd/districts/senate/20.md) — 19% (state senate)
- [SD House District 8](/us/states/sd/districts/house/8.md) — 81% (state house)
- [SD House District 20](/us/states/sd/districts/house/20.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
