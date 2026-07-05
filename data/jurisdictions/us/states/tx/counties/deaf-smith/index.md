---
type: Jurisdiction
title: "Deaf Smith County, TX"
classification: county
fips: "48117"
state: "TX"
demographics:
  population: 18460
  population_under_18: 5794
  population_18_64: 10231
  population_65_plus: 2435
  median_household_income: 60799
  poverty_rate: 17.67
  homeownership_rate: 66.82
  unemployment_rate: 3.45
  median_home_value: 121300
  gini_index: 0.4164
  vacancy_rate: 13.36
  race_white: 7469
  race_black: 479
  race_asian: 12
  race_native: 113
  hispanic: 14110
  bachelors_plus: 1566
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/86"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Deaf Smith County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18460 |
| Under 18 | 5794 |
| 18–64 | 10231 |
| 65+ | 2435 |
| Median household income | 60799 |
| Poverty rate | 17.67 |
| Homeownership rate | 66.82 |
| Unemployment rate | 3.45 |
| Median home value | 121300 |
| Gini index | 0.4164 |
| Vacancy rate | 13.36 |
| White | 7469 |
| Black | 479 |
| Asian | 12 |
| Native | 113 |
| Hispanic/Latino | 14110 |
| Bachelor's or higher | 1566 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
