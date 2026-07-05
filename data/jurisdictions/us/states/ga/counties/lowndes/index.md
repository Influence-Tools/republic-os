---
type: Jurisdiction
title: "Lowndes County, GA"
classification: county
fips: "13185"
state: "GA"
demographics:
  population: 119965
  population_under_18: 29477
  population_18_64: 74565
  population_65_plus: 15923
  median_household_income: 58541
  poverty_rate: 19.18
  homeownership_rate: 56.87
  unemployment_rate: 5.09
  median_home_value: 215600
  gini_index: 0.4922
  vacancy_rate: 10.39
  race_white: 62936
  race_black: 44625
  race_asian: 2285
  race_native: 378
  hispanic: 8552
  bachelors_plus: 28410
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/8"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/house/175"
    rel: in-district
    area_weight: 0.5372
  - to: "us/states/ga/districts/house/174"
    rel: in-district
    area_weight: 0.2945
  - to: "us/states/ga/districts/house/176"
    rel: in-district
    area_weight: 0.0673
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Lowndes County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 119965 |
| Under 18 | 29477 |
| 18–64 | 74565 |
| 65+ | 15923 |
| Median household income | 58541 |
| Poverty rate | 19.18 |
| Homeownership rate | 56.87 |
| Unemployment rate | 5.09 |
| Median home value | 215600 |
| Gini index | 0.4922 |
| Vacancy rate | 10.39 |
| White | 62936 |
| Black | 44625 |
| Asian | 2285 |
| Native | 378 |
| Hispanic/Latino | 8552 |
| Bachelor's or higher | 28410 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 8](/us/states/ga/districts/senate/8.md) — 100% (state senate)
- [GA House District 175](/us/states/ga/districts/house/175.md) — 54% (state house)
- [GA House District 174](/us/states/ga/districts/house/174.md) — 29% (state house)
- [GA House District 176](/us/states/ga/districts/house/176.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
