---
type: Jurisdiction
title: "Lowndes County, AL"
classification: county
fips: "01085"
state: "AL"
demographics:
  population: 9833
  population_under_18: 2158
  population_18_64: 5652
  population_65_plus: 2023
  median_household_income: 37052
  poverty_rate: 29.95
  homeownership_rate: 77.52
  unemployment_rate: 6.84
  median_home_value: 86300
  gini_index: 0.5434
  vacancy_rate: 11.62
  race_white: 2428
  race_black: 7258
  race_asian: 0
  race_native: 11
  hispanic: 16
  bachelors_plus: 1304
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/69"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Lowndes County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9833 |
| Under 18 | 2158 |
| 18–64 | 5652 |
| 65+ | 2023 |
| Median household income | 37052 |
| Poverty rate | 29.95 |
| Homeownership rate | 77.52 |
| Unemployment rate | 6.84 |
| Median home value | 86300 |
| Gini index | 0.5434 |
| Vacancy rate | 11.62 |
| White | 2428 |
| Black | 7258 |
| Asian | 0 |
| Native | 11 |
| Hispanic/Latino | 16 |
| Bachelor's or higher | 1304 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 69](/us/states/al/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
