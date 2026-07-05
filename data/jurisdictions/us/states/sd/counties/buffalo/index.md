---
type: Jurisdiction
title: "Buffalo County, SD"
classification: county
fips: "46017"
state: "SD"
demographics:
  population: 1808
  population_under_18: 708
  population_18_64: 934
  population_65_plus: 166
  median_household_income: 47045
  poverty_rate: 33.91
  homeownership_rate: 52.56
  unemployment_rate: 10.8
  median_home_value: 117800
  gini_index: 0.4952
  vacancy_rate: 12.11
  race_white: 316
  race_black: 0
  race_asian: 0
  race_native: 1428
  hispanic: 31
  bachelors_plus: 101
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

# Buffalo County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1808 |
| Under 18 | 708 |
| 18–64 | 934 |
| 65+ | 166 |
| Median household income | 47045 |
| Poverty rate | 33.91 |
| Homeownership rate | 52.56 |
| Unemployment rate | 10.8 |
| Median home value | 117800 |
| Gini index | 0.4952 |
| Vacancy rate | 12.11 |
| White | 316 |
| Black | 0 |
| Asian | 0 |
| Native | 1428 |
| Hispanic/Latino | 31 |
| Bachelor's or higher | 101 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 100% (state senate)
- [SD House District 26B](/us/states/sd/districts/house/26b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
