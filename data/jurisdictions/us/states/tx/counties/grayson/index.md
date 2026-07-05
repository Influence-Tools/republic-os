---
type: Jurisdiction
title: "Grayson County, TX"
classification: county
fips: "48181"
state: "TX"
demographics:
  population: 143337
  population_under_18: 34451
  population_18_64: 83010
  population_65_plus: 25876
  median_household_income: 72182
  poverty_rate: 11.15
  homeownership_rate: 66.78
  unemployment_rate: 3.12
  median_home_value: 248400
  gini_index: 0.452
  vacancy_rate: 11.08
  race_white: 109325
  race_black: 7432
  race_asian: 2168
  race_native: 1050
  hispanic: 23433
  bachelors_plus: 30706
districts:
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/62"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Grayson County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 143337 |
| Under 18 | 34451 |
| 18–64 | 83010 |
| 65+ | 25876 |
| Median household income | 72182 |
| Poverty rate | 11.15 |
| Homeownership rate | 66.78 |
| Unemployment rate | 3.12 |
| Median home value | 248400 |
| Gini index | 0.452 |
| Vacancy rate | 11.08 |
| White | 109325 |
| Black | 7432 |
| Asian | 2168 |
| Native | 1050 |
| Hispanic/Latino | 23433 |
| Bachelor's or higher | 30706 |

## Districts

- [TX-04](/us/states/tx/districts/04.md) — 100% (congressional)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 100% (state senate)
- [TX House District 62](/us/states/tx/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
