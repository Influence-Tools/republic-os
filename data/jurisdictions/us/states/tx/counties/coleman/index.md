---
type: Jurisdiction
title: "Coleman County, TX"
classification: county
fips: "48083"
state: "TX"
demographics:
  population: 7833
  population_under_18: 1611
  population_18_64: 4169
  population_65_plus: 2053
  median_household_income: 49159
  poverty_rate: 19.64
  homeownership_rate: 77.18
  unemployment_rate: 7.67
  median_home_value: 92500
  gini_index: 0.4861
  vacancy_rate: 31.76
  race_white: 6085
  race_black: 360
  race_asian: 44
  race_native: 12
  hispanic: 1297
  bachelors_plus: 1163
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
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

# Coleman County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7833 |
| Under 18 | 1611 |
| 18–64 | 4169 |
| 65+ | 2053 |
| Median household income | 49159 |
| Poverty rate | 19.64 |
| Homeownership rate | 77.18 |
| Unemployment rate | 7.67 |
| Median home value | 92500 |
| Gini index | 0.4861 |
| Vacancy rate | 31.76 |
| White | 6085 |
| Black | 360 |
| Asian | 44 |
| Native | 12 |
| Hispanic/Latino | 1297 |
| Bachelor's or higher | 1163 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
