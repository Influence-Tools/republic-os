---
type: Jurisdiction
title: "Grant County, ND"
classification: county
fips: "38037"
state: "ND"
demographics:
  population: 2269
  population_under_18: 510
  population_18_64: 1085
  population_65_plus: 674
  median_household_income: 57875
  poverty_rate: 16.61
  homeownership_rate: 83.38
  unemployment_rate: 3.57
  median_home_value: 93200
  gini_index: 0.5121
  vacancy_rate: 35.23
  race_white: 2097
  race_black: 3
  race_asian: 35
  race_native: 53
  hispanic: 28
  bachelors_plus: 422
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nd/districts/house/31"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Grant County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2269 |
| Under 18 | 510 |
| 18–64 | 1085 |
| 65+ | 674 |
| Median household income | 57875 |
| Poverty rate | 16.61 |
| Homeownership rate | 83.38 |
| Unemployment rate | 3.57 |
| Median home value | 93200 |
| Gini index | 0.5121 |
| Vacancy rate | 35.23 |
| White | 2097 |
| Black | 3 |
| Asian | 35 |
| Native | 53 |
| Hispanic/Latino | 28 |
| Bachelor's or higher | 422 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 31](/us/states/nd/districts/senate/31.md) — 100% (state senate)
- [ND House District 31](/us/states/nd/districts/house/31.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
