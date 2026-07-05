---
type: Jurisdiction
title: "Lumpkin County, GA"
classification: county
fips: "13187"
state: "GA"
demographics:
  population: 34505
  population_under_18: 5855
  population_18_64: 22231
  population_65_plus: 6419
  median_household_income: 77448
  poverty_rate: 14.15
  homeownership_rate: 76.34
  unemployment_rate: 5.71
  median_home_value: 307900
  gini_index: 0.4634
  vacancy_rate: 13.81
  race_white: 31196
  race_black: 721
  race_asian: 291
  race_native: 119
  hispanic: 2011
  bachelors_plus: 9542
districts:
  - to: "us/states/ga/districts/07"
    rel: in-district
    area_weight: 0.9897
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.0103
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/9"
    rel: in-district
    area_weight: 0.9185
  - to: "us/states/ga/districts/house/27"
    rel: in-district
    area_weight: 0.0759
  - to: "us/states/ga/districts/house/8"
    rel: in-district
    area_weight: 0.0056
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Lumpkin County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34505 |
| Under 18 | 5855 |
| 18–64 | 22231 |
| 65+ | 6419 |
| Median household income | 77448 |
| Poverty rate | 14.15 |
| Homeownership rate | 76.34 |
| Unemployment rate | 5.71 |
| Median home value | 307900 |
| Gini index | 0.4634 |
| Vacancy rate | 13.81 |
| White | 31196 |
| Black | 721 |
| Asian | 291 |
| Native | 119 |
| Hispanic/Latino | 2011 |
| Bachelor's or higher | 9542 |

## Districts

- [GA-07](/us/states/ga/districts/07.md) — 99% (congressional)
- [GA-09](/us/states/ga/districts/09.md) — 1% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 9](/us/states/ga/districts/house/9.md) — 92% (state house)
- [GA House District 27](/us/states/ga/districts/house/27.md) — 8% (state house)
- [GA House District 8](/us/states/ga/districts/house/8.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
