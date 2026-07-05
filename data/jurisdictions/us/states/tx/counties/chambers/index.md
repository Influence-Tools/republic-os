---
type: Jurisdiction
title: "Chambers County, TX"
classification: county
fips: "48071"
state: "TX"
demographics:
  population: 51498
  population_under_18: 14126
  population_18_64: 30881
  population_65_plus: 6491
  median_household_income: 109804
  poverty_rate: 11.85
  homeownership_rate: 81.56
  unemployment_rate: 7.27
  median_home_value: 329500
  gini_index: 0.4213
  vacancy_rate: 9.02
  race_white: 35031
  race_black: 4198
  race_asian: 779
  race_native: 85
  hispanic: 13637
  bachelors_plus: 8946
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.7165
  - to: "us/states/tx/districts/14"
    rel: in-district
    area_weight: 0.0062
  - to: "us/states/tx/districts/senate/4"
    rel: in-district
    area_weight: 0.7257
  - to: "us/states/tx/districts/house/23"
    rel: in-district
    area_weight: 0.7257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Chambers County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51498 |
| Under 18 | 14126 |
| 18–64 | 30881 |
| 65+ | 6491 |
| Median household income | 109804 |
| Poverty rate | 11.85 |
| Homeownership rate | 81.56 |
| Unemployment rate | 7.27 |
| Median home value | 329500 |
| Gini index | 0.4213 |
| Vacancy rate | 9.02 |
| White | 35031 |
| Black | 4198 |
| Asian | 779 |
| Native | 85 |
| Hispanic/Latino | 13637 |
| Bachelor's or higher | 8946 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 72% (congressional)
- [TX-14](/us/states/tx/districts/14.md) — 1% (congressional)
- [TX Senate District 4](/us/states/tx/districts/senate/4.md) — 73% (state senate)
- [TX House District 23](/us/states/tx/districts/house/23.md) — 73% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
