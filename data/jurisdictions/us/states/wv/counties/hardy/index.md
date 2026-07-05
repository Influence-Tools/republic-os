---
type: Jurisdiction
title: "Hardy County, WV"
classification: county
fips: "54031"
state: "WV"
demographics:
  population: 14243
  population_under_18: 2823
  population_18_64: 8117
  population_65_plus: 3303
  median_household_income: 49272
  poverty_rate: 17.69
  homeownership_rate: 77.34
  unemployment_rate: 7.33
  median_home_value: 166300
  gini_index: 0.4303
  vacancy_rate: 28.13
  race_white: 12798
  race_black: 695
  race_asian: 8
  race_native: 2
  hispanic: 658
  bachelors_plus: 2357
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/senate/14"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wv/districts/house/86"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Hardy County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14243 |
| Under 18 | 2823 |
| 18–64 | 8117 |
| 65+ | 3303 |
| Median household income | 49272 |
| Poverty rate | 17.69 |
| Homeownership rate | 77.34 |
| Unemployment rate | 7.33 |
| Median home value | 166300 |
| Gini index | 0.4303 |
| Vacancy rate | 28.13 |
| White | 12798 |
| Black | 695 |
| Asian | 8 |
| Native | 2 |
| Hispanic/Latino | 658 |
| Bachelor's or higher | 2357 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 14](/us/states/wv/districts/senate/14.md) — 100% (state senate)
- [WV House District 86](/us/states/wv/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
