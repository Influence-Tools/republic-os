---
type: Jurisdiction
title: "Liberty County, TX"
classification: county
fips: "48291"
state: "TX"
demographics:
  population: 103380
  population_under_18: 30946
  population_18_64: 60529
  population_65_plus: 11905
  median_household_income: 68703
  poverty_rate: 18.66
  homeownership_rate: 82.32
  unemployment_rate: 7.11
  median_home_value: 181700
  gini_index: 0.4452
  vacancy_rate: 13.67
  race_white: 58688
  race_black: 7853
  race_asian: 582
  race_native: 1060
  hispanic: 40921
  bachelors_plus: 9838
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/18"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Liberty County, TX

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103380 |
| Under 18 | 30946 |
| 18–64 | 60529 |
| 65+ | 11905 |
| Median household income | 68703 |
| Poverty rate | 18.66 |
| Homeownership rate | 82.32 |
| Unemployment rate | 7.11 |
| Median home value | 181700 |
| Gini index | 0.4452 |
| Vacancy rate | 13.67 |
| White | 58688 |
| Black | 7853 |
| Asian | 582 |
| Native | 1060 |
| Hispanic/Latino | 40921 |
| Bachelor's or higher | 9838 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 18](/us/states/tx/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
