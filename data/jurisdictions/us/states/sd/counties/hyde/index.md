---
type: Jurisdiction
title: "Hyde County, SD"
classification: county
fips: "46069"
state: "SD"
demographics:
  population: 1191
  population_under_18: 214
  population_18_64: 640
  population_65_plus: 337
  median_household_income: 73472
  poverty_rate: 5.65
  homeownership_rate: 83.5
  unemployment_rate: 3.72
  median_home_value: 181600
  gini_index: 0.3946
  vacancy_rate: 18.48
  race_white: 1025
  race_black: 3
  race_asian: 0
  race_native: 11
  hispanic: 19
  bachelors_plus: 204
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/24"
    rel: in-district
    area_weight: 0.9025
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.0975
  - to: "us/states/sd/districts/house/24"
    rel: in-district
    area_weight: 0.9025
  - to: "us/states/sd/districts/house/26b"
    rel: in-district
    area_weight: 0.0975
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Hyde County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1191 |
| Under 18 | 214 |
| 18–64 | 640 |
| 65+ | 337 |
| Median household income | 73472 |
| Poverty rate | 5.65 |
| Homeownership rate | 83.5 |
| Unemployment rate | 3.72 |
| Median home value | 181600 |
| Gini index | 0.3946 |
| Vacancy rate | 18.48 |
| White | 1025 |
| Black | 3 |
| Asian | 0 |
| Native | 11 |
| Hispanic/Latino | 19 |
| Bachelor's or higher | 204 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 24](/us/states/sd/districts/senate/24.md) — 90% (state senate)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 10% (state senate)
- [SD House District 24](/us/states/sd/districts/house/24.md) — 90% (state house)
- [SD House District 26B](/us/states/sd/districts/house/26b.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
