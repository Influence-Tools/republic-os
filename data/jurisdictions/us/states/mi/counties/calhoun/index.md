---
type: Jurisdiction
title: "Calhoun County, MI"
classification: county
fips: "26025"
state: "MI"
demographics:
  population: 133778
  population_under_18: 30588
  population_18_64: 78263
  population_65_plus: 24927
  median_household_income: 63177
  poverty_rate: 13.94
  homeownership_rate: 72.65
  unemployment_rate: 6.42
  median_home_value: 162800
  gini_index: 0.4441
  vacancy_rate: 10.52
  race_white: 102224
  race_black: 13067
  race_asian: 3495
  race_native: 474
  hispanic: 7914
  bachelors_plus: 28345
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.7982
  - to: "us/states/mi/districts/04"
    rel: in-district
    area_weight: 0.2017
  - to: "us/states/mi/districts/senate/18"
    rel: in-district
    area_weight: 0.6059
  - to: "us/states/mi/districts/senate/17"
    rel: in-district
    area_weight: 0.3941
  - to: "us/states/mi/districts/house/45"
    rel: in-district
    area_weight: 0.6439
  - to: "us/states/mi/districts/house/44"
    rel: in-district
    area_weight: 0.3561
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Calhoun County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 133778 |
| Under 18 | 30588 |
| 18–64 | 78263 |
| 65+ | 24927 |
| Median household income | 63177 |
| Poverty rate | 13.94 |
| Homeownership rate | 72.65 |
| Unemployment rate | 6.42 |
| Median home value | 162800 |
| Gini index | 0.4441 |
| Vacancy rate | 10.52 |
| White | 102224 |
| Black | 13067 |
| Asian | 3495 |
| Native | 474 |
| Hispanic/Latino | 7914 |
| Bachelor's or higher | 28345 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 80% (congressional)
- [MI-04](/us/states/mi/districts/04.md) — 20% (congressional)
- [MI Senate District 18](/us/states/mi/districts/senate/18.md) — 61% (state senate)
- [MI Senate District 17](/us/states/mi/districts/senate/17.md) — 39% (state senate)
- [MI House District 45](/us/states/mi/districts/house/45.md) — 64% (state house)
- [MI House District 44](/us/states/mi/districts/house/44.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
