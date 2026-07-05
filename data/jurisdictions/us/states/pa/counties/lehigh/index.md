---
type: Jurisdiction
title: "Lehigh County, PA"
classification: county
fips: "42077"
state: "PA"
demographics:
  population: 378792
  population_under_18: 84498
  population_18_64: 227286
  population_65_plus: 67008
  median_household_income: 80079
  poverty_rate: 11.57
  homeownership_rate: 65.57
  unemployment_rate: 5.88
  median_home_value: 300400
  gini_index: 0.4653
  vacancy_rate: 4.52
  race_white: 236150
  race_black: 24476
  race_asian: 13517
  race_native: 1801
  hispanic: 105976
  bachelors_plus: 123421
districts:
  - to: "us/states/pa/districts/07"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/pa/districts/senate/16"
    rel: in-district
    area_weight: 0.8272
  - to: "us/states/pa/districts/senate/14"
    rel: in-district
    area_weight: 0.1598
  - to: "us/states/pa/districts/senate/18"
    rel: in-district
    area_weight: 0.0126
  - to: "us/states/pa/districts/house/187"
    rel: in-district
    area_weight: 0.4424
  - to: "us/states/pa/districts/house/131"
    rel: in-district
    area_weight: 0.1881
  - to: "us/states/pa/districts/house/183"
    rel: in-district
    area_weight: 0.1266
  - to: "us/states/pa/districts/house/132"
    rel: in-district
    area_weight: 0.1001
  - to: "us/states/pa/districts/house/133"
    rel: in-district
    area_weight: 0.0695
  - to: "us/states/pa/districts/house/134"
    rel: in-district
    area_weight: 0.0383
  - to: "us/states/pa/districts/house/22"
    rel: in-district
    area_weight: 0.0348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Lehigh County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 378792 |
| Under 18 | 84498 |
| 18–64 | 227286 |
| 65+ | 67008 |
| Median household income | 80079 |
| Poverty rate | 11.57 |
| Homeownership rate | 65.57 |
| Unemployment rate | 5.88 |
| Median home value | 300400 |
| Gini index | 0.4653 |
| Vacancy rate | 4.52 |
| White | 236150 |
| Black | 24476 |
| Asian | 13517 |
| Native | 1801 |
| Hispanic/Latino | 105976 |
| Bachelor's or higher | 123421 |

## Districts

- [PA-07](/us/states/pa/districts/07.md) — 100% (congressional)
- [PA Senate District 16](/us/states/pa/districts/senate/16.md) — 83% (state senate)
- [PA Senate District 14](/us/states/pa/districts/senate/14.md) — 16% (state senate)
- [PA Senate District 18](/us/states/pa/districts/senate/18.md) — 1% (state senate)
- [PA House District 187](/us/states/pa/districts/house/187.md) — 44% (state house)
- [PA House District 131](/us/states/pa/districts/house/131.md) — 19% (state house)
- [PA House District 183](/us/states/pa/districts/house/183.md) — 13% (state house)
- [PA House District 132](/us/states/pa/districts/house/132.md) — 10% (state house)
- [PA House District 133](/us/states/pa/districts/house/133.md) — 7% (state house)
- [PA House District 134](/us/states/pa/districts/house/134.md) — 4% (state house)
- [PA House District 22](/us/states/pa/districts/house/22.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
