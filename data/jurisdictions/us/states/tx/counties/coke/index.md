---
type: Jurisdiction
title: "Coke County, TX"
classification: county
fips: "48081"
state: "TX"
demographics:
  population: 3353
  population_under_18: 713
  population_18_64: 1734
  population_65_plus: 906
  median_household_income: 43333
  poverty_rate: 22.85
  homeownership_rate: 71.14
  unemployment_rate: 5.58
  median_home_value: 117900
  gini_index: 0.4652
  vacancy_rate: 25.65
  race_white: 2826
  race_black: 42
  race_asian: 8
  race_native: 14
  hispanic: 706
  bachelors_plus: 723
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/72"
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

# Coke County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3353 |
| Under 18 | 713 |
| 18–64 | 1734 |
| 65+ | 906 |
| Median household income | 43333 |
| Poverty rate | 22.85 |
| Homeownership rate | 71.14 |
| Unemployment rate | 5.58 |
| Median home value | 117900 |
| Gini index | 0.4652 |
| Vacancy rate | 25.65 |
| White | 2826 |
| Black | 42 |
| Asian | 8 |
| Native | 14 |
| Hispanic/Latino | 706 |
| Bachelor's or higher | 723 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
