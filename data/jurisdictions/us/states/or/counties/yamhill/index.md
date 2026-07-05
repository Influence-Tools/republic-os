---
type: Jurisdiction
title: "Yamhill County, OR"
classification: county
fips: "41071"
state: "OR"
demographics:
  population: 108734
  population_under_18: 22912
  population_18_64: 65332
  population_65_plus: 20490
  median_household_income: 90063
  poverty_rate: 10.25
  homeownership_rate: 69.43
  unemployment_rate: 4.8
  median_home_value: 471700
  gini_index: 0.4436
  vacancy_rate: 4.74
  race_white: 83324
  race_black: 805
  race_asian: 2111
  race_native: 1094
  hispanic: 19181
  bachelors_plus: 30062
districts:
  - to: "us/states/or/districts/06"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/or/districts/senate/12"
    rel: in-district
    area_weight: 0.9811
  - to: "us/states/or/districts/senate/13"
    rel: in-district
    area_weight: 0.0181
  - to: "us/states/or/districts/house/24"
    rel: in-district
    area_weight: 0.8268
  - to: "us/states/or/districts/house/23"
    rel: in-district
    area_weight: 0.1543
  - to: "us/states/or/districts/house/26"
    rel: in-district
    area_weight: 0.0181
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Yamhill County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 108734 |
| Under 18 | 22912 |
| 18–64 | 65332 |
| 65+ | 20490 |
| Median household income | 90063 |
| Poverty rate | 10.25 |
| Homeownership rate | 69.43 |
| Unemployment rate | 4.8 |
| Median home value | 471700 |
| Gini index | 0.4436 |
| Vacancy rate | 4.74 |
| White | 83324 |
| Black | 805 |
| Asian | 2111 |
| Native | 1094 |
| Hispanic/Latino | 19181 |
| Bachelor's or higher | 30062 |

## Districts

- [OR-06](/us/states/or/districts/06.md) — 100% (congressional)
- [OR Senate District 12](/us/states/or/districts/senate/12.md) — 98% (state senate)
- [OR Senate District 13](/us/states/or/districts/senate/13.md) — 2% (state senate)
- [OR House District 24](/us/states/or/districts/house/24.md) — 83% (state house)
- [OR House District 23](/us/states/or/districts/house/23.md) — 15% (state house)
- [OR House District 26](/us/states/or/districts/house/26.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
