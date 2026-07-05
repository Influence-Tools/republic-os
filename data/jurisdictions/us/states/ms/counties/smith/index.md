---
type: Jurisdiction
title: "Smith County, MS"
classification: county
fips: "28129"
state: "MS"
demographics:
  population: 14132
  population_under_18: 3232
  population_18_64: 7944
  population_65_plus: 2956
  median_household_income: 60916
  poverty_rate: 17.05
  homeownership_rate: 87.43
  unemployment_rate: 4.45
  median_home_value: 112600
  gini_index: 0.4543
  vacancy_rate: 16.71
  race_white: 10504
  race_black: 3257
  race_asian: 43
  race_native: 0
  hispanic: 240
  bachelors_plus: 2126
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/79"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Smith County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14132 |
| Under 18 | 3232 |
| 18–64 | 7944 |
| 65+ | 2956 |
| Median household income | 60916 |
| Poverty rate | 17.05 |
| Homeownership rate | 87.43 |
| Unemployment rate | 4.45 |
| Median home value | 112600 |
| Gini index | 0.4543 |
| Vacancy rate | 16.71 |
| White | 10504 |
| Black | 3257 |
| Asian | 43 |
| Native | 0 |
| Hispanic/Latino | 240 |
| Bachelor's or higher | 2126 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 36](/us/states/ms/districts/senate/36.md) — 100% (state senate)
- [MS House District 79](/us/states/ms/districts/house/79.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
