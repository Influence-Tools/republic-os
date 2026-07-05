---
type: Jurisdiction
title: "Bristol Bay Borough, AK"
classification: county
fips: "02060"
state: "AK"
demographics:
  population: 918
  population_under_18: 143
  population_18_64: 344
  population_65_plus: 431
  median_household_income: 95625
  poverty_rate: 9.25
  homeownership_rate: 53.61
  unemployment_rate: 4.36
  median_home_value: 245800
  gini_index: 0.4486
  vacancy_rate: 63.53
  race_white: 447
  race_black: 5
  race_asian: 92
  race_native: 194
  hispanic: 46
  bachelors_plus: 182
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.6043
  - to: "us/states/ak/districts/senate/s"
    rel: in-district
    area_weight: 0.6022
  - to: "us/states/ak/districts/house/37"
    rel: in-district
    area_weight: 0.6022
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Bristol Bay Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 918 |
| Under 18 | 143 |
| 18–64 | 344 |
| 65+ | 431 |
| Median household income | 95625 |
| Poverty rate | 9.25 |
| Homeownership rate | 53.61 |
| Unemployment rate | 4.36 |
| Median home value | 245800 |
| Gini index | 0.4486 |
| Vacancy rate | 63.53 |
| White | 447 |
| Black | 5 |
| Asian | 92 |
| Native | 194 |
| Hispanic/Latino | 46 |
| Bachelor's or higher | 182 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 60% (congressional)
- [AK Senate District S](/us/states/ak/districts/senate/s.md) — 60% (state senate)
- [AK House District 37](/us/states/ak/districts/house/37.md) — 60% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
