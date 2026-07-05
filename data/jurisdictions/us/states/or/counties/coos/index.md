---
type: Jurisdiction
title: "Coos County, OR"
classification: county
fips: "41011"
state: "OR"
demographics:
  population: 64827
  population_under_18: 11391
  population_18_64: 35206
  population_65_plus: 18230
  median_household_income: 62143
  poverty_rate: 16.14
  homeownership_rate: 71.16
  unemployment_rate: 6.0
  median_home_value: 337800
  gini_index: 0.4669
  vacancy_rate: 9.95
  race_white: 54632
  race_black: 415
  race_asian: 771
  race_native: 1073
  hispanic: 4720
  bachelors_plus: 15480
districts:
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.9002
  - to: "us/states/or/districts/senate/1"
    rel: in-district
    area_weight: 0.7445
  - to: "us/states/or/districts/senate/5"
    rel: in-district
    area_weight: 0.156
  - to: "us/states/or/districts/house/1"
    rel: in-district
    area_weight: 0.7445
  - to: "us/states/or/districts/house/9"
    rel: in-district
    area_weight: 0.156
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Coos County, OR

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64827 |
| Under 18 | 11391 |
| 18–64 | 35206 |
| 65+ | 18230 |
| Median household income | 62143 |
| Poverty rate | 16.14 |
| Homeownership rate | 71.16 |
| Unemployment rate | 6.0 |
| Median home value | 337800 |
| Gini index | 0.4669 |
| Vacancy rate | 9.95 |
| White | 54632 |
| Black | 415 |
| Asian | 771 |
| Native | 1073 |
| Hispanic/Latino | 4720 |
| Bachelor's or higher | 15480 |

## Districts

- [OR-04](/us/states/or/districts/04.md) — 90% (congressional)
- [OR Senate District 1](/us/states/or/districts/senate/1.md) — 74% (state senate)
- [OR Senate District 5](/us/states/or/districts/senate/5.md) — 16% (state senate)
- [OR House District 1](/us/states/or/districts/house/1.md) — 74% (state house)
- [OR House District 9](/us/states/or/districts/house/9.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
