---
type: Jurisdiction
title: "Louisa County, IA"
classification: county
fips: "19115"
state: "IA"
demographics:
  population: 10678
  population_under_18: 2347
  population_18_64: 6185
  population_65_plus: 2146
  median_household_income: 77354
  poverty_rate: 9.77
  homeownership_rate: 80.27
  unemployment_rate: 2.97
  median_home_value: 150100
  gini_index: 0.4027
  vacancy_rate: 10.59
  race_white: 8429
  race_black: 110
  race_asian: 231
  race_native: 67
  hispanic: 1754
  bachelors_plus: 1487
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/48"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/95"
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

# Louisa County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10678 |
| Under 18 | 2347 |
| 18–64 | 6185 |
| 65+ | 2146 |
| Median household income | 77354 |
| Poverty rate | 9.77 |
| Homeownership rate | 80.27 |
| Unemployment rate | 2.97 |
| Median home value | 150100 |
| Gini index | 0.4027 |
| Vacancy rate | 10.59 |
| White | 8429 |
| Black | 110 |
| Asian | 231 |
| Native | 67 |
| Hispanic/Latino | 1754 |
| Bachelor's or higher | 1487 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 48](/us/states/ia/districts/senate/48.md) — 100% (state senate)
- [IA House District 95](/us/states/ia/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
