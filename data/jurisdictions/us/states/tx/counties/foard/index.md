---
type: Jurisdiction
title: "Foard County, TX"
classification: county
fips: "48155"
state: "TX"
demographics:
  population: 991
  population_under_18: 150
  population_18_64: 525
  population_65_plus: 316
  median_household_income: 61563
  poverty_rate: 5.57
  homeownership_rate: 75.97
  unemployment_rate: 6.26
  median_home_value: 70700
  gini_index: 0.4775
  vacancy_rate: 29.86
  race_white: 829
  race_black: 3
  race_asian: 3
  race_native: 0
  hispanic: 118
  bachelors_plus: 175
districts:
  - to: "us/states/tx/districts/13"
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

# Foard County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 991 |
| Under 18 | 150 |
| 18–64 | 525 |
| 65+ | 316 |
| Median household income | 61563 |
| Poverty rate | 5.57 |
| Homeownership rate | 75.97 |
| Unemployment rate | 6.26 |
| Median home value | 70700 |
| Gini index | 0.4775 |
| Vacancy rate | 29.86 |
| White | 829 |
| Black | 3 |
| Asian | 3 |
| Native | 0 |
| Hispanic/Latino | 118 |
| Bachelor's or higher | 175 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
