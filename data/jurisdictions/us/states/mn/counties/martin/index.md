---
type: Jurisdiction
title: "Martin County, MN"
classification: county
fips: "27091"
state: "MN"
demographics:
  population: 19780
  population_under_18: 4515
  population_18_64: 10399
  population_65_plus: 4866
  median_household_income: 59507
  poverty_rate: 13.13
  homeownership_rate: 68.9
  unemployment_rate: 4.16
  median_home_value: 163500
  gini_index: 0.4546
  vacancy_rate: 9.15
  race_white: 18303
  race_black: 169
  race_asian: 101
  race_native: 49
  hispanic: 1421
  bachelors_plus: 4370
districts:
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.8025
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.1974
  - to: "us/states/mn/districts/house/22a"
    rel: in-district
    area_weight: 0.8025
  - to: "us/states/mn/districts/house/21b"
    rel: in-district
    area_weight: 0.1974
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Martin County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19780 |
| Under 18 | 4515 |
| 18–64 | 10399 |
| 65+ | 4866 |
| Median household income | 59507 |
| Poverty rate | 13.13 |
| Homeownership rate | 68.9 |
| Unemployment rate | 4.16 |
| Median home value | 163500 |
| Gini index | 0.4546 |
| Vacancy rate | 9.15 |
| White | 18303 |
| Black | 169 |
| Asian | 101 |
| Native | 49 |
| Hispanic/Latino | 1421 |
| Bachelor's or higher | 4370 |

## Districts

- [MN-01](/us/states/mn/districts/01.md) — 100% (congressional)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 80% (state senate)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 20% (state senate)
- [MN House District 22A](/us/states/mn/districts/house/22a.md) — 80% (state house)
- [MN House District 21B](/us/states/mn/districts/house/21b.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
