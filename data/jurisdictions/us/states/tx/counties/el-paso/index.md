---
type: Jurisdiction
title: "El Paso County, TX"
classification: county
fips: "48141"
state: "TX"
demographics:
  population: 870779
  population_under_18: 226840
  population_18_64: 529768
  population_65_plus: 114171
  median_household_income: 59806
  poverty_rate: 18.75
  homeownership_rate: 64.23
  unemployment_rate: 6.0
  median_home_value: 180400
  gini_index: 0.4672
  vacancy_rate: 7.4
  race_white: 257683
  race_black: 29487
  race_asian: 11128
  race_native: 8239
  hispanic: 720158
  bachelors_plus: 189363
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.6865
  - to: "us/states/tx/districts/16"
    rel: in-district
    area_weight: 0.3118
  - to: "us/states/tx/districts/senate/29"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/house/75"
    rel: in-district
    area_weight: 0.4689
  - to: "us/states/tx/districts/house/74"
    rel: in-district
    area_weight: 0.2317
  - to: "us/states/tx/districts/house/78"
    rel: in-district
    area_weight: 0.1463
  - to: "us/states/tx/districts/house/79"
    rel: in-district
    area_weight: 0.094
  - to: "us/states/tx/districts/house/77"
    rel: in-district
    area_weight: 0.0585
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# El Paso County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 870779 |
| Under 18 | 226840 |
| 18–64 | 529768 |
| 65+ | 114171 |
| Median household income | 59806 |
| Poverty rate | 18.75 |
| Homeownership rate | 64.23 |
| Unemployment rate | 6.0 |
| Median home value | 180400 |
| Gini index | 0.4672 |
| Vacancy rate | 7.4 |
| White | 257683 |
| Black | 29487 |
| Asian | 11128 |
| Native | 8239 |
| Hispanic/Latino | 720158 |
| Bachelor's or higher | 189363 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 69% (congressional)
- [TX-16](/us/states/tx/districts/16.md) — 31% (congressional)
- [TX Senate District 29](/us/states/tx/districts/senate/29.md) — 100% (state senate)
- [TX House District 75](/us/states/tx/districts/house/75.md) — 47% (state house)
- [TX House District 74](/us/states/tx/districts/house/74.md) — 23% (state house)
- [TX House District 78](/us/states/tx/districts/house/78.md) — 15% (state house)
- [TX House District 79](/us/states/tx/districts/house/79.md) — 9% (state house)
- [TX House District 77](/us/states/tx/districts/house/77.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
