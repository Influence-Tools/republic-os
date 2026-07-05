---
type: Jurisdiction
title: "Wadena County, MN"
classification: county
fips: "27159"
state: "MN"
demographics:
  population: 14256
  population_under_18: 3722
  population_18_64: 7653
  population_65_plus: 2881
  median_household_income: 61467
  poverty_rate: 12.48
  homeownership_rate: 73.57
  unemployment_rate: 5.49
  median_home_value: 173000
  gini_index: 0.4201
  vacancy_rate: 13.39
  race_white: 12328
  race_black: 243
  race_asian: 44
  race_native: 30
  hispanic: 345
  bachelors_plus: 2349
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/mn/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/5a"
    rel: in-district
    area_weight: 0.529
  - to: "us/states/mn/districts/house/5b"
    rel: in-district
    area_weight: 0.4709
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Wadena County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14256 |
| Under 18 | 3722 |
| 18–64 | 7653 |
| 65+ | 2881 |
| Median household income | 61467 |
| Poverty rate | 12.48 |
| Homeownership rate | 73.57 |
| Unemployment rate | 5.49 |
| Median home value | 173000 |
| Gini index | 0.4201 |
| Vacancy rate | 13.39 |
| White | 12328 |
| Black | 243 |
| Asian | 44 |
| Native | 30 |
| Hispanic/Latino | 345 |
| Bachelor's or higher | 2349 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 5](/us/states/mn/districts/senate/5.md) — 100% (state senate)
- [MN House District 5A](/us/states/mn/districts/house/5a.md) — 53% (state house)
- [MN House District 5B](/us/states/mn/districts/house/5b.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
