---
type: Jurisdiction
title: "Mills County, IA"
classification: county
fips: "19129"
state: "IA"
demographics:
  population: 14568
  population_under_18: 3326
  population_18_64: 8321
  population_65_plus: 2921
  median_household_income: 90753
  poverty_rate: 8.22
  homeownership_rate: 83.54
  unemployment_rate: 1.98
  median_home_value: 237800
  gini_index: 0.4137
  vacancy_rate: 12.06
  race_white: 13605
  race_black: 59
  race_asian: 82
  race_native: 16
  hispanic: 563
  bachelors_plus: 4156
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ia/districts/senate/8"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ia/districts/house/16"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Mills County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14568 |
| Under 18 | 3326 |
| 18–64 | 8321 |
| 65+ | 2921 |
| Median household income | 90753 |
| Poverty rate | 8.22 |
| Homeownership rate | 83.54 |
| Unemployment rate | 1.98 |
| Median home value | 237800 |
| Gini index | 0.4137 |
| Vacancy rate | 12.06 |
| White | 13605 |
| Black | 59 |
| Asian | 82 |
| Native | 16 |
| Hispanic/Latino | 563 |
| Bachelor's or higher | 4156 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 8](/us/states/ia/districts/senate/8.md) — 100% (state senate)
- [IA House District 16](/us/states/ia/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
