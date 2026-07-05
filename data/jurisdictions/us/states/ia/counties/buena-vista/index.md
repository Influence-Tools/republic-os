---
type: Jurisdiction
title: "Buena Vista County, IA"
classification: county
fips: "19021"
state: "IA"
demographics:
  population: 20753
  population_under_18: 5519
  population_18_64: 11861
  population_65_plus: 3373
  median_household_income: 71719
  poverty_rate: 7.79
  homeownership_rate: 73.22
  unemployment_rate: 5.55
  median_home_value: 159500
  gini_index: 0.4217
  vacancy_rate: 9.01
  race_white: 12457
  race_black: 679
  race_asian: 1982
  race_native: 85
  hispanic: 6094
  bachelors_plus: 3884
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/6"
    rel: in-district
    area_weight: 0.7506
  - to: "us/states/ia/districts/house/5"
    rel: in-district
    area_weight: 0.2493
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Buena Vista County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20753 |
| Under 18 | 5519 |
| 18–64 | 11861 |
| 65+ | 3373 |
| Median household income | 71719 |
| Poverty rate | 7.79 |
| Homeownership rate | 73.22 |
| Unemployment rate | 5.55 |
| Median home value | 159500 |
| Gini index | 0.4217 |
| Vacancy rate | 9.01 |
| White | 12457 |
| Black | 679 |
| Asian | 1982 |
| Native | 85 |
| Hispanic/Latino | 6094 |
| Bachelor's or higher | 3884 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 3](/us/states/ia/districts/senate/3.md) — 100% (state senate)
- [IA House District 6](/us/states/ia/districts/house/6.md) — 75% (state house)
- [IA House District 5](/us/states/ia/districts/house/5.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
