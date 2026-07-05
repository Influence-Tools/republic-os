---
type: Jurisdiction
title: "Claiborne Parish, LA"
classification: county
fips: "22027"
state: "LA"
demographics:
  population: 13833
  population_under_18: 2626
  population_18_64: 8154
  population_65_plus: 3053
  median_household_income: 32831
  poverty_rate: 31.98
  homeownership_rate: 68.83
  unemployment_rate: 5.11
  median_home_value: 82100
  gini_index: 0.5311
  vacancy_rate: 24.3
  race_white: 6155
  race_black: 6957
  race_asian: 15
  race_native: 8
  hispanic: 85
  bachelors_plus: 1490
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/11"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Claiborne Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13833 |
| Under 18 | 2626 |
| 18–64 | 8154 |
| 65+ | 3053 |
| Median household income | 32831 |
| Poverty rate | 31.98 |
| Homeownership rate | 68.83 |
| Unemployment rate | 5.11 |
| Median home value | 82100 |
| Gini index | 0.5311 |
| Vacancy rate | 24.3 |
| White | 6155 |
| Black | 6957 |
| Asian | 15 |
| Native | 8 |
| Hispanic/Latino | 85 |
| Bachelor's or higher | 1490 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 100% (state senate)
- [LA House District 11](/us/states/la/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
