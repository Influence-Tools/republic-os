---
type: Jurisdiction
title: "Preston County, WV"
classification: county
fips: "54077"
state: "WV"
demographics:
  population: 34160
  population_under_18: 6104
  population_18_64: 21070
  population_65_plus: 6986
  median_household_income: 61880
  poverty_rate: 13.77
  homeownership_rate: 81.49
  unemployment_rate: 5.31
  median_home_value: 162800
  gini_index: 0.4081
  vacancy_rate: 15.64
  race_white: 30270
  race_black: 2258
  race_asian: 125
  race_native: 106
  hispanic: 661
  bachelors_plus: 6180
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/senate/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/house/84"
    rel: in-district
    area_weight: 0.5621
  - to: "us/states/wv/districts/house/83"
    rel: in-district
    area_weight: 0.4376
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Preston County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34160 |
| Under 18 | 6104 |
| 18–64 | 21070 |
| 65+ | 6986 |
| Median household income | 61880 |
| Poverty rate | 13.77 |
| Homeownership rate | 81.49 |
| Unemployment rate | 5.31 |
| Median home value | 162800 |
| Gini index | 0.4081 |
| Vacancy rate | 15.64 |
| White | 30270 |
| Black | 2258 |
| Asian | 125 |
| Native | 106 |
| Hispanic/Latino | 661 |
| Bachelor's or higher | 6180 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 14](/us/states/wv/districts/senate/14.md) — 100% (state senate)
- [WV House District 84](/us/states/wv/districts/house/84.md) — 56% (state house)
- [WV House District 83](/us/states/wv/districts/house/83.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
