---
type: Jurisdiction
title: "Holmes County, MS"
classification: county
fips: "28051"
state: "MS"
demographics:
  population: 16191
  population_under_18: 3959
  population_18_64: 9517
  population_65_plus: 2715
  median_household_income: 32538
  poverty_rate: 36.36
  homeownership_rate: 61.02
  unemployment_rate: 9.54
  median_home_value: 80400
  gini_index: 0.5859
  vacancy_rate: 18.93
  race_white: 2368
  race_black: 13116
  race_asian: 46
  race_native: 19
  hispanic: 64
  bachelors_plus: 1977
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/47"
    rel: in-district
    area_weight: 0.681
  - to: "us/states/ms/districts/house/51"
    rel: in-district
    area_weight: 0.2053
  - to: "us/states/ms/districts/house/48"
    rel: in-district
    area_weight: 0.1137
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Holmes County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16191 |
| Under 18 | 3959 |
| 18–64 | 9517 |
| 65+ | 2715 |
| Median household income | 32538 |
| Poverty rate | 36.36 |
| Homeownership rate | 61.02 |
| Unemployment rate | 9.54 |
| Median home value | 80400 |
| Gini index | 0.5859 |
| Vacancy rate | 18.93 |
| White | 2368 |
| Black | 13116 |
| Asian | 46 |
| Native | 19 |
| Hispanic/Latino | 64 |
| Bachelor's or higher | 1977 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 21](/us/states/ms/districts/senate/21.md) — 100% (state senate)
- [MS House District 47](/us/states/ms/districts/house/47.md) — 68% (state house)
- [MS House District 51](/us/states/ms/districts/house/51.md) — 21% (state house)
- [MS House District 48](/us/states/ms/districts/house/48.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
