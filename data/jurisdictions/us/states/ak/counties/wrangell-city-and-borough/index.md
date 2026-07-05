---
type: Jurisdiction
title: "Wrangell City and Borough, AK"
classification: county
fips: "02275"
state: "AK"
demographics:
  population: 2088
  population_under_18: 456
  population_18_64: 532
  population_65_plus: 1100
  median_household_income: 63750
  poverty_rate: 12.09
  homeownership_rate: 59.12
  unemployment_rate: 4.33
  median_home_value: 296400
  gini_index: 0.4282
  vacancy_rate: 25.1
  race_white: 1186
  race_black: 2
  race_asian: 89
  race_native: 381
  hispanic: 79
  bachelors_plus: 417
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.8026
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.7714
  - to: "us/states/ak/districts/house/1"
    rel: in-district
    area_weight: 0.7714
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Wrangell City and Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2088 |
| Under 18 | 456 |
| 18–64 | 532 |
| 65+ | 1100 |
| Median household income | 63750 |
| Poverty rate | 12.09 |
| Homeownership rate | 59.12 |
| Unemployment rate | 4.33 |
| Median home value | 296400 |
| Gini index | 0.4282 |
| Vacancy rate | 25.1 |
| White | 1186 |
| Black | 2 |
| Asian | 89 |
| Native | 381 |
| Hispanic/Latino | 79 |
| Bachelor's or higher | 417 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 80% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 77% (state senate)
- [AK House District 1](/us/states/ak/districts/house/1.md) — 77% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
