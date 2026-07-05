---
type: Jurisdiction
title: "Kingfisher County, OK"
classification: county
fips: "40073"
state: "OK"
demographics:
  population: 15430
  population_under_18: 4120
  population_18_64: 8661
  population_65_plus: 2649
  median_household_income: 71975
  poverty_rate: 12.84
  homeownership_rate: 74.51
  unemployment_rate: 2.11
  median_home_value: 215800
  gini_index: 0.4448
  vacancy_rate: 12.01
  race_white: 11705
  race_black: 73
  race_asian: 86
  race_native: 576
  hispanic: 2863
  bachelors_plus: 3133
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/26"
    rel: in-district
    area_weight: 0.7085
  - to: "us/states/ok/districts/senate/20"
    rel: in-district
    area_weight: 0.2915
  - to: "us/states/ok/districts/house/59"
    rel: in-district
    area_weight: 0.9473
  - to: "us/states/ok/districts/house/41"
    rel: in-district
    area_weight: 0.0526
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Kingfisher County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15430 |
| Under 18 | 4120 |
| 18–64 | 8661 |
| 65+ | 2649 |
| Median household income | 71975 |
| Poverty rate | 12.84 |
| Homeownership rate | 74.51 |
| Unemployment rate | 2.11 |
| Median home value | 215800 |
| Gini index | 0.4448 |
| Vacancy rate | 12.01 |
| White | 11705 |
| Black | 73 |
| Asian | 86 |
| Native | 576 |
| Hispanic/Latino | 2863 |
| Bachelor's or higher | 3133 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 26](/us/states/ok/districts/senate/26.md) — 71% (state senate)
- [OK Senate District 20](/us/states/ok/districts/senate/20.md) — 29% (state senate)
- [OK House District 59](/us/states/ok/districts/house/59.md) — 95% (state house)
- [OK House District 41](/us/states/ok/districts/house/41.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
