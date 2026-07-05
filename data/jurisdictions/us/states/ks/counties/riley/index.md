---
type: Jurisdiction
title: "Riley County, KS"
classification: county
fips: "20161"
state: "KS"
demographics:
  population: 71946
  population_under_18: 11589
  population_18_64: 53154
  population_65_plus: 7203
  median_household_income: 61098
  poverty_rate: 19.87
  homeownership_rate: 46.08
  unemployment_rate: 3.79
  median_home_value: 237100
  gini_index: 0.482
  vacancy_rate: 9.95
  race_white: 55289
  race_black: 4714
  race_asian: 2995
  race_native: 760
  hispanic: 7205
  bachelors_plus: 26242
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ks/districts/senate/22"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ks/districts/house/64"
    rel: in-district
    area_weight: 0.7364
  - to: "us/states/ks/districts/house/51"
    rel: in-district
    area_weight: 0.1183
  - to: "us/states/ks/districts/house/68"
    rel: in-district
    area_weight: 0.1021
  - to: "us/states/ks/districts/house/67"
    rel: in-district
    area_weight: 0.0288
  - to: "us/states/ks/districts/house/66"
    rel: in-district
    area_weight: 0.0104
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Riley County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 71946 |
| Under 18 | 11589 |
| 18–64 | 53154 |
| 65+ | 7203 |
| Median household income | 61098 |
| Poverty rate | 19.87 |
| Homeownership rate | 46.08 |
| Unemployment rate | 3.79 |
| Median home value | 237100 |
| Gini index | 0.482 |
| Vacancy rate | 9.95 |
| White | 55289 |
| Black | 4714 |
| Asian | 2995 |
| Native | 760 |
| Hispanic/Latino | 7205 |
| Bachelor's or higher | 26242 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 22](/us/states/ks/districts/senate/22.md) — 100% (state senate)
- [KS House District 64](/us/states/ks/districts/house/64.md) — 74% (state house)
- [KS House District 51](/us/states/ks/districts/house/51.md) — 12% (state house)
- [KS House District 68](/us/states/ks/districts/house/68.md) — 10% (state house)
- [KS House District 67](/us/states/ks/districts/house/67.md) — 3% (state house)
- [KS House District 66](/us/states/ks/districts/house/66.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
