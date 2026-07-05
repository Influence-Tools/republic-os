---
type: Jurisdiction
title: "Cass County, TX"
classification: county
fips: "48067"
state: "TX"
demographics:
  population: 28568
  population_under_18: 6413
  population_18_64: 15723
  population_65_plus: 6432
  median_household_income: 53813
  poverty_rate: 17.52
  homeownership_rate: 76.59
  unemployment_rate: 6.39
  median_home_value: 146400
  gini_index: 0.4692
  vacancy_rate: 15.64
  race_white: 21831
  race_black: 4640
  race_asian: 210
  race_native: 180
  hispanic: 1548
  bachelors_plus: 5031
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/1"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Cass County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28568 |
| Under 18 | 6413 |
| 18–64 | 15723 |
| 65+ | 6432 |
| Median household income | 53813 |
| Poverty rate | 17.52 |
| Homeownership rate | 76.59 |
| Unemployment rate | 6.39 |
| Median home value | 146400 |
| Gini index | 0.4692 |
| Vacancy rate | 15.64 |
| White | 21831 |
| Black | 4640 |
| Asian | 210 |
| Native | 180 |
| Hispanic/Latino | 1548 |
| Bachelor's or higher | 5031 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 1](/us/states/tx/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
