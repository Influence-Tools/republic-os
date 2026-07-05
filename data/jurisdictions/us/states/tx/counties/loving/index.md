---
type: Jurisdiction
title: "Loving County, TX"
classification: county
fips: "48301"
state: "TX"
demographics:
  population: 33
  population_65_plus: 27
  median_household_income: 51250
  poverty_rate: 6.06
  homeownership_rate: 11.11
  unemployment_rate: 0.0
  gini_index: 0.3081
  vacancy_rate: 18.18
  race_white: 31
  race_black: 0
  race_asian: 2
  race_native: 0
  hispanic: 0
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/81"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Loving County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33 |
| 65+ | 27 |
| Median household income | 51250 |
| Poverty rate | 6.06 |
| Homeownership rate | 11.11 |
| Unemployment rate | 0.0 |
| Gini index | 0.3081 |
| Vacancy rate | 18.18 |
| White | 31 |
| Black | 0 |
| Asian | 2 |
| Native | 0 |
| Hispanic/Latino | 0 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 81](/us/states/tx/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
