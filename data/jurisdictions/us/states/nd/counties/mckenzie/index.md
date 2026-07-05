---
type: Jurisdiction
title: "McKenzie County, ND"
classification: county
fips: "38053"
state: "ND"
demographics:
  population: 14321
  population_under_18: 4450
  population_18_64: 8535
  population_65_plus: 1336
  median_household_income: 93404
  poverty_rate: 11.96
  homeownership_rate: 53.39
  unemployment_rate: 1.27
  median_home_value: 349600
  gini_index: 0.4525
  vacancy_rate: 22.64
  race_white: 11191
  race_black: 276
  race_asian: 162
  race_native: 1180
  hispanic: 1729
  bachelors_plus: 2056
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/26"
    rel: in-district
    area_weight: 0.9433
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.0566
  - to: "us/states/nd/districts/house/26"
    rel: in-district
    area_weight: 0.9433
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.0566
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# McKenzie County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14321 |
| Under 18 | 4450 |
| 18–64 | 8535 |
| 65+ | 1336 |
| Median household income | 93404 |
| Poverty rate | 11.96 |
| Homeownership rate | 53.39 |
| Unemployment rate | 1.27 |
| Median home value | 349600 |
| Gini index | 0.4525 |
| Vacancy rate | 22.64 |
| White | 11191 |
| Black | 276 |
| Asian | 162 |
| Native | 1180 |
| Hispanic/Latino | 1729 |
| Bachelor's or higher | 2056 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 26](/us/states/nd/districts/senate/26.md) — 94% (state senate)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 6% (state senate)
- [ND House District 26](/us/states/nd/districts/house/26.md) — 94% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
