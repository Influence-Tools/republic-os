---
type: Jurisdiction
title: "Haskell County, TX"
classification: county
fips: "48207"
state: "TX"
demographics:
  population: 5421
  population_under_18: 981
  population_18_64: 3210
  population_65_plus: 1230
  median_household_income: 60653
  poverty_rate: 16.55
  homeownership_rate: 73.67
  unemployment_rate: 4.88
  median_home_value: 98700
  gini_index: 0.5417
  vacancy_rate: 31.09
  race_white: 4152
  race_black: 321
  race_asian: 10
  race_native: 9
  hispanic: 1432
  bachelors_plus: 1308
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
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

# Haskell County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5421 |
| Under 18 | 981 |
| 18–64 | 3210 |
| 65+ | 1230 |
| Median household income | 60653 |
| Poverty rate | 16.55 |
| Homeownership rate | 73.67 |
| Unemployment rate | 4.88 |
| Median home value | 98700 |
| Gini index | 0.5417 |
| Vacancy rate | 31.09 |
| White | 4152 |
| Black | 321 |
| Asian | 10 |
| Native | 9 |
| Hispanic/Latino | 1432 |
| Bachelor's or higher | 1308 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
