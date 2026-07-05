---
type: Jurisdiction
title: "Grafton County, NH"
classification: county
fips: "33009"
state: "NH"
demographics:
  population: 92120
  population_under_18: 14414
  population_18_64: 56562
  population_65_plus: 21144
  median_household_income: 88261
  poverty_rate: 10.35
  homeownership_rate: 71.32
  unemployment_rate: 3.18
  median_home_value: 344500
  gini_index: 0.4947
  vacancy_rate: 28.53
  race_white: 81303
  race_black: 1042
  race_asian: 3242
  race_native: 211
  hispanic: 2679
  bachelors_plus: 47331
districts:
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/nh/districts/senate/1"
    rel: in-district
    area_weight: 0.4117
  - to: "us/states/nh/districts/senate/5"
    rel: in-district
    area_weight: 0.2559
  - to: "us/states/nh/districts/senate/3"
    rel: in-district
    area_weight: 0.1485
  - to: "us/states/nh/districts/senate/7"
    rel: in-district
    area_weight: 0.0976
  - to: "us/states/nh/districts/senate/2"
    rel: in-district
    area_weight: 0.0862
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Grafton County, NH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92120 |
| Under 18 | 14414 |
| 18–64 | 56562 |
| 65+ | 21144 |
| Median household income | 88261 |
| Poverty rate | 10.35 |
| Homeownership rate | 71.32 |
| Unemployment rate | 3.18 |
| Median home value | 344500 |
| Gini index | 0.4947 |
| Vacancy rate | 28.53 |
| White | 81303 |
| Black | 1042 |
| Asian | 3242 |
| Native | 211 |
| Hispanic/Latino | 2679 |
| Bachelor's or higher | 47331 |

## Districts

- [NH-02](/us/states/nh/districts/02.md) — 100% (congressional)
- [NH Senate District 1](/us/states/nh/districts/senate/1.md) — 41% (state senate)
- [NH Senate District 5](/us/states/nh/districts/senate/5.md) — 26% (state senate)
- [NH Senate District 3](/us/states/nh/districts/senate/3.md) — 15% (state senate)
- [NH Senate District 7](/us/states/nh/districts/senate/7.md) — 10% (state senate)
- [NH Senate District 2](/us/states/nh/districts/senate/2.md) — 9% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
