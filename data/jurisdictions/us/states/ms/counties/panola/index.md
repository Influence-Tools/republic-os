---
type: Jurisdiction
title: "Panola County, MS"
classification: county
fips: "28107"
state: "MS"
demographics:
  population: 32808
  population_under_18: 8094
  population_18_64: 18988
  population_65_plus: 5726
  median_household_income: 45945
  poverty_rate: 23.33
  homeownership_rate: 71.1
  unemployment_rate: 6.6
  median_home_value: 127800
  gini_index: 0.4844
  vacancy_rate: 16.34
  race_white: 15293
  race_black: 15844
  race_asian: 164
  race_native: 11
  hispanic: 686
  bachelors_plus: 5426
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ms/districts/senate/24"
    rel: in-district
    area_weight: 0.8343
  - to: "us/states/ms/districts/senate/9"
    rel: in-district
    area_weight: 0.1656
  - to: "us/states/ms/districts/house/11"
    rel: in-district
    area_weight: 0.6811
  - to: "us/states/ms/districts/house/10"
    rel: in-district
    area_weight: 0.3185
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Panola County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32808 |
| Under 18 | 8094 |
| 18–64 | 18988 |
| 65+ | 5726 |
| Median household income | 45945 |
| Poverty rate | 23.33 |
| Homeownership rate | 71.1 |
| Unemployment rate | 6.6 |
| Median home value | 127800 |
| Gini index | 0.4844 |
| Vacancy rate | 16.34 |
| White | 15293 |
| Black | 15844 |
| Asian | 164 |
| Native | 11 |
| Hispanic/Latino | 686 |
| Bachelor's or higher | 5426 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 24](/us/states/ms/districts/senate/24.md) — 83% (state senate)
- [MS Senate District 9](/us/states/ms/districts/senate/9.md) — 17% (state senate)
- [MS House District 11](/us/states/ms/districts/house/11.md) — 68% (state house)
- [MS House District 10](/us/states/ms/districts/house/10.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
