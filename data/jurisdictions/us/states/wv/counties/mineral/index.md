---
type: Jurisdiction
title: "Mineral County, WV"
classification: county
fips: "54057"
state: "WV"
demographics:
  population: 26854
  population_under_18: 5406
  population_18_64: 15377
  population_65_plus: 6071
  median_household_income: 69375
  poverty_rate: 14.04
  homeownership_rate: 80.98
  unemployment_rate: 6.56
  median_home_value: 180400
  gini_index: 0.4704
  vacancy_rate: 11.1
  race_white: 24957
  race_black: 357
  race_asian: 58
  race_native: 102
  hispanic: 332
  bachelors_plus: 6855
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9924
  - to: "us/states/md/districts/06"
    rel: in-district
    area_weight: 0.0076
  - to: "us/states/wv/districts/senate/14"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/wv/districts/house/88"
    rel: in-district
    area_weight: 0.6014
  - to: "us/states/wv/districts/house/87"
    rel: in-district
    area_weight: 0.397
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Mineral County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26854 |
| Under 18 | 5406 |
| 18–64 | 15377 |
| 65+ | 6071 |
| Median household income | 69375 |
| Poverty rate | 14.04 |
| Homeownership rate | 80.98 |
| Unemployment rate | 6.56 |
| Median home value | 180400 |
| Gini index | 0.4704 |
| Vacancy rate | 11.1 |
| White | 24957 |
| Black | 357 |
| Asian | 58 |
| Native | 102 |
| Hispanic/Latino | 332 |
| Bachelor's or higher | 6855 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 99% (congressional)
- [MD-06](/us/states/md/districts/06.md) — 1% (congressional)
- [WV Senate District 14](/us/states/wv/districts/senate/14.md) — 100% (state senate)
- [WV House District 88](/us/states/wv/districts/house/88.md) — 60% (state house)
- [WV House District 87](/us/states/wv/districts/house/87.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
