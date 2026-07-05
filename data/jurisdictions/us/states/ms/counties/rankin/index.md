---
type: Jurisdiction
title: "Rankin County, MS"
classification: county
fips: "28121"
state: "MS"
demographics:
  population: 158854
  population_under_18: 35587
  population_18_64: 96661
  population_65_plus: 26606
  median_household_income: 79357
  poverty_rate: 9.84
  homeownership_rate: 76.82
  unemployment_rate: 4.35
  median_home_value: 237400
  gini_index: 0.4205
  vacancy_rate: 6.65
  race_white: 113415
  race_black: 33225
  race_asian: 2194
  race_native: 965
  hispanic: 5279
  bachelors_plus: 50539
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/ms/districts/senate/36"
    rel: in-district
    area_weight: 0.6236
  - to: "us/states/ms/districts/senate/20"
    rel: in-district
    area_weight: 0.2288
  - to: "us/states/ms/districts/senate/30"
    rel: in-district
    area_weight: 0.0909
  - to: "us/states/ms/districts/senate/31"
    rel: in-district
    area_weight: 0.0565
  - to: "us/states/ms/districts/house/75"
    rel: in-district
    area_weight: 0.2428
  - to: "us/states/ms/districts/house/77"
    rel: in-district
    area_weight: 0.2008
  - to: "us/states/ms/districts/house/60"
    rel: in-district
    area_weight: 0.1492
  - to: "us/states/ms/districts/house/62"
    rel: in-district
    area_weight: 0.1485
  - to: "us/states/ms/districts/house/74"
    rel: in-district
    area_weight: 0.092
  - to: "us/states/ms/districts/house/59"
    rel: in-district
    area_weight: 0.0497
  - to: "us/states/ms/districts/house/68"
    rel: in-district
    area_weight: 0.046
  - to: "us/states/ms/districts/house/79"
    rel: in-district
    area_weight: 0.0365
  - to: "us/states/ms/districts/house/61"
    rel: in-district
    area_weight: 0.0343
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Rankin County, MS

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 158854 |
| Under 18 | 35587 |
| 18–64 | 96661 |
| 65+ | 26606 |
| Median household income | 79357 |
| Poverty rate | 9.84 |
| Homeownership rate | 76.82 |
| Unemployment rate | 4.35 |
| Median home value | 237400 |
| Gini index | 0.4205 |
| Vacancy rate | 6.65 |
| White | 113415 |
| Black | 33225 |
| Asian | 2194 |
| Native | 965 |
| Hispanic/Latino | 5279 |
| Bachelor's or higher | 50539 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 36](/us/states/ms/districts/senate/36.md) — 62% (state senate)
- [MS Senate District 20](/us/states/ms/districts/senate/20.md) — 23% (state senate)
- [MS Senate District 30](/us/states/ms/districts/senate/30.md) — 9% (state senate)
- [MS Senate District 31](/us/states/ms/districts/senate/31.md) — 6% (state senate)
- [MS House District 75](/us/states/ms/districts/house/75.md) — 24% (state house)
- [MS House District 77](/us/states/ms/districts/house/77.md) — 20% (state house)
- [MS House District 60](/us/states/ms/districts/house/60.md) — 15% (state house)
- [MS House District 62](/us/states/ms/districts/house/62.md) — 15% (state house)
- [MS House District 74](/us/states/ms/districts/house/74.md) — 9% (state house)
- [MS House District 59](/us/states/ms/districts/house/59.md) — 5% (state house)
- [MS House District 68](/us/states/ms/districts/house/68.md) — 5% (state house)
- [MS House District 79](/us/states/ms/districts/house/79.md) — 4% (state house)
- [MS House District 61](/us/states/ms/districts/house/61.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
