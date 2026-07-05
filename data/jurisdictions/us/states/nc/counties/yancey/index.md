---
type: Jurisdiction
title: "Yancey County, NC"
classification: county
fips: "37199"
state: "NC"
demographics:
  population: 18797
  population_under_18: 3379
  population_18_64: 10333
  population_65_plus: 5085
  median_household_income: 58709
  poverty_rate: 15.17
  homeownership_rate: 79.42
  unemployment_rate: 7.3
  median_home_value: 243100
  gini_index: 0.4869
  vacancy_rate: 28.53
  race_white: 17315
  race_black: 157
  race_asian: 86
  race_native: 38
  hispanic: 1091
  bachelors_plus: 4767
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/85"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Yancey County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18797 |
| Under 18 | 3379 |
| 18–64 | 10333 |
| 65+ | 5085 |
| Median household income | 58709 |
| Poverty rate | 15.17 |
| Homeownership rate | 79.42 |
| Unemployment rate | 7.3 |
| Median home value | 243100 |
| Gini index | 0.4869 |
| Vacancy rate | 28.53 |
| White | 17315 |
| Black | 157 |
| Asian | 86 |
| Native | 38 |
| Hispanic/Latino | 1091 |
| Bachelor's or higher | 4767 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 100% (state senate)
- [NC House District 85](/us/states/nc/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
