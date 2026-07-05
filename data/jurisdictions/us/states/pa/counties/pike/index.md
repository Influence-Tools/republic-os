---
type: Jurisdiction
title: "Pike County, PA"
classification: county
fips: "42103"
state: "PA"
demographics:
  population: 60621
  population_under_18: 10433
  population_18_64: 35456
  population_65_plus: 14732
  median_household_income: 81323
  poverty_rate: 9.81
  homeownership_rate: 87.03
  unemployment_rate: 7.47
  median_home_value: 272600
  gini_index: 0.4293
  vacancy_rate: 39.61
  race_white: 47981
  race_black: 3660
  race_asian: 829
  race_native: 60
  hispanic: 7537
  bachelors_plus: 19199
districts:
  - to: "us/states/pa/districts/08"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/pa/districts/senate/20"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/pa/districts/house/139"
    rel: in-district
    area_weight: 0.7244
  - to: "us/states/pa/districts/house/189"
    rel: in-district
    area_weight: 0.2751
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Pike County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 60621 |
| Under 18 | 10433 |
| 18–64 | 35456 |
| 65+ | 14732 |
| Median household income | 81323 |
| Poverty rate | 9.81 |
| Homeownership rate | 87.03 |
| Unemployment rate | 7.47 |
| Median home value | 272600 |
| Gini index | 0.4293 |
| Vacancy rate | 39.61 |
| White | 47981 |
| Black | 3660 |
| Asian | 829 |
| Native | 60 |
| Hispanic/Latino | 7537 |
| Bachelor's or higher | 19199 |

## Districts

- [PA-08](/us/states/pa/districts/08.md) — 100% (congressional)
- [PA Senate District 20](/us/states/pa/districts/senate/20.md) — 100% (state senate)
- [PA House District 139](/us/states/pa/districts/house/139.md) — 72% (state house)
- [PA House District 189](/us/states/pa/districts/house/189.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
