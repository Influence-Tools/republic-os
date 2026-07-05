---
type: Jurisdiction
title: "Lake County, IN"
classification: county
fips: "18089"
state: "IN"
demographics:
  population: 500379
  population_under_18: 115840
  population_18_64: 295097
  population_65_plus: 89442
  median_household_income: 71493
  poverty_rate: 14.29
  homeownership_rate: 71.67
  unemployment_rate: 6.08
  median_home_value: 230600
  gini_index: 0.4556
  vacancy_rate: 10.26
  race_white: 274459
  race_black: 115462
  race_asian: 8064
  race_native: 2582
  hispanic: 104584
  bachelors_plus: 117510
districts:
  - to: "us/states/in/districts/01"
    rel: in-district
    area_weight: 0.8033
  - to: "us/states/in/districts/senate/6"
    rel: in-district
    area_weight: 0.4329
  - to: "us/states/in/districts/senate/3"
    rel: in-district
    area_weight: 0.1836
  - to: "us/states/in/districts/senate/1"
    rel: in-district
    area_weight: 0.1104
  - to: "us/states/in/districts/senate/2"
    rel: in-district
    area_weight: 0.077
  - to: "us/states/in/districts/house/11"
    rel: in-district
    area_weight: 0.306
  - to: "us/states/in/districts/house/19"
    rel: in-district
    area_weight: 0.1453
  - to: "us/states/in/districts/house/3"
    rel: in-district
    area_weight: 0.0819
  - to: "us/states/in/districts/house/15"
    rel: in-district
    area_weight: 0.0724
  - to: "us/states/in/districts/house/2"
    rel: in-district
    area_weight: 0.0637
  - to: "us/states/in/districts/house/14"
    rel: in-district
    area_weight: 0.0605
  - to: "us/states/in/districts/house/12"
    rel: in-district
    area_weight: 0.0396
  - to: "us/states/in/districts/house/1"
    rel: in-district
    area_weight: 0.0346
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Lake County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 500379 |
| Under 18 | 115840 |
| 18–64 | 295097 |
| 65+ | 89442 |
| Median household income | 71493 |
| Poverty rate | 14.29 |
| Homeownership rate | 71.67 |
| Unemployment rate | 6.08 |
| Median home value | 230600 |
| Gini index | 0.4556 |
| Vacancy rate | 10.26 |
| White | 274459 |
| Black | 115462 |
| Asian | 8064 |
| Native | 2582 |
| Hispanic/Latino | 104584 |
| Bachelor's or higher | 117510 |

## Districts

- [IN-01](/us/states/in/districts/01.md) — 80% (congressional)
- [IN Senate District 6](/us/states/in/districts/senate/6.md) — 43% (state senate)
- [IN Senate District 3](/us/states/in/districts/senate/3.md) — 18% (state senate)
- [IN Senate District 1](/us/states/in/districts/senate/1.md) — 11% (state senate)
- [IN Senate District 2](/us/states/in/districts/senate/2.md) — 8% (state senate)
- [IN House District 11](/us/states/in/districts/house/11.md) — 31% (state house)
- [IN House District 19](/us/states/in/districts/house/19.md) — 15% (state house)
- [IN House District 3](/us/states/in/districts/house/3.md) — 8% (state house)
- [IN House District 15](/us/states/in/districts/house/15.md) — 7% (state house)
- [IN House District 2](/us/states/in/districts/house/2.md) — 6% (state house)
- [IN House District 14](/us/states/in/districts/house/14.md) — 6% (state house)
- [IN House District 12](/us/states/in/districts/house/12.md) — 4% (state house)
- [IN House District 1](/us/states/in/districts/house/1.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
