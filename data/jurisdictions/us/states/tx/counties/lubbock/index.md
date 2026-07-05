---
type: Jurisdiction
title: "Lubbock County, TX"
classification: county
fips: "48303"
state: "TX"
demographics:
  population: 318884
  population_under_18: 74972
  population_18_64: 201598
  population_65_plus: 42314
  median_household_income: 64155
  poverty_rate: 17.15
  homeownership_rate: 55.5
  unemployment_rate: 4.94
  median_home_value: 214100
  gini_index: 0.4828
  vacancy_rate: 9.41
  race_white: 200827
  race_black: 23567
  race_asian: 7734
  race_native: 1836
  hispanic: 115556
  bachelors_plus: 89566
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/83"
    rel: in-district
    area_weight: 0.692
  - to: "us/states/tx/districts/house/84"
    rel: in-district
    area_weight: 0.308
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lubbock County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 318884 |
| Under 18 | 74972 |
| 18–64 | 201598 |
| 65+ | 42314 |
| Median household income | 64155 |
| Poverty rate | 17.15 |
| Homeownership rate | 55.5 |
| Unemployment rate | 4.94 |
| Median home value | 214100 |
| Gini index | 0.4828 |
| Vacancy rate | 9.41 |
| White | 200827 |
| Black | 23567 |
| Asian | 7734 |
| Native | 1836 |
| Hispanic/Latino | 115556 |
| Bachelor's or higher | 89566 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 83](/us/states/tx/districts/house/83.md) — 69% (state house)
- [TX House District 84](/us/states/tx/districts/house/84.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
