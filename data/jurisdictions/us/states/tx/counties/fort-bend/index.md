---
type: Jurisdiction
title: "Fort Bend County, TX"
classification: county
fips: "48157"
state: "TX"
demographics:
  population: 893767
  population_under_18: 238118
  population_18_64: 543360
  population_65_plus: 112289
  median_household_income: 114041
  poverty_rate: 7.57
  homeownership_rate: 76.96
  unemployment_rate: 5.05
  median_home_value: 374500
  gini_index: 0.4326
  vacancy_rate: 4.23
  race_white: 300429
  race_black: 186159
  race_asian: 197513
  race_native: 3781
  hispanic: 220445
  bachelors_plus: 410511
districts:
  - to: "us/states/tx/districts/22"
    rel: in-district
    area_weight: 0.8564
  - to: "us/states/tx/districts/09"
    rel: in-district
    area_weight: 0.0746
  - to: "us/states/tx/districts/07"
    rel: in-district
    area_weight: 0.0677
  - to: "us/states/tx/districts/senate/17"
    rel: in-district
    area_weight: 0.5757
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.3324
  - to: "us/states/tx/districts/senate/13"
    rel: in-district
    area_weight: 0.0918
  - to: "us/states/tx/districts/house/28"
    rel: in-district
    area_weight: 0.4764
  - to: "us/states/tx/districts/house/85"
    rel: in-district
    area_weight: 0.2643
  - to: "us/states/tx/districts/house/27"
    rel: in-district
    area_weight: 0.1038
  - to: "us/states/tx/districts/house/26"
    rel: in-district
    area_weight: 0.0932
  - to: "us/states/tx/districts/house/76"
    rel: in-district
    area_weight: 0.0622
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Fort Bend County, TX

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 893767 |
| Under 18 | 238118 |
| 18–64 | 543360 |
| 65+ | 112289 |
| Median household income | 114041 |
| Poverty rate | 7.57 |
| Homeownership rate | 76.96 |
| Unemployment rate | 5.05 |
| Median home value | 374500 |
| Gini index | 0.4326 |
| Vacancy rate | 4.23 |
| White | 300429 |
| Black | 186159 |
| Asian | 197513 |
| Native | 3781 |
| Hispanic/Latino | 220445 |
| Bachelor's or higher | 410511 |

## Districts

- [TX-22](/us/states/tx/districts/22.md) — 86% (congressional)
- [TX-09](/us/states/tx/districts/09.md) — 7% (congressional)
- [TX-07](/us/states/tx/districts/07.md) — 7% (congressional)
- [TX Senate District 17](/us/states/tx/districts/senate/17.md) — 58% (state senate)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 33% (state senate)
- [TX Senate District 13](/us/states/tx/districts/senate/13.md) — 9% (state senate)
- [TX House District 28](/us/states/tx/districts/house/28.md) — 48% (state house)
- [TX House District 85](/us/states/tx/districts/house/85.md) — 26% (state house)
- [TX House District 27](/us/states/tx/districts/house/27.md) — 10% (state house)
- [TX House District 26](/us/states/tx/districts/house/26.md) — 9% (state house)
- [TX House District 76](/us/states/tx/districts/house/76.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
