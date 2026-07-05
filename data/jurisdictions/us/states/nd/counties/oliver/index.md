---
type: Jurisdiction
title: "Oliver County, ND"
classification: county
fips: "38065"
state: "ND"
demographics:
  population: 1839
  population_under_18: 476
  population_18_64: 862
  population_65_plus: 501
  median_household_income: 77240
  poverty_rate: 5.22
  homeownership_rate: 95.17
  unemployment_rate: 1.0
  median_home_value: 215700
  gini_index: 0.4049
  vacancy_rate: 18.81
  race_white: 1820
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 18
  bachelors_plus: 361
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/33"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Oliver County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1839 |
| Under 18 | 476 |
| 18–64 | 862 |
| 65+ | 501 |
| Median household income | 77240 |
| Poverty rate | 5.22 |
| Homeownership rate | 95.17 |
| Unemployment rate | 1.0 |
| Median home value | 215700 |
| Gini index | 0.4049 |
| Vacancy rate | 18.81 |
| White | 1820 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 18 |
| Bachelor's or higher | 361 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 33](/us/states/nd/districts/senate/33.md) — 100% (state senate)
- [ND House District 33](/us/states/nd/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
