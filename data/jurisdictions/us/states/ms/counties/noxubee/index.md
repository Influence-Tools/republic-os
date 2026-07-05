---
type: Jurisdiction
title: "Noxubee County, MS"
classification: county
fips: "28103"
state: "MS"
demographics:
  population: 10025
  population_under_18: 2519
  population_18_64: 5683
  population_65_plus: 1823
  median_household_income: 33833
  poverty_rate: 26.33
  homeownership_rate: 73.01
  unemployment_rate: 8.62
  median_home_value: 90800
  gini_index: 0.5437
  vacancy_rate: 16.54
  race_white: 2552
  race_black: 7374
  race_asian: 8
  race_native: 14
  hispanic: 38
  bachelors_plus: 1037
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/32"
    rel: in-district
    area_weight: 0.5372
  - to: "us/states/ms/districts/senate/16"
    rel: in-district
    area_weight: 0.4628
  - to: "us/states/ms/districts/house/42"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Noxubee County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10025 |
| Under 18 | 2519 |
| 18–64 | 5683 |
| 65+ | 1823 |
| Median household income | 33833 |
| Poverty rate | 26.33 |
| Homeownership rate | 73.01 |
| Unemployment rate | 8.62 |
| Median home value | 90800 |
| Gini index | 0.5437 |
| Vacancy rate | 16.54 |
| White | 2552 |
| Black | 7374 |
| Asian | 8 |
| Native | 14 |
| Hispanic/Latino | 38 |
| Bachelor's or higher | 1037 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 32](/us/states/ms/districts/senate/32.md) — 54% (state senate)
- [MS Senate District 16](/us/states/ms/districts/senate/16.md) — 46% (state senate)
- [MS House District 42](/us/states/ms/districts/house/42.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
