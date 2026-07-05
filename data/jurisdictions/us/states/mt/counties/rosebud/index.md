---
type: Jurisdiction
title: "Rosebud County, MT"
classification: county
fips: "30087"
state: "MT"
demographics:
  population: 8165
  population_under_18: 2308
  population_18_64: 4424
  population_65_plus: 1433
  median_household_income: 49914
  poverty_rate: 24.45
  homeownership_rate: 63.65
  unemployment_rate: 10.59
  median_home_value: 182400
  gini_index: 0.4921
  vacancy_rate: 18.76
  race_white: 4365
  race_black: 5
  race_asian: 186
  race_native: 3016
  hispanic: 299
  bachelors_plus: 1413
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/18"
    rel: in-district
    area_weight: 0.82
  - to: "us/states/mt/districts/senate/21"
    rel: in-district
    area_weight: 0.1799
  - to: "us/states/mt/districts/house/35"
    rel: in-district
    area_weight: 0.82
  - to: "us/states/mt/districts/house/41"
    rel: in-district
    area_weight: 0.1799
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Rosebud County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8165 |
| Under 18 | 2308 |
| 18–64 | 4424 |
| 65+ | 1433 |
| Median household income | 49914 |
| Poverty rate | 24.45 |
| Homeownership rate | 63.65 |
| Unemployment rate | 10.59 |
| Median home value | 182400 |
| Gini index | 0.4921 |
| Vacancy rate | 18.76 |
| White | 4365 |
| Black | 5 |
| Asian | 186 |
| Native | 3016 |
| Hispanic/Latino | 299 |
| Bachelor's or higher | 1413 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 18](/us/states/mt/districts/senate/18.md) — 82% (state senate)
- [MT Senate District 21](/us/states/mt/districts/senate/21.md) — 18% (state senate)
- [MT House District 35](/us/states/mt/districts/house/35.md) — 82% (state house)
- [MT House District 41](/us/states/mt/districts/house/41.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
