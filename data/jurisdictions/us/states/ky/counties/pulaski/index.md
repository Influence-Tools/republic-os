---
type: Jurisdiction
title: "Pulaski County, KY"
classification: county
fips: "21199"
state: "KY"
demographics:
  population: 65897
  population_under_18: 14636
  population_18_64: 38436
  population_65_plus: 12825
  median_household_income: 51898
  poverty_rate: 19.71
  homeownership_rate: 72.48
  unemployment_rate: 4.94
  median_home_value: 166900
  gini_index: 0.474
  vacancy_rate: 17.38
  race_white: 61777
  race_black: 551
  race_asian: 535
  race_native: 106
  hispanic: 2040
  bachelors_plus: 12108
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/senate/15"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/85"
    rel: in-district
    area_weight: 0.4444
  - to: "us/states/ky/districts/house/83"
    rel: in-district
    area_weight: 0.2817
  - to: "us/states/ky/districts/house/71"
    rel: in-district
    area_weight: 0.167
  - to: "us/states/ky/districts/house/52"
    rel: in-district
    area_weight: 0.083
  - to: "us/states/ky/districts/house/80"
    rel: in-district
    area_weight: 0.0237
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Pulaski County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65897 |
| Under 18 | 14636 |
| 18–64 | 38436 |
| 65+ | 12825 |
| Median household income | 51898 |
| Poverty rate | 19.71 |
| Homeownership rate | 72.48 |
| Unemployment rate | 4.94 |
| Median home value | 166900 |
| Gini index | 0.474 |
| Vacancy rate | 17.38 |
| White | 61777 |
| Black | 551 |
| Asian | 535 |
| Native | 106 |
| Hispanic/Latino | 2040 |
| Bachelor's or higher | 12108 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 15](/us/states/ky/districts/senate/15.md) — 100% (state senate)
- [KY House District 85](/us/states/ky/districts/house/85.md) — 44% (state house)
- [KY House District 83](/us/states/ky/districts/house/83.md) — 28% (state house)
- [KY House District 71](/us/states/ky/districts/house/71.md) — 17% (state house)
- [KY House District 52](/us/states/ky/districts/house/52.md) — 8% (state house)
- [KY House District 80](/us/states/ky/districts/house/80.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
