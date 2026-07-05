---
type: Jurisdiction
title: "Bowie County, TX"
classification: county
fips: "48037"
state: "TX"
demographics:
  population: 92115
  population_under_18: 21902
  population_18_64: 54048
  population_65_plus: 16165
  median_household_income: 59803
  poverty_rate: 16.21
  homeownership_rate: 63.45
  unemployment_rate: 4.43
  median_home_value: 173000
  gini_index: 0.4729
  vacancy_rate: 12.2
  race_white: 59018
  race_black: 22866
  race_asian: 1273
  race_native: 467
  hispanic: 7938
  bachelors_plus: 20253
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 0.6407
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.3515
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/house/1"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bowie County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92115 |
| Under 18 | 21902 |
| 18–64 | 54048 |
| 65+ | 16165 |
| Median household income | 59803 |
| Poverty rate | 16.21 |
| Homeownership rate | 63.45 |
| Unemployment rate | 4.43 |
| Median home value | 173000 |
| Gini index | 0.4729 |
| Vacancy rate | 12.2 |
| White | 59018 |
| Black | 22866 |
| Asian | 1273 |
| Native | 467 |
| Hispanic/Latino | 7938 |
| Bachelor's or higher | 20253 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 64% (congressional)
- [TX-04](/us/states/tx/districts/04.md) — 35% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 1](/us/states/tx/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
