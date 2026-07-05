---
type: Jurisdiction
title: "Bosque County, TX"
classification: county
fips: "48035"
state: "TX"
demographics:
  population: 18687
  population_under_18: 3882
  population_18_64: 10020
  population_65_plus: 4785
  median_household_income: 68914
  poverty_rate: 9.29
  homeownership_rate: 75.83
  unemployment_rate: 3.58
  median_home_value: 200900
  gini_index: 0.4491
  vacancy_rate: 19.81
  race_white: 14409
  race_black: 230
  race_asian: 81
  race_native: 41
  hispanic: 3576
  bachelors_plus: 3687
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/13"
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

# Bosque County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18687 |
| Under 18 | 3882 |
| 18–64 | 10020 |
| 65+ | 4785 |
| Median household income | 68914 |
| Poverty rate | 9.29 |
| Homeownership rate | 75.83 |
| Unemployment rate | 3.58 |
| Median home value | 200900 |
| Gini index | 0.4491 |
| Vacancy rate | 19.81 |
| White | 14409 |
| Black | 230 |
| Asian | 81 |
| Native | 41 |
| Hispanic/Latino | 3576 |
| Bachelor's or higher | 3687 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 13](/us/states/tx/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
