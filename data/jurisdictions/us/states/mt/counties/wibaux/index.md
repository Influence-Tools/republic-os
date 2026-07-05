---
type: Jurisdiction
title: "Wibaux County, MT"
classification: county
fips: "30109"
state: "MT"
demographics:
  population: 1193
  population_under_18: 356
  population_18_64: 593
  population_65_plus: 244
  median_household_income: 67462
  poverty_rate: 15.81
  homeownership_rate: 72.45
  unemployment_rate: 1.71
  median_home_value: 98600
  gini_index: 0.4076
  vacancy_rate: 22.52
  race_white: 1100
  race_black: 7
  race_asian: 1
  race_native: 0
  hispanic: 92
  bachelors_plus: 218
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Wibaux County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1193 |
| Under 18 | 356 |
| 18–64 | 593 |
| 65+ | 244 |
| Median household income | 67462 |
| Poverty rate | 15.81 |
| Homeownership rate | 72.45 |
| Unemployment rate | 1.71 |
| Median home value | 98600 |
| Gini index | 0.4076 |
| Vacancy rate | 22.52 |
| White | 1100 |
| Black | 7 |
| Asian | 1 |
| Native | 0 |
| Hispanic/Latino | 92 |
| Bachelor's or higher | 218 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
