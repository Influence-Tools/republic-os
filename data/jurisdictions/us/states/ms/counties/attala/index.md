---
type: Jurisdiction
title: "Attala County, MS"
classification: county
fips: "28007"
state: "MS"
demographics:
  population: 17526
  population_under_18: 4417
  population_18_64: 9697
  population_65_plus: 3412
  median_household_income: 51639
  poverty_rate: 18.0
  homeownership_rate: 75.28
  unemployment_rate: 5.42
  median_home_value: 104600
  gini_index: 0.5128
  vacancy_rate: 20.56
  race_white: 9106
  race_black: 7741
  race_asian: 44
  race_native: 5
  hispanic: 377
  bachelors_plus: 3142
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/14"
    rel: in-district
    area_weight: 0.6406
  - to: "us/states/ms/districts/senate/21"
    rel: in-district
    area_weight: 0.3593
  - to: "us/states/ms/districts/house/48"
    rel: in-district
    area_weight: 0.7839
  - to: "us/states/ms/districts/house/27"
    rel: in-district
    area_weight: 0.1367
  - to: "us/states/ms/districts/house/47"
    rel: in-district
    area_weight: 0.0793
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Attala County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17526 |
| Under 18 | 4417 |
| 18–64 | 9697 |
| 65+ | 3412 |
| Median household income | 51639 |
| Poverty rate | 18.0 |
| Homeownership rate | 75.28 |
| Unemployment rate | 5.42 |
| Median home value | 104600 |
| Gini index | 0.5128 |
| Vacancy rate | 20.56 |
| White | 9106 |
| Black | 7741 |
| Asian | 44 |
| Native | 5 |
| Hispanic/Latino | 377 |
| Bachelor's or higher | 3142 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 14](/us/states/ms/districts/senate/14.md) — 64% (state senate)
- [MS Senate District 21](/us/states/ms/districts/senate/21.md) — 36% (state senate)
- [MS House District 48](/us/states/ms/districts/house/48.md) — 78% (state house)
- [MS House District 27](/us/states/ms/districts/house/27.md) — 14% (state house)
- [MS House District 47](/us/states/ms/districts/house/47.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
