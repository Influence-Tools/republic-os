---
type: Jurisdiction
title: "Fayette County, WV"
classification: county
fips: "54019"
state: "WV"
demographics:
  population: 39519
  population_under_18: 8175
  population_18_64: 22473
  population_65_plus: 8871
  median_household_income: 53194
  poverty_rate: 19.24
  homeownership_rate: 77.67
  unemployment_rate: 5.55
  median_home_value: 105800
  gini_index: 0.4417
  vacancy_rate: 16.43
  race_white: 36269
  race_black: 1641
  race_asian: 21
  race_native: 10
  hispanic: 549
  bachelors_plus: 6145
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/10"
    rel: in-district
    area_weight: 0.8592
  - to: "us/states/wv/districts/senate/9"
    rel: in-district
    area_weight: 0.1408
  - to: "us/states/wv/districts/house/51"
    rel: in-district
    area_weight: 0.5535
  - to: "us/states/wv/districts/house/50"
    rel: in-district
    area_weight: 0.3501
  - to: "us/states/wv/districts/house/45"
    rel: in-district
    area_weight: 0.0943
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Fayette County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39519 |
| Under 18 | 8175 |
| 18–64 | 22473 |
| 65+ | 8871 |
| Median household income | 53194 |
| Poverty rate | 19.24 |
| Homeownership rate | 77.67 |
| Unemployment rate | 5.55 |
| Median home value | 105800 |
| Gini index | 0.4417 |
| Vacancy rate | 16.43 |
| White | 36269 |
| Black | 1641 |
| Asian | 21 |
| Native | 10 |
| Hispanic/Latino | 549 |
| Bachelor's or higher | 6145 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 10](/us/states/wv/districts/senate/10.md) — 86% (state senate)
- [WV Senate District 9](/us/states/wv/districts/senate/9.md) — 14% (state senate)
- [WV House District 51](/us/states/wv/districts/house/51.md) — 55% (state house)
- [WV House District 50](/us/states/wv/districts/house/50.md) — 35% (state house)
- [WV House District 45](/us/states/wv/districts/house/45.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
