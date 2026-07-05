---
type: Jurisdiction
title: "Nicholas County, WV"
classification: county
fips: "54067"
state: "WV"
demographics:
  population: 24277
  population_under_18: 5122
  population_18_64: 13346
  population_65_plus: 5809
  median_household_income: 54639
  poverty_rate: 15.4
  homeownership_rate: 82.21
  unemployment_rate: 5.92
  median_home_value: 121600
  gini_index: 0.4827
  vacancy_rate: 24.57
  race_white: 23386
  race_black: 133
  race_asian: 59
  race_native: 2
  hispanic: 265
  bachelors_plus: 5759
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/house/49"
    rel: in-district
    area_weight: 0.7701
  - to: "us/states/wv/districts/house/48"
    rel: in-district
    area_weight: 0.2297
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Nicholas County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24277 |
| Under 18 | 5122 |
| 18–64 | 13346 |
| 65+ | 5809 |
| Median household income | 54639 |
| Poverty rate | 15.4 |
| Homeownership rate | 82.21 |
| Unemployment rate | 5.92 |
| Median home value | 121600 |
| Gini index | 0.4827 |
| Vacancy rate | 24.57 |
| White | 23386 |
| Black | 133 |
| Asian | 59 |
| Native | 2 |
| Hispanic/Latino | 265 |
| Bachelor's or higher | 5759 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 10](/us/states/wv/districts/senate/10.md) — 100% (state senate)
- [WV House District 49](/us/states/wv/districts/house/49.md) — 77% (state house)
- [WV House District 48](/us/states/wv/districts/house/48.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
