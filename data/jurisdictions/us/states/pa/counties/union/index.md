---
type: Jurisdiction
title: "Union County, PA"
classification: county
fips: "42119"
state: "PA"
demographics:
  population: 42456
  population_under_18: 7370
  population_18_64: 26647
  population_65_plus: 8439
  median_household_income: 76404
  poverty_rate: 8.96
  homeownership_rate: 72.32
  unemployment_rate: 2.17
  median_home_value: 240100
  gini_index: 0.4736
  vacancy_rate: 10.24
  race_white: 37633
  race_black: 2526
  race_asian: 846
  race_native: 58
  hispanic: 2147
  bachelors_plus: 11230
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/pa/districts/senate/23"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/pa/districts/house/76"
    rel: in-district
    area_weight: 0.7225
  - to: "us/states/pa/districts/house/83"
    rel: in-district
    area_weight: 0.1939
  - to: "us/states/pa/districts/house/85"
    rel: in-district
    area_weight: 0.0833
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Union County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42456 |
| Under 18 | 7370 |
| 18–64 | 26647 |
| 65+ | 8439 |
| Median household income | 76404 |
| Poverty rate | 8.96 |
| Homeownership rate | 72.32 |
| Unemployment rate | 2.17 |
| Median home value | 240100 |
| Gini index | 0.4736 |
| Vacancy rate | 10.24 |
| White | 37633 |
| Black | 2526 |
| Asian | 846 |
| Native | 58 |
| Hispanic/Latino | 2147 |
| Bachelor's or higher | 11230 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 23](/us/states/pa/districts/senate/23.md) — 100% (state senate)
- [PA House District 76](/us/states/pa/districts/house/76.md) — 72% (state house)
- [PA House District 83](/us/states/pa/districts/house/83.md) — 19% (state house)
- [PA House District 85](/us/states/pa/districts/house/85.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
