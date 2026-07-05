---
type: Jurisdiction
title: "Midland County, TX"
classification: county
fips: "48329"
state: "TX"
demographics:
  population: 174801
  population_under_18: 50927
  population_18_64: 105092
  population_65_plus: 18782
  median_household_income: 92874
  poverty_rate: 11.35
  homeownership_rate: 67.63
  unemployment_rate: 3.36
  median_home_value: 312700
  gini_index: 0.484
  vacancy_rate: 6.97
  race_white: 97750
  race_black: 12602
  race_asian: 4197
  race_native: 988
  hispanic: 80341
  bachelors_plus: 44359
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/82"
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

# Midland County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 174801 |
| Under 18 | 50927 |
| 18–64 | 105092 |
| 65+ | 18782 |
| Median household income | 92874 |
| Poverty rate | 11.35 |
| Homeownership rate | 67.63 |
| Unemployment rate | 3.36 |
| Median home value | 312700 |
| Gini index | 0.484 |
| Vacancy rate | 6.97 |
| White | 97750 |
| Black | 12602 |
| Asian | 4197 |
| Native | 988 |
| Hispanic/Latino | 80341 |
| Bachelor's or higher | 44359 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 82](/us/states/tx/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
