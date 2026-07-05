---
type: Jurisdiction
title: "Stanislaus County, CA"
classification: county
fips: "06099"
state: "CA"
demographics:
  population: 553990
  population_under_18: 147379
  population_18_64: 330340
  population_65_plus: 76271
  median_household_income: 81468
  poverty_rate: 13.53
  homeownership_rate: 61.18
  unemployment_rate: 7.98
  median_home_value: 450100
  gini_index: 0.4426
  vacancy_rate: 3.93
  race_white: 237229
  race_black: 15171
  race_asian: 33935
  race_native: 7720
  hispanic: 277207
  bachelors_plus: 91801
districts:
  - to: "us/states/ca/districts/13"
    rel: in-district
    area_weight: 0.5577
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.3433
  - to: "us/states/ca/districts/09"
    rel: in-district
    area_weight: 0.0982
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/22"
    rel: in-district
    area_weight: 0.6037
  - to: "us/states/ca/districts/house/9"
    rel: in-district
    area_weight: 0.3962
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Stanislaus County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 553990 |
| Under 18 | 147379 |
| 18–64 | 330340 |
| 65+ | 76271 |
| Median household income | 81468 |
| Poverty rate | 13.53 |
| Homeownership rate | 61.18 |
| Unemployment rate | 7.98 |
| Median home value | 450100 |
| Gini index | 0.4426 |
| Vacancy rate | 3.93 |
| White | 237229 |
| Black | 15171 |
| Asian | 33935 |
| Native | 7720 |
| Hispanic/Latino | 277207 |
| Bachelor's or higher | 91801 |

## Districts

- [CA-13](/us/states/ca/districts/13.md) — 56% (congressional)
- [CA-05](/us/states/ca/districts/05.md) — 34% (congressional)
- [CA-09](/us/states/ca/districts/09.md) — 10% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 22](/us/states/ca/districts/house/22.md) — 60% (state house)
- [CA House District 9](/us/states/ca/districts/house/9.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
