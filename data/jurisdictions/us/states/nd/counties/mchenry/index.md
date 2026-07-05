---
type: Jurisdiction
title: "McHenry County, ND"
classification: county
fips: "38049"
state: "ND"
demographics:
  population: 5207
  population_under_18: 1260
  population_18_64: 2794
  population_65_plus: 1153
  median_household_income: 80733
  poverty_rate: 9.69
  homeownership_rate: 81.37
  unemployment_rate: 4.13
  median_home_value: 151000
  gini_index: 0.408
  vacancy_rate: 20.79
  race_white: 4908
  race_black: 40
  race_asian: 12
  race_native: 40
  hispanic: 112
  bachelors_plus: 864
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/6"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# McHenry County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5207 |
| Under 18 | 1260 |
| 18–64 | 2794 |
| 65+ | 1153 |
| Median household income | 80733 |
| Poverty rate | 9.69 |
| Homeownership rate | 81.37 |
| Unemployment rate | 4.13 |
| Median home value | 151000 |
| Gini index | 0.408 |
| Vacancy rate | 20.79 |
| White | 4908 |
| Black | 40 |
| Asian | 12 |
| Native | 40 |
| Hispanic/Latino | 112 |
| Bachelor's or higher | 864 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 6](/us/states/nd/districts/senate/6.md) — 100% (state senate)
- [ND House District 6](/us/states/nd/districts/house/6.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
