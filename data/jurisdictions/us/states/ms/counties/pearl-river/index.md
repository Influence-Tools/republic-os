---
type: Jurisdiction
title: "Pearl River County, MS"
classification: county
fips: "28109"
state: "MS"
demographics:
  population: 57458
  population_under_18: 13147
  population_18_64: 33065
  population_65_plus: 11246
  median_household_income: 58135
  poverty_rate: 16.5
  homeownership_rate: 80.39
  unemployment_rate: 6.11
  median_home_value: 182300
  gini_index: 0.4505
  vacancy_rate: 14.0
  race_white: 45935
  race_black: 6888
  race_asian: 199
  race_native: 103
  hispanic: 2493
  bachelors_plus: 8526
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/ms/districts/senate/40"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/ms/districts/house/106"
    rel: in-district
    area_weight: 0.6008
  - to: "us/states/ms/districts/house/93"
    rel: in-district
    area_weight: 0.2326
  - to: "us/states/ms/districts/house/108"
    rel: in-district
    area_weight: 0.1648
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Pearl River County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57458 |
| Under 18 | 13147 |
| 18–64 | 33065 |
| 65+ | 11246 |
| Median household income | 58135 |
| Poverty rate | 16.5 |
| Homeownership rate | 80.39 |
| Unemployment rate | 6.11 |
| Median home value | 182300 |
| Gini index | 0.4505 |
| Vacancy rate | 14.0 |
| White | 45935 |
| Black | 6888 |
| Asian | 199 |
| Native | 103 |
| Hispanic/Latino | 2493 |
| Bachelor's or higher | 8526 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 40](/us/states/ms/districts/senate/40.md) — 100% (state senate)
- [MS House District 106](/us/states/ms/districts/house/106.md) — 60% (state house)
- [MS House District 93](/us/states/ms/districts/house/93.md) — 23% (state house)
- [MS House District 108](/us/states/ms/districts/house/108.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
