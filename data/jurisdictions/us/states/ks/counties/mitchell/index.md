---
type: Jurisdiction
title: "Mitchell County, KS"
classification: county
fips: "20123"
state: "KS"
demographics:
  population: 5779
  population_under_18: 1325
  population_18_64: 3134
  population_65_plus: 1320
  median_household_income: 64246
  poverty_rate: 12.2
  homeownership_rate: 69.03
  unemployment_rate: 0.14
  median_home_value: 133800
  gini_index: 0.4539
  vacancy_rate: 13.99
  race_white: 5408
  race_black: 6
  race_asian: 39
  race_native: 16
  hispanic: 187
  bachelors_plus: 1402
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/107"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Mitchell County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5779 |
| Under 18 | 1325 |
| 18–64 | 3134 |
| 65+ | 1320 |
| Median household income | 64246 |
| Poverty rate | 12.2 |
| Homeownership rate | 69.03 |
| Unemployment rate | 0.14 |
| Median home value | 133800 |
| Gini index | 0.4539 |
| Vacancy rate | 13.99 |
| White | 5408 |
| Black | 6 |
| Asian | 39 |
| Native | 16 |
| Hispanic/Latino | 187 |
| Bachelor's or higher | 1402 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 107](/us/states/ks/districts/house/107.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
