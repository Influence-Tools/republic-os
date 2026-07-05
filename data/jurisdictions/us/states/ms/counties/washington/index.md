---
type: Jurisdiction
title: "Washington County, MS"
classification: county
fips: "28151"
state: "MS"
demographics:
  population: 42765
  population_under_18: 10961
  population_18_64: 24183
  population_65_plus: 7621
  median_household_income: 42165
  poverty_rate: 26.45
  homeownership_rate: 60.19
  unemployment_rate: 6.28
  median_home_value: 104000
  gini_index: 0.4987
  vacancy_rate: 17.99
  race_white: 10216
  race_black: 30599
  race_asian: 338
  race_native: 18
  hispanic: 664
  bachelors_plus: 8953
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/ms/districts/senate/12"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ms/districts/house/50"
    rel: in-district
    area_weight: 0.8149
  - to: "us/states/ms/districts/house/49"
    rel: in-district
    area_weight: 0.1844
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Washington County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42765 |
| Under 18 | 10961 |
| 18–64 | 24183 |
| 65+ | 7621 |
| Median household income | 42165 |
| Poverty rate | 26.45 |
| Homeownership rate | 60.19 |
| Unemployment rate | 6.28 |
| Median home value | 104000 |
| Gini index | 0.4987 |
| Vacancy rate | 17.99 |
| White | 10216 |
| Black | 30599 |
| Asian | 338 |
| Native | 18 |
| Hispanic/Latino | 664 |
| Bachelor's or higher | 8953 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 12](/us/states/ms/districts/senate/12.md) — 100% (state senate)
- [MS House District 50](/us/states/ms/districts/house/50.md) — 81% (state house)
- [MS House District 49](/us/states/ms/districts/house/49.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
