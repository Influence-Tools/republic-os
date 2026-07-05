---
type: Jurisdiction
title: "Ogemaw County, MI"
classification: county
fips: "26129"
state: "MI"
demographics:
  population: 20885
  population_under_18: 3720
  population_18_64: 11331
  population_65_plus: 5834
  median_household_income: 54666
  poverty_rate: 16.66
  homeownership_rate: 83.71
  unemployment_rate: 6.25
  median_home_value: 154900
  gini_index: 0.4336
  vacancy_rate: 38.86
  race_white: 19455
  race_black: 117
  race_asian: 162
  race_native: 60
  hispanic: 470
  bachelors_plus: 3669
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Ogemaw County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20885 |
| Under 18 | 3720 |
| 18–64 | 11331 |
| 65+ | 5834 |
| Median household income | 54666 |
| Poverty rate | 16.66 |
| Homeownership rate | 83.71 |
| Unemployment rate | 6.25 |
| Median home value | 154900 |
| Gini index | 0.4336 |
| Vacancy rate | 38.86 |
| White | 19455 |
| Black | 117 |
| Asian | 162 |
| Native | 60 |
| Hispanic/Latino | 470 |
| Bachelor's or higher | 3669 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
