---
type: Jurisdiction
title: "Bleckley County, GA"
classification: county
fips: "13023"
state: "GA"
demographics:
  population: 12430
  population_under_18: 2521
  population_18_64: 7654
  population_65_plus: 2255
  median_household_income: 62008
  poverty_rate: 19.32
  homeownership_rate: 72.95
  unemployment_rate: 5.89
  median_home_value: 149600
  gini_index: 0.4821
  vacancy_rate: 15.56
  race_white: 8486
  race_black: 3239
  race_asian: 116
  race_native: 16
  hispanic: 472
  bachelors_plus: 2219
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/133"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Bleckley County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12430 |
| Under 18 | 2521 |
| 18–64 | 7654 |
| 65+ | 2255 |
| Median household income | 62008 |
| Poverty rate | 19.32 |
| Homeownership rate | 72.95 |
| Unemployment rate | 5.89 |
| Median home value | 149600 |
| Gini index | 0.4821 |
| Vacancy rate | 15.56 |
| White | 8486 |
| Black | 3239 |
| Asian | 116 |
| Native | 16 |
| Hispanic/Latino | 472 |
| Bachelor's or higher | 2219 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 133](/us/states/ga/districts/house/133.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
