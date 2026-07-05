---
type: Jurisdiction
title: "Todd County, SD"
classification: county
fips: "46121"
state: "SD"
demographics:
  population: 9244
  population_under_18: 3945
  population_18_64: 2990
  population_65_plus: 2309
  median_household_income: 42075
  poverty_rate: 48.43
  homeownership_rate: 46.34
  unemployment_rate: 18.66
  median_home_value: 53900
  gini_index: 0.5085
  vacancy_rate: 11.64
  race_white: 747
  race_black: 41
  race_asian: 287
  race_native: 7739
  hispanic: 224
  bachelors_plus: 1006
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/26a"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Todd County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9244 |
| Under 18 | 3945 |
| 18–64 | 2990 |
| 65+ | 2309 |
| Median household income | 42075 |
| Poverty rate | 48.43 |
| Homeownership rate | 46.34 |
| Unemployment rate | 18.66 |
| Median home value | 53900 |
| Gini index | 0.5085 |
| Vacancy rate | 11.64 |
| White | 747 |
| Black | 41 |
| Asian | 287 |
| Native | 7739 |
| Hispanic/Latino | 224 |
| Bachelor's or higher | 1006 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 26](/us/states/sd/districts/senate/26.md) — 100% (state senate)
- [SD House District 26A](/us/states/sd/districts/house/26a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
