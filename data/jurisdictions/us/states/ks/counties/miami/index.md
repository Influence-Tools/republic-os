---
type: Jurisdiction
title: "Miami County, KS"
classification: county
fips: "20121"
state: "KS"
demographics:
  population: 34938
  population_under_18: 8228
  population_18_64: 20387
  population_65_plus: 6323
  median_household_income: 89000
  poverty_rate: 7.9
  homeownership_rate: 78.21
  unemployment_rate: 3.69
  median_home_value: 287700
  gini_index: 0.4096
  vacancy_rate: 3.67
  race_white: 31547
  race_black: 442
  race_asian: 51
  race_native: 218
  hispanic: 1423
  bachelors_plus: 9928
districts:
  - to: "us/states/ks/districts/03"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.5721
  - to: "us/states/ks/districts/senate/37"
    rel: in-district
    area_weight: 0.4151
  - to: "us/states/ks/districts/senate/23"
    rel: in-district
    area_weight: 0.0124
  - to: "us/states/ks/districts/house/6"
    rel: in-district
    area_weight: 0.4936
  - to: "us/states/ks/districts/house/5"
    rel: in-district
    area_weight: 0.2643
  - to: "us/states/ks/districts/house/9"
    rel: in-district
    area_weight: 0.2396
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Miami County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34938 |
| Under 18 | 8228 |
| 18–64 | 20387 |
| 65+ | 6323 |
| Median household income | 89000 |
| Poverty rate | 7.9 |
| Homeownership rate | 78.21 |
| Unemployment rate | 3.69 |
| Median home value | 287700 |
| Gini index | 0.4096 |
| Vacancy rate | 3.67 |
| White | 31547 |
| Black | 442 |
| Asian | 51 |
| Native | 218 |
| Hispanic/Latino | 1423 |
| Bachelor's or higher | 9928 |

## Districts

- [KS-03](/us/states/ks/districts/03.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 57% (state senate)
- [KS Senate District 37](/us/states/ks/districts/senate/37.md) — 42% (state senate)
- [KS Senate District 23](/us/states/ks/districts/senate/23.md) — 1% (state senate)
- [KS House District 6](/us/states/ks/districts/house/6.md) — 49% (state house)
- [KS House District 5](/us/states/ks/districts/house/5.md) — 26% (state house)
- [KS House District 9](/us/states/ks/districts/house/9.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
