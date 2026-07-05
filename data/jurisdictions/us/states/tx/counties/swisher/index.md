---
type: Jurisdiction
title: "Swisher County, TX"
classification: county
fips: "48437"
state: "TX"
demographics:
  population: 6937
  population_under_18: 1660
  population_18_64: 4150
  population_65_plus: 1127
  median_household_income: 36165
  poverty_rate: 30.1
  homeownership_rate: 66.43
  unemployment_rate: 4.29
  median_home_value: 86300
  gini_index: 0.5187
  vacancy_rate: 21.33
  race_white: 4126
  race_black: 543
  race_asian: 120
  race_native: 43
  hispanic: 3212
  bachelors_plus: 877
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/88"
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

# Swisher County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6937 |
| Under 18 | 1660 |
| 18–64 | 4150 |
| 65+ | 1127 |
| Median household income | 36165 |
| Poverty rate | 30.1 |
| Homeownership rate | 66.43 |
| Unemployment rate | 4.29 |
| Median home value | 86300 |
| Gini index | 0.5187 |
| Vacancy rate | 21.33 |
| White | 4126 |
| Black | 543 |
| Asian | 120 |
| Native | 43 |
| Hispanic/Latino | 3212 |
| Bachelor's or higher | 877 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
