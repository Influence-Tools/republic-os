---
type: Jurisdiction
title: "Houston County, MN"
classification: county
fips: "27055"
state: "MN"
demographics:
  population: 18653
  population_under_18: 3992
  population_18_64: 10265
  population_65_plus: 4396
  median_household_income: 79825
  poverty_rate: 6.58
  homeownership_rate: 83.38
  unemployment_rate: 1.57
  median_home_value: 239000
  gini_index: 0.4372
  vacancy_rate: 7.29
  race_white: 17487
  race_black: 50
  race_asian: 166
  race_native: 45
  hispanic: 289
  bachelors_plus: 5205
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/26b"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Houston County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18653 |
| Under 18 | 3992 |
| 18–64 | 10265 |
| 65+ | 4396 |
| Median household income | 79825 |
| Poverty rate | 6.58 |
| Homeownership rate | 83.38 |
| Unemployment rate | 1.57 |
| Median home value | 239000 |
| Gini index | 0.4372 |
| Vacancy rate | 7.29 |
| White | 17487 |
| Black | 50 |
| Asian | 166 |
| Native | 45 |
| Hispanic/Latino | 289 |
| Bachelor's or higher | 5205 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 26](/us/states/mn/districts/senate/26.md) — 100% (state senate)
- [MN House District 26B](/us/states/mn/districts/house/26b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
