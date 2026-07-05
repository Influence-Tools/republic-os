---
type: Jurisdiction
title: "Fillmore County, MN"
classification: county
fips: "27045"
state: "MN"
demographics:
  population: 21414
  population_under_18: 5231
  population_18_64: 11437
  population_65_plus: 4746
  median_household_income: 77512
  poverty_rate: 8.39
  homeownership_rate: 82.56
  unemployment_rate: 2.72
  median_home_value: 221100
  gini_index: 0.4073
  vacancy_rate: 10.0
  race_white: 20344
  race_black: 112
  race_asian: 153
  race_native: 17
  hispanic: 421
  bachelors_plus: 4668
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/26b"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Fillmore County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21414 |
| Under 18 | 5231 |
| 18–64 | 11437 |
| 65+ | 4746 |
| Median household income | 77512 |
| Poverty rate | 8.39 |
| Homeownership rate | 82.56 |
| Unemployment rate | 2.72 |
| Median home value | 221100 |
| Gini index | 0.4073 |
| Vacancy rate | 10.0 |
| White | 20344 |
| Black | 112 |
| Asian | 153 |
| Native | 17 |
| Hispanic/Latino | 421 |
| Bachelor's or higher | 4668 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 26](/us/states/mn/districts/senate/26.md) — 100% (state senate)
- [MN House District 26B](/us/states/mn/districts/house/26b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
