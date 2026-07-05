---
type: Jurisdiction
title: "Chickasaw County, MS"
classification: county
fips: "28017"
state: "MS"
demographics:
  population: 16915
  population_under_18: 4197
  population_18_64: 9565
  population_65_plus: 3153
  median_household_income: 43586
  poverty_rate: 23.55
  homeownership_rate: 70.3
  unemployment_rate: 4.86
  median_home_value: 109800
  gini_index: 0.4716
  vacancy_rate: 14.99
  race_white: 8366
  race_black: 8100
  race_asian: 61
  race_native: 7
  hispanic: 189
  bachelors_plus: 1854
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/22"
    rel: in-district
    area_weight: 0.7699
  - to: "us/states/ms/districts/house/16"
    rel: in-district
    area_weight: 0.1567
  - to: "us/states/ms/districts/house/36"
    rel: in-district
    area_weight: 0.0733
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Chickasaw County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16915 |
| Under 18 | 4197 |
| 18–64 | 9565 |
| 65+ | 3153 |
| Median household income | 43586 |
| Poverty rate | 23.55 |
| Homeownership rate | 70.3 |
| Unemployment rate | 4.86 |
| Median home value | 109800 |
| Gini index | 0.4716 |
| Vacancy rate | 14.99 |
| White | 8366 |
| Black | 8100 |
| Asian | 61 |
| Native | 7 |
| Hispanic/Latino | 189 |
| Bachelor's or higher | 1854 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 8](/us/states/ms/districts/senate/8.md) — 100% (state senate)
- [MS House District 22](/us/states/ms/districts/house/22.md) — 77% (state house)
- [MS House District 16](/us/states/ms/districts/house/16.md) — 16% (state house)
- [MS House District 36](/us/states/ms/districts/house/36.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
