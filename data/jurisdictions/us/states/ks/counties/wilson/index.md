---
type: Jurisdiction
title: "Wilson County, KS"
classification: county
fips: "20205"
state: "KS"
demographics:
  population: 8505
  population_under_18: 2032
  population_18_64: 4509
  population_65_plus: 1964
  median_household_income: 60677
  poverty_rate: 15.48
  homeownership_rate: 77.74
  unemployment_rate: 2.96
  median_home_value: 93500
  gini_index: 0.4301
  vacancy_rate: 21.72
  race_white: 7912
  race_black: 15
  race_asian: 2
  race_native: 65
  hispanic: 327
  bachelors_plus: 1449
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Wilson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8505 |
| Under 18 | 2032 |
| 18–64 | 4509 |
| 65+ | 1964 |
| Median household income | 60677 |
| Poverty rate | 15.48 |
| Homeownership rate | 77.74 |
| Unemployment rate | 2.96 |
| Median home value | 93500 |
| Gini index | 0.4301 |
| Vacancy rate | 21.72 |
| White | 7912 |
| Black | 15 |
| Asian | 2 |
| Native | 65 |
| Hispanic/Latino | 327 |
| Bachelor's or higher | 1449 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 100% (state senate)
- [KS House District 13](/us/states/ks/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
