---
type: Jurisdiction
title: "Brule County, SD"
classification: county
fips: "46015"
state: "SD"
demographics:
  population: 5283
  population_under_18: 1283
  population_18_64: 2890
  population_65_plus: 1110
  median_household_income: 73720
  poverty_rate: 10.67
  homeownership_rate: 76.37
  unemployment_rate: 1.48
  median_home_value: 216800
  gini_index: 0.4436
  vacancy_rate: 17.41
  race_white: 4342
  race_black: 34
  race_asian: 0
  race_native: 541
  hispanic: 121
  bachelors_plus: 1312
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/26b"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Brule County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5283 |
| Under 18 | 1283 |
| 18–64 | 2890 |
| 65+ | 1110 |
| Median household income | 73720 |
| Poverty rate | 10.67 |
| Homeownership rate | 76.37 |
| Unemployment rate | 1.48 |
| Median home value | 216800 |
| Gini index | 0.4436 |
| Vacancy rate | 17.41 |
| White | 4342 |
| Black | 34 |
| Asian | 0 |
| Native | 541 |
| Hispanic/Latino | 121 |
| Bachelor's or higher | 1312 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 100% (state senate)
- [SD House District 26B](/us/states/sd/districts/house/26b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
