---
type: Jurisdiction
title: "Pierce County, ND"
classification: county
fips: "38069"
state: "ND"
demographics:
  population: 3928
  population_under_18: 820
  population_18_64: 2070
  population_65_plus: 1038
  median_household_income: 59365
  poverty_rate: 10.8
  homeownership_rate: 81.55
  unemployment_rate: 1.08
  median_home_value: 147300
  gini_index: 0.4574
  vacancy_rate: 9.21
  race_white: 3571
  race_black: 11
  race_asian: 17
  race_native: 167
  hispanic: 32
  bachelors_plus: 991
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 0.9097
  - to: "us/states/nd/districts/senate/9"
    rel: in-district
    area_weight: 0.0902
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 0.9097
  - to: "us/states/nd/districts/house/9"
    rel: in-district
    area_weight: 0.0902
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Pierce County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3928 |
| Under 18 | 820 |
| 18–64 | 2070 |
| 65+ | 1038 |
| Median household income | 59365 |
| Poverty rate | 10.8 |
| Homeownership rate | 81.55 |
| Unemployment rate | 1.08 |
| Median home value | 147300 |
| Gini index | 0.4574 |
| Vacancy rate | 9.21 |
| White | 3571 |
| Black | 11 |
| Asian | 17 |
| Native | 167 |
| Hispanic/Latino | 32 |
| Bachelor's or higher | 991 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 91% (state senate)
- [ND Senate District 9](/us/states/nd/districts/senate/9.md) — 9% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 91% (state house)
- [ND House District 9](/us/states/nd/districts/house/9.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
