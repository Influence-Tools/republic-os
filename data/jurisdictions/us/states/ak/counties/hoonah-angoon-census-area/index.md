---
type: Jurisdiction
title: "Hoonah-Angoon Census Area, AK"
classification: county
fips: "02105"
state: "AK"
demographics:
  population: 2311
  population_under_18: 427
  population_18_64: 604
  population_65_plus: 1280
  median_household_income: 61406
  poverty_rate: 14.25
  homeownership_rate: 71.97
  unemployment_rate: 15.85
  median_home_value: 262800
  gini_index: 0.4301
  vacancy_rate: 47.29
  race_white: 1144
  race_black: 14
  race_asian: 61
  race_native: 607
  hispanic: 255
  bachelors_plus: 561
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.7348
  - to: "us/states/ak/districts/senate/a"
    rel: in-district
    area_weight: 0.5523
  - to: "us/states/ak/districts/senate/b"
    rel: in-district
    area_weight: 0.1635
  - to: "us/states/ak/districts/house/2"
    rel: in-district
    area_weight: 0.5523
  - to: "us/states/ak/districts/house/3"
    rel: in-district
    area_weight: 0.1635
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Hoonah-Angoon Census Area, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2311 |
| Under 18 | 427 |
| 18–64 | 604 |
| 65+ | 1280 |
| Median household income | 61406 |
| Poverty rate | 14.25 |
| Homeownership rate | 71.97 |
| Unemployment rate | 15.85 |
| Median home value | 262800 |
| Gini index | 0.4301 |
| Vacancy rate | 47.29 |
| White | 1144 |
| Black | 14 |
| Asian | 61 |
| Native | 607 |
| Hispanic/Latino | 255 |
| Bachelor's or higher | 561 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 73% (congressional)
- [AK Senate District A](/us/states/ak/districts/senate/a.md) — 55% (state senate)
- [AK Senate District B](/us/states/ak/districts/senate/b.md) — 16% (state senate)
- [AK House District 2](/us/states/ak/districts/house/2.md) — 55% (state house)
- [AK House District 3](/us/states/ak/districts/house/3.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
