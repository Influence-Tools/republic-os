---
type: Jurisdiction
title: "Charlevoix County, MI"
classification: county
fips: "26029"
state: "MI"
demographics:
  population: 26108
  population_under_18: 4586
  population_18_64: 14455
  population_65_plus: 7067
  median_household_income: 76531
  poverty_rate: 8.73
  homeownership_rate: 83.49
  unemployment_rate: 3.35
  median_home_value: 276800
  gini_index: 0.4609
  vacancy_rate: 30.46
  race_white: 24313
  race_black: 136
  race_asian: 176
  race_native: 223
  hispanic: 530
  bachelors_plus: 9861
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.3291
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.3245
  - to: "us/states/mi/districts/house/107"
    rel: in-district
    area_weight: 0.3245
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Charlevoix County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26108 |
| Under 18 | 4586 |
| 18–64 | 14455 |
| 65+ | 7067 |
| Median household income | 76531 |
| Poverty rate | 8.73 |
| Homeownership rate | 83.49 |
| Unemployment rate | 3.35 |
| Median home value | 276800 |
| Gini index | 0.4609 |
| Vacancy rate | 30.46 |
| White | 24313 |
| Black | 136 |
| Asian | 176 |
| Native | 223 |
| Hispanic/Latino | 530 |
| Bachelor's or higher | 9861 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 33% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 32% (state senate)
- [MI House District 107](/us/states/mi/districts/house/107.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
