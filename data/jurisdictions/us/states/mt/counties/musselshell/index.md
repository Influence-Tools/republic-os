---
type: Jurisdiction
title: "Musselshell County, MT"
classification: county
fips: "30065"
state: "MT"
demographics:
  population: 5152
  population_under_18: 998
  population_18_64: 2660
  population_65_plus: 1494
  median_household_income: 58920
  poverty_rate: 17.03
  homeownership_rate: 85.06
  unemployment_rate: 9.22
  median_home_value: 235000
  gini_index: 0.4739
  vacancy_rate: 19.34
  race_white: 4495
  race_black: 0
  race_asian: 0
  race_native: 196
  hispanic: 221
  bachelors_plus: 1078
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/38"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Musselshell County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5152 |
| Under 18 | 998 |
| 18–64 | 2660 |
| 65+ | 1494 |
| Median household income | 58920 |
| Poverty rate | 17.03 |
| Homeownership rate | 85.06 |
| Unemployment rate | 9.22 |
| Median home value | 235000 |
| Gini index | 0.4739 |
| Vacancy rate | 19.34 |
| White | 4495 |
| Black | 0 |
| Asian | 0 |
| Native | 196 |
| Hispanic/Latino | 221 |
| Bachelor's or higher | 1078 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 19](/us/states/mt/districts/senate/19.md) — 100% (state senate)
- [MT House District 38](/us/states/mt/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
