---
type: Jurisdiction
title: "Chippewa County, MN"
classification: county
fips: "27023"
state: "MN"
demographics:
  population: 12377
  population_under_18: 3014
  population_18_64: 6705
  population_65_plus: 2658
  median_household_income: 71458
  poverty_rate: 14.53
  homeownership_rate: 72.3
  unemployment_rate: 4.35
  median_home_value: 156100
  gini_index: 0.433
  vacancy_rate: 9.45
  race_white: 10309
  race_black: 66
  race_asian: 182
  race_native: 173
  hispanic: 1307
  bachelors_plus: 2122
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/16"
    rel: in-district
    area_weight: 0.9948
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.0052
  - to: "us/states/mn/districts/house/16a"
    rel: in-district
    area_weight: 0.9947
  - to: "us/states/mn/districts/house/15a"
    rel: in-district
    area_weight: 0.0052
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Chippewa County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12377 |
| Under 18 | 3014 |
| 18–64 | 6705 |
| 65+ | 2658 |
| Median household income | 71458 |
| Poverty rate | 14.53 |
| Homeownership rate | 72.3 |
| Unemployment rate | 4.35 |
| Median home value | 156100 |
| Gini index | 0.433 |
| Vacancy rate | 9.45 |
| White | 10309 |
| Black | 66 |
| Asian | 182 |
| Native | 173 |
| Hispanic/Latino | 1307 |
| Bachelor's or higher | 2122 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 16](/us/states/mn/districts/senate/16.md) — 99% (state senate)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 1% (state senate)
- [MN House District 16A](/us/states/mn/districts/house/16a.md) — 99% (state house)
- [MN House District 15A](/us/states/mn/districts/house/15a.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
