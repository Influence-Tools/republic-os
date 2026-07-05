---
type: Jurisdiction
title: "Harvey County, KS"
classification: county
fips: "20079"
state: "KS"
demographics:
  population: 33756
  population_under_18: 7934
  population_18_64: 18583
  population_65_plus: 7239
  median_household_income: 74368
  poverty_rate: 8.23
  homeownership_rate: 69.85
  unemployment_rate: 4.81
  median_home_value: 180300
  gini_index: 0.3765
  vacancy_rate: 6.52
  race_white: 28206
  race_black: 478
  race_asian: 389
  race_native: 550
  hispanic: 4129
  bachelors_plus: 9350
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ks/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/74"
    rel: in-district
    area_weight: 0.6982
  - to: "us/states/ks/districts/house/72"
    rel: in-district
    area_weight: 0.3018
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Harvey County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33756 |
| Under 18 | 7934 |
| 18–64 | 18583 |
| 65+ | 7239 |
| Median household income | 74368 |
| Poverty rate | 8.23 |
| Homeownership rate | 69.85 |
| Unemployment rate | 4.81 |
| Median home value | 180300 |
| Gini index | 0.3765 |
| Vacancy rate | 6.52 |
| White | 28206 |
| Black | 478 |
| Asian | 389 |
| Native | 550 |
| Hispanic/Latino | 4129 |
| Bachelor's or higher | 9350 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 31](/us/states/ks/districts/senate/31.md) — 100% (state senate)
- [KS House District 74](/us/states/ks/districts/house/74.md) — 70% (state house)
- [KS House District 72](/us/states/ks/districts/house/72.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
