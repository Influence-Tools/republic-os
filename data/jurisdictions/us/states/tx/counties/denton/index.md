---
type: Jurisdiction
title: "Denton County, TX"
classification: county
fips: "48121"
state: "TX"
demographics:
  population: 979561
  population_under_18: 228961
  population_18_64: 637475
  population_65_plus: 113125
  median_household_income: 111498
  poverty_rate: 7.07
  homeownership_rate: 65.46
  unemployment_rate: 4.02
  median_home_value: 437200
  gini_index: 0.4357
  vacancy_rate: 4.34
  race_white: 557664
  race_black: 107302
  race_asian: 108976
  race_native: 6852
  hispanic: 200647
  bachelors_plus: 442127
districts:
  - to: "us/states/tx/districts/26"
    rel: in-district
    area_weight: 0.7399
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.2383
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.0175
  - to: "us/states/tx/districts/senate/12"
    rel: in-district
    area_weight: 0.5517
  - to: "us/states/tx/districts/senate/30"
    rel: in-district
    area_weight: 0.4483
  - to: "us/states/tx/districts/house/106"
    rel: in-district
    area_weight: 0.2998
  - to: "us/states/tx/districts/house/64"
    rel: in-district
    area_weight: 0.255
  - to: "us/states/tx/districts/house/57"
    rel: in-district
    area_weight: 0.2033
  - to: "us/states/tx/districts/house/65"
    rel: in-district
    area_weight: 0.1594
  - to: "us/states/tx/districts/house/63"
    rel: in-district
    area_weight: 0.0824
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Denton County, TX

County jurisdiction — 9 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 979561 |
| Under 18 | 228961 |
| 18–64 | 637475 |
| 65+ | 113125 |
| Median household income | 111498 |
| Poverty rate | 7.07 |
| Homeownership rate | 65.46 |
| Unemployment rate | 4.02 |
| Median home value | 437200 |
| Gini index | 0.4357 |
| Vacancy rate | 4.34 |
| White | 557664 |
| Black | 107302 |
| Asian | 108976 |
| Native | 6852 |
| Hispanic/Latino | 200647 |
| Bachelor's or higher | 442127 |

## Districts

- [TX-26](/us/states/tx/districts/26.md) — 74% (congressional)
- [TX-13](/us/states/tx/districts/13.md) — 24% (congressional)
- [TX-04](/us/states/tx/districts/04.md) — 2% (congressional)
- [TX Senate District 12](/us/states/tx/districts/senate/12.md) — 55% (state senate)
- [TX Senate District 30](/us/states/tx/districts/senate/30.md) — 45% (state senate)
- [TX House District 106](/us/states/tx/districts/house/106.md) — 30% (state house)
- [TX House District 64](/us/states/tx/districts/house/64.md) — 26% (state house)
- [TX House District 57](/us/states/tx/districts/house/57.md) — 20% (state house)
- [TX House District 65](/us/states/tx/districts/house/65.md) — 16% (state house)
- [TX House District 63](/us/states/tx/districts/house/63.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
