---
type: Jurisdiction
title: "Pennington County, MN"
classification: county
fips: "27113"
state: "MN"
demographics:
  population: 13791
  population_under_18: 2866
  population_18_64: 8260
  population_65_plus: 2665
  median_household_income: 77325
  poverty_rate: 10.46
  homeownership_rate: 72.16
  unemployment_rate: 2.88
  median_home_value: 195500
  gini_index: 0.413
  vacancy_rate: 8.71
  race_white: 12218
  race_black: 106
  race_asian: 211
  race_native: 50
  hispanic: 678
  bachelors_plus: 2559
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/1a"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Pennington County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13791 |
| Under 18 | 2866 |
| 18–64 | 8260 |
| 65+ | 2665 |
| Median household income | 77325 |
| Poverty rate | 10.46 |
| Homeownership rate | 72.16 |
| Unemployment rate | 2.88 |
| Median home value | 195500 |
| Gini index | 0.413 |
| Vacancy rate | 8.71 |
| White | 12218 |
| Black | 106 |
| Asian | 211 |
| Native | 50 |
| Hispanic/Latino | 678 |
| Bachelor's or higher | 2559 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1A](/us/states/mn/districts/house/1a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
