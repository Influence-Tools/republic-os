---
type: Jurisdiction
title: "Boone County, IA"
classification: county
fips: "19015"
state: "IA"
demographics:
  population: 26668
  population_under_18: 5612
  population_18_64: 15732
  population_65_plus: 5324
  median_household_income: 83531
  poverty_rate: 6.16
  homeownership_rate: 80.0
  unemployment_rate: 1.51
  median_home_value: 212400
  gini_index: 0.3997
  vacancy_rate: 9.18
  race_white: 25099
  race_black: 307
  race_asian: 53
  race_native: 11
  hispanic: 783
  bachelors_plus: 7262
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/48"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Boone County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26668 |
| Under 18 | 5612 |
| 18–64 | 15732 |
| 65+ | 5324 |
| Median household income | 83531 |
| Poverty rate | 6.16 |
| Homeownership rate | 80.0 |
| Unemployment rate | 1.51 |
| Median home value | 212400 |
| Gini index | 0.3997 |
| Vacancy rate | 9.18 |
| White | 25099 |
| Black | 307 |
| Asian | 53 |
| Native | 11 |
| Hispanic/Latino | 783 |
| Bachelor's or higher | 7262 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 24](/us/states/ia/districts/senate/24.md) — 100% (state senate)
- [IA House District 48](/us/states/ia/districts/house/48.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
