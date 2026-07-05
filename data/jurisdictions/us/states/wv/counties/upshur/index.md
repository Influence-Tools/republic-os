---
type: Jurisdiction
title: "Upshur County, WV"
classification: county
fips: "54097"
state: "WV"
demographics:
  population: 23712
  population_under_18: 4797
  population_18_64: 13743
  population_65_plus: 5172
  median_household_income: 54338
  poverty_rate: 19.24
  homeownership_rate: 80.72
  unemployment_rate: 5.72
  median_home_value: 170800
  gini_index: 0.4471
  vacancy_rate: 15.28
  race_white: 21830
  race_black: 317
  race_asian: 88
  race_native: 10
  hispanic: 351
  bachelors_plus: 4259
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/house/65"
    rel: in-district
    area_weight: 0.7008
  - to: "us/states/wv/districts/house/68"
    rel: in-district
    area_weight: 0.1808
  - to: "us/states/wv/districts/house/64"
    rel: in-district
    area_weight: 0.1181
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Upshur County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23712 |
| Under 18 | 4797 |
| 18–64 | 13743 |
| 65+ | 5172 |
| Median household income | 54338 |
| Poverty rate | 19.24 |
| Homeownership rate | 80.72 |
| Unemployment rate | 5.72 |
| Median home value | 170800 |
| Gini index | 0.4471 |
| Vacancy rate | 15.28 |
| White | 21830 |
| Black | 317 |
| Asian | 88 |
| Native | 10 |
| Hispanic/Latino | 351 |
| Bachelor's or higher | 4259 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 65](/us/states/wv/districts/house/65.md) — 70% (state house)
- [WV House District 68](/us/states/wv/districts/house/68.md) — 18% (state house)
- [WV House District 64](/us/states/wv/districts/house/64.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
