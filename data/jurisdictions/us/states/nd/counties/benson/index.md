---
type: Jurisdiction
title: "Benson County, ND"
classification: county
fips: "38005"
state: "ND"
demographics:
  population: 5808
  population_under_18: 1947
  population_18_64: 2939
  population_65_plus: 922
  median_household_income: 64033
  poverty_rate: 25.6
  homeownership_rate: 73.09
  unemployment_rate: 3.44
  median_home_value: 90000
  gini_index: 0.5229
  vacancy_rate: 20.15
  race_white: 2503
  race_black: 35
  race_asian: 48
  race_native: 2931
  hispanic: 113
  bachelors_plus: 960
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/9"
    rel: in-district
    area_weight: 0.6445
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 0.3554
  - to: "us/states/nd/districts/house/9"
    rel: in-district
    area_weight: 0.6445
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 0.3554
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Benson County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5808 |
| Under 18 | 1947 |
| 18–64 | 2939 |
| 65+ | 922 |
| Median household income | 64033 |
| Poverty rate | 25.6 |
| Homeownership rate | 73.09 |
| Unemployment rate | 3.44 |
| Median home value | 90000 |
| Gini index | 0.5229 |
| Vacancy rate | 20.15 |
| White | 2503 |
| Black | 35 |
| Asian | 48 |
| Native | 2931 |
| Hispanic/Latino | 113 |
| Bachelor's or higher | 960 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 9](/us/states/nd/districts/senate/9.md) — 64% (state senate)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 36% (state senate)
- [ND House District 9](/us/states/nd/districts/house/9.md) — 64% (state house)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
