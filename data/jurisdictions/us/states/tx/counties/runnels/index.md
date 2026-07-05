---
type: Jurisdiction
title: "Runnels County, TX"
classification: county
fips: "48399"
state: "TX"
demographics:
  population: 9874
  population_under_18: 2317
  population_18_64: 5444
  population_65_plus: 2113
  median_household_income: 62632
  poverty_rate: 10.98
  homeownership_rate: 75.01
  unemployment_rate: 4.9
  median_home_value: 109300
  gini_index: 0.4171
  vacancy_rate: 23.67
  race_white: 6360
  race_black: 290
  race_asian: 11
  race_native: 23
  hispanic: 3442
  bachelors_plus: 1715
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/72"
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

# Runnels County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9874 |
| Under 18 | 2317 |
| 18–64 | 5444 |
| 65+ | 2113 |
| Median household income | 62632 |
| Poverty rate | 10.98 |
| Homeownership rate | 75.01 |
| Unemployment rate | 4.9 |
| Median home value | 109300 |
| Gini index | 0.4171 |
| Vacancy rate | 23.67 |
| White | 6360 |
| Black | 290 |
| Asian | 11 |
| Native | 23 |
| Hispanic/Latino | 3442 |
| Bachelor's or higher | 1715 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
