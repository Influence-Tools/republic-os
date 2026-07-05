---
type: Jurisdiction
title: "Madison County, MS"
classification: county
fips: "28089"
state: "MS"
demographics:
  population: 111647
  population_under_18: 27113
  population_18_64: 67492
  population_65_plus: 17042
  median_household_income: 83441
  poverty_rate: 11.17
  homeownership_rate: 71.32
  unemployment_rate: 3.73
  median_home_value: 311100
  gini_index: 0.4963
  vacancy_rate: 7.43
  race_white: 61103
  race_black: 41466
  race_asian: 3347
  race_native: 83
  hispanic: 4320
  bachelors_plus: 53158
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.703
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.297
  - to: "us/states/ms/districts/senate/21"
    rel: in-district
    area_weight: 0.6005
  - to: "us/states/ms/districts/senate/22"
    rel: in-district
    area_weight: 0.1897
  - to: "us/states/ms/districts/senate/23"
    rel: in-district
    area_weight: 0.0874
  - to: "us/states/ms/districts/senate/26"
    rel: in-district
    area_weight: 0.0665
  - to: "us/states/ms/districts/senate/25"
    rel: in-district
    area_weight: 0.0558
  - to: "us/states/ms/districts/house/27"
    rel: in-district
    area_weight: 0.3597
  - to: "us/states/ms/districts/house/57"
    rel: in-district
    area_weight: 0.2914
  - to: "us/states/ms/districts/house/75"
    rel: in-district
    area_weight: 0.1163
  - to: "us/states/ms/districts/house/56"
    rel: in-district
    area_weight: 0.0991
  - to: "us/states/ms/districts/house/73"
    rel: in-district
    area_weight: 0.0668
  - to: "us/states/ms/districts/house/58"
    rel: in-district
    area_weight: 0.0515
  - to: "us/states/ms/districts/house/72"
    rel: in-district
    area_weight: 0.0084
  - to: "us/states/ms/districts/house/64"
    rel: in-district
    area_weight: 0.0064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Madison County, MS

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 111647 |
| Under 18 | 27113 |
| 18–64 | 67492 |
| 65+ | 17042 |
| Median household income | 83441 |
| Poverty rate | 11.17 |
| Homeownership rate | 71.32 |
| Unemployment rate | 3.73 |
| Median home value | 311100 |
| Gini index | 0.4963 |
| Vacancy rate | 7.43 |
| White | 61103 |
| Black | 41466 |
| Asian | 3347 |
| Native | 83 |
| Hispanic/Latino | 4320 |
| Bachelor's or higher | 53158 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 70% (congressional)
- [MS-03](/us/states/ms/districts/03.md) — 30% (congressional)
- [MS Senate District 21](/us/states/ms/districts/senate/21.md) — 60% (state senate)
- [MS Senate District 22](/us/states/ms/districts/senate/22.md) — 19% (state senate)
- [MS Senate District 23](/us/states/ms/districts/senate/23.md) — 9% (state senate)
- [MS Senate District 26](/us/states/ms/districts/senate/26.md) — 7% (state senate)
- [MS Senate District 25](/us/states/ms/districts/senate/25.md) — 6% (state senate)
- [MS House District 27](/us/states/ms/districts/house/27.md) — 36% (state house)
- [MS House District 57](/us/states/ms/districts/house/57.md) — 29% (state house)
- [MS House District 75](/us/states/ms/districts/house/75.md) — 12% (state house)
- [MS House District 56](/us/states/ms/districts/house/56.md) — 10% (state house)
- [MS House District 73](/us/states/ms/districts/house/73.md) — 7% (state house)
- [MS House District 58](/us/states/ms/districts/house/58.md) — 5% (state house)
- [MS House District 72](/us/states/ms/districts/house/72.md) — 1% (state house)
- [MS House District 64](/us/states/ms/districts/house/64.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
