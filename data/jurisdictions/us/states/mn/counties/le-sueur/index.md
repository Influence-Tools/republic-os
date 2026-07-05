---
type: Jurisdiction
title: "Le Sueur County, MN"
classification: county
fips: "27079"
state: "MN"
demographics:
  population: 29113
  population_under_18: 6683
  population_18_64: 16947
  population_65_plus: 5483
  median_household_income: 94968
  poverty_rate: 6.44
  homeownership_rate: 81.01
  unemployment_rate: 4.18
  median_home_value: 316500
  gini_index: 0.409
  vacancy_rate: 10.76
  race_white: 26347
  race_black: 219
  race_asian: 151
  race_native: 78
  hispanic: 2009
  bachelors_plus: 6894
districts:
  - to: "us/states/mn/districts/02"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.9775
  - to: "us/states/mn/districts/senate/18"
    rel: in-district
    area_weight: 0.0223
  - to: "us/states/mn/districts/house/22b"
    rel: in-district
    area_weight: 0.9775
  - to: "us/states/mn/districts/house/18a"
    rel: in-district
    area_weight: 0.0223
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Le Sueur County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29113 |
| Under 18 | 6683 |
| 18–64 | 16947 |
| 65+ | 5483 |
| Median household income | 94968 |
| Poverty rate | 6.44 |
| Homeownership rate | 81.01 |
| Unemployment rate | 4.18 |
| Median home value | 316500 |
| Gini index | 0.409 |
| Vacancy rate | 10.76 |
| White | 26347 |
| Black | 219 |
| Asian | 151 |
| Native | 78 |
| Hispanic/Latino | 2009 |
| Bachelor's or higher | 6894 |

## Districts

- [MN-02](/us/states/mn/districts/02.md) — 100% (congressional)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 98% (state senate)
- [MN Senate District 18](/us/states/mn/districts/senate/18.md) — 2% (state senate)
- [MN House District 22B](/us/states/mn/districts/house/22b.md) — 98% (state house)
- [MN House District 18A](/us/states/mn/districts/house/18a.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
