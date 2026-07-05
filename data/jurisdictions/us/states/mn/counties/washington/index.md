---
type: Jurisdiction
title: "Washington County, MN"
classification: county
fips: "27163"
state: "MN"
demographics:
  population: 276238
  population_under_18: 66194
  population_18_64: 164071
  population_65_plus: 45973
  median_household_income: 115345
  poverty_rate: 5.12
  homeownership_rate: 81.29
  unemployment_rate: 3.37
  median_home_value: 422000
  gini_index: 0.426
  vacancy_rate: 3.41
  race_white: 215812
  race_black: 15355
  race_asian: 21295
  race_native: 689
  hispanic: 14552
  bachelors_plus: 125328
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.3979
  - to: "us/states/mn/districts/04"
    rel: in-district
    area_weight: 0.3888
  - to: "us/states/mn/districts/02"
    rel: in-district
    area_weight: 0.2119
  - to: "us/states/mn/districts/senate/33"
    rel: in-district
    area_weight: 0.4772
  - to: "us/states/mn/districts/senate/41"
    rel: in-district
    area_weight: 0.377
  - to: "us/states/mn/districts/senate/47"
    rel: in-district
    area_weight: 0.0841
  - to: "us/states/mn/districts/senate/53"
    rel: in-district
    area_weight: 0.0313
  - to: "us/states/mn/districts/senate/44"
    rel: in-district
    area_weight: 0.0291
  - to: "us/states/mn/districts/house/33b"
    rel: in-district
    area_weight: 0.2926
  - to: "us/states/mn/districts/house/41a"
    rel: in-district
    area_weight: 0.2647
  - to: "us/states/mn/districts/house/33a"
    rel: in-district
    area_weight: 0.1846
  - to: "us/states/mn/districts/house/41b"
    rel: in-district
    area_weight: 0.1123
  - to: "us/states/mn/districts/house/47b"
    rel: in-district
    area_weight: 0.0557
  - to: "us/states/mn/districts/house/53b"
    rel: in-district
    area_weight: 0.0313
  - to: "us/states/mn/districts/house/44b"
    rel: in-district
    area_weight: 0.0291
  - to: "us/states/mn/districts/house/47a"
    rel: in-district
    area_weight: 0.0285
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Washington County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 276238 |
| Under 18 | 66194 |
| 18–64 | 164071 |
| 65+ | 45973 |
| Median household income | 115345 |
| Poverty rate | 5.12 |
| Homeownership rate | 81.29 |
| Unemployment rate | 3.37 |
| Median home value | 422000 |
| Gini index | 0.426 |
| Vacancy rate | 3.41 |
| White | 215812 |
| Black | 15355 |
| Asian | 21295 |
| Native | 689 |
| Hispanic/Latino | 14552 |
| Bachelor's or higher | 125328 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 40% (congressional)
- [MN-04](/us/states/mn/districts/04.md) — 39% (congressional)
- [MN-02](/us/states/mn/districts/02.md) — 21% (congressional)
- [MN Senate District 33](/us/states/mn/districts/senate/33.md) — 48% (state senate)
- [MN Senate District 41](/us/states/mn/districts/senate/41.md) — 38% (state senate)
- [MN Senate District 47](/us/states/mn/districts/senate/47.md) — 8% (state senate)
- [MN Senate District 53](/us/states/mn/districts/senate/53.md) — 3% (state senate)
- [MN Senate District 44](/us/states/mn/districts/senate/44.md) — 3% (state senate)
- [MN House District 33B](/us/states/mn/districts/house/33b.md) — 29% (state house)
- [MN House District 41A](/us/states/mn/districts/house/41a.md) — 26% (state house)
- [MN House District 33A](/us/states/mn/districts/house/33a.md) — 18% (state house)
- [MN House District 41B](/us/states/mn/districts/house/41b.md) — 11% (state house)
- [MN House District 47B](/us/states/mn/districts/house/47b.md) — 6% (state house)
- [MN House District 53B](/us/states/mn/districts/house/53b.md) — 3% (state house)
- [MN House District 44B](/us/states/mn/districts/house/44b.md) — 3% (state house)
- [MN House District 47A](/us/states/mn/districts/house/47a.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
