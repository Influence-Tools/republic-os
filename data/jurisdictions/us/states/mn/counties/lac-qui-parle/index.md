---
type: Jurisdiction
title: "Lac qui Parle County, MN"
classification: county
fips: "27073"
state: "MN"
demographics:
  population: 6682
  population_under_18: 1452
  population_18_64: 3387
  population_65_plus: 1843
  median_household_income: 74432
  poverty_rate: 8.14
  homeownership_rate: 82.52
  unemployment_rate: 2.0
  median_home_value: 157600
  gini_index: 0.4681
  vacancy_rate: 15.71
  race_white: 6237
  race_black: 23
  race_asian: 42
  race_native: 11
  hispanic: 230
  bachelors_plus: 1347
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mn/districts/house/15a"
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

# Lac qui Parle County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6682 |
| Under 18 | 1452 |
| 18–64 | 3387 |
| 65+ | 1843 |
| Median household income | 74432 |
| Poverty rate | 8.14 |
| Homeownership rate | 82.52 |
| Unemployment rate | 2.0 |
| Median home value | 157600 |
| Gini index | 0.4681 |
| Vacancy rate | 15.71 |
| White | 6237 |
| Black | 23 |
| Asian | 42 |
| Native | 11 |
| Hispanic/Latino | 230 |
| Bachelor's or higher | 1347 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 15](/us/states/mn/districts/senate/15.md) — 100% (state senate)
- [MN House District 15A](/us/states/mn/districts/house/15a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
