---
type: Jurisdiction
title: "Grimes County, TX"
classification: county
fips: "48185"
state: "TX"
demographics:
  population: 31340
  population_under_18: 7027
  population_18_64: 18488
  population_65_plus: 5825
  median_household_income: 69803
  poverty_rate: 14.57
  homeownership_rate: 79.92
  unemployment_rate: 5.06
  median_home_value: 237400
  gini_index: 0.4779
  vacancy_rate: 16.96
  race_white: 19177
  race_black: 3586
  race_asian: 116
  race_native: 175
  hispanic: 7998
  bachelors_plus: 5631
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/12"
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

# Grimes County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31340 |
| Under 18 | 7027 |
| 18–64 | 18488 |
| 65+ | 5825 |
| Median household income | 69803 |
| Poverty rate | 14.57 |
| Homeownership rate | 79.92 |
| Unemployment rate | 5.06 |
| Median home value | 237400 |
| Gini index | 0.4779 |
| Vacancy rate | 16.96 |
| White | 19177 |
| Black | 3586 |
| Asian | 116 |
| Native | 175 |
| Hispanic/Latino | 7998 |
| Bachelor's or higher | 5631 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 12](/us/states/tx/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
