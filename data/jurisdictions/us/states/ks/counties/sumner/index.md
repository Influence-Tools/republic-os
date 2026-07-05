---
type: Jurisdiction
title: "Sumner County, KS"
classification: county
fips: "20191"
state: "KS"
demographics:
  population: 22353
  population_under_18: 5383
  population_18_64: 12603
  population_65_plus: 4367
  median_household_income: 63951
  poverty_rate: 10.64
  homeownership_rate: 75.06
  unemployment_rate: 5.94
  median_home_value: 135100
  gini_index: 0.4242
  vacancy_rate: 13.87
  race_white: 20007
  race_black: 246
  race_asian: 85
  race_native: 278
  hispanic: 1366
  bachelors_plus: 5123
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/32"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/ks/districts/house/79"
    rel: in-district
    area_weight: 0.3834
  - to: "us/states/ks/districts/house/80"
    rel: in-district
    area_weight: 0.3244
  - to: "us/states/ks/districts/house/116"
    rel: in-district
    area_weight: 0.2829
  - to: "us/states/ks/districts/house/82"
    rel: in-district
    area_weight: 0.0091
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Sumner County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22353 |
| Under 18 | 5383 |
| 18–64 | 12603 |
| 65+ | 4367 |
| Median household income | 63951 |
| Poverty rate | 10.64 |
| Homeownership rate | 75.06 |
| Unemployment rate | 5.94 |
| Median home value | 135100 |
| Gini index | 0.4242 |
| Vacancy rate | 13.87 |
| White | 20007 |
| Black | 246 |
| Asian | 85 |
| Native | 278 |
| Hispanic/Latino | 1366 |
| Bachelor's or higher | 5123 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 32](/us/states/ks/districts/senate/32.md) — 100% (state senate)
- [KS House District 79](/us/states/ks/districts/house/79.md) — 38% (state house)
- [KS House District 80](/us/states/ks/districts/house/80.md) — 32% (state house)
- [KS House District 116](/us/states/ks/districts/house/116.md) — 28% (state house)
- [KS House District 82](/us/states/ks/districts/house/82.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
