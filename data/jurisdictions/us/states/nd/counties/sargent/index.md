---
type: Jurisdiction
title: "Sargent County, ND"
classification: county
fips: "38081"
state: "ND"
demographics:
  population: 3804
  population_under_18: 776
  population_18_64: 2120
  population_65_plus: 908
  median_household_income: 77946
  poverty_rate: 6.88
  homeownership_rate: 72.47
  unemployment_rate: 0.77
  median_home_value: 163200
  gini_index: 0.4372
  vacancy_rate: 12.27
  race_white: 3429
  race_black: 120
  race_asian: 11
  race_native: 10
  hispanic: 110
  bachelors_plus: 650
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/28"
    rel: in-district
    area_weight: 0.9236
  - to: "us/states/nd/districts/senate/25"
    rel: in-district
    area_weight: 0.0763
  - to: "us/states/nd/districts/house/28"
    rel: in-district
    area_weight: 0.9236
  - to: "us/states/nd/districts/house/25"
    rel: in-district
    area_weight: 0.0763
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Sargent County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3804 |
| Under 18 | 776 |
| 18–64 | 2120 |
| 65+ | 908 |
| Median household income | 77946 |
| Poverty rate | 6.88 |
| Homeownership rate | 72.47 |
| Unemployment rate | 0.77 |
| Median home value | 163200 |
| Gini index | 0.4372 |
| Vacancy rate | 12.27 |
| White | 3429 |
| Black | 120 |
| Asian | 11 |
| Native | 10 |
| Hispanic/Latino | 110 |
| Bachelor's or higher | 650 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 28](/us/states/nd/districts/senate/28.md) — 92% (state senate)
- [ND Senate District 25](/us/states/nd/districts/senate/25.md) — 8% (state senate)
- [ND House District 28](/us/states/nd/districts/house/28.md) — 92% (state house)
- [ND House District 25](/us/states/nd/districts/house/25.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
