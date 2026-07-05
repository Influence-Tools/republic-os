---
type: Jurisdiction
title: "Decatur County, IA"
classification: county
fips: "19053"
state: "IA"
demographics:
  population: 7759
  population_under_18: 1721
  population_18_64: 4399
  population_65_plus: 1639
  median_household_income: 59044
  poverty_rate: 14.56
  homeownership_rate: 69.72
  unemployment_rate: 1.94
  median_home_value: 113900
  gini_index: 0.4289
  vacancy_rate: 16.51
  race_white: 7121
  race_black: 102
  race_asian: 56
  race_native: 16
  hispanic: 274
  bachelors_plus: 1661
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/24"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Decatur County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7759 |
| Under 18 | 1721 |
| 18–64 | 4399 |
| 65+ | 1639 |
| Median household income | 59044 |
| Poverty rate | 14.56 |
| Homeownership rate | 69.72 |
| Unemployment rate | 1.94 |
| Median home value | 113900 |
| Gini index | 0.4289 |
| Vacancy rate | 16.51 |
| White | 7121 |
| Black | 102 |
| Asian | 56 |
| Native | 16 |
| Hispanic/Latino | 274 |
| Bachelor's or higher | 1661 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 24](/us/states/ia/districts/house/24.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
