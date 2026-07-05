---
type: Jurisdiction
title: "Stewart County, TN"
classification: county
fips: "47161"
state: "TN"
demographics:
  population: 14027
  population_under_18: 2922
  population_18_64: 8172
  population_65_plus: 2933
  median_household_income: 63114
  poverty_rate: 16.42
  homeownership_rate: 81.06
  unemployment_rate: 2.73
  median_home_value: 204700
  gini_index: 0.4352
  vacancy_rate: 20.77
  race_white: 12914
  race_black: 196
  race_asian: 114
  race_native: 14
  hispanic: 425
  bachelors_plus: 2371
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/74"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Stewart County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14027 |
| Under 18 | 2922 |
| 18–64 | 8172 |
| 65+ | 2933 |
| Median household income | 63114 |
| Poverty rate | 16.42 |
| Homeownership rate | 81.06 |
| Unemployment rate | 2.73 |
| Median home value | 204700 |
| Gini index | 0.4352 |
| Vacancy rate | 20.77 |
| White | 12914 |
| Black | 196 |
| Asian | 114 |
| Native | 14 |
| Hispanic/Latino | 425 |
| Bachelor's or higher | 2371 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 74](/us/states/tn/districts/house/74.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
