---
type: Jurisdiction
title: "Wood County, WV"
classification: county
fips: "54107"
state: "WV"
demographics:
  population: 83407
  population_under_18: 17380
  population_18_64: 48001
  population_65_plus: 18026
  median_household_income: 57810
  poverty_rate: 14.75
  homeownership_rate: 75.1
  unemployment_rate: 5.35
  median_home_value: 158500
  gini_index: 0.4608
  vacancy_rate: 11.04
  race_white: 78671
  race_black: 978
  race_asian: 365
  race_native: 85
  hispanic: 1231
  bachelors_plus: 19943
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/wv/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/house/14"
    rel: in-district
    area_weight: 0.4798
  - to: "us/states/wv/districts/house/10"
    rel: in-district
    area_weight: 0.3881
  - to: "us/states/wv/districts/house/13"
    rel: in-district
    area_weight: 0.0688
  - to: "us/states/wv/districts/house/12"
    rel: in-district
    area_weight: 0.0389
  - to: "us/states/wv/districts/house/11"
    rel: in-district
    area_weight: 0.0239
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Wood County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83407 |
| Under 18 | 17380 |
| 18–64 | 48001 |
| 65+ | 18026 |
| Median household income | 57810 |
| Poverty rate | 14.75 |
| Homeownership rate | 75.1 |
| Unemployment rate | 5.35 |
| Median home value | 158500 |
| Gini index | 0.4608 |
| Vacancy rate | 11.04 |
| White | 78671 |
| Black | 978 |
| Asian | 365 |
| Native | 85 |
| Hispanic/Latino | 1231 |
| Bachelor's or higher | 19943 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 3](/us/states/wv/districts/senate/3.md) — 100% (state senate)
- [WV House District 14](/us/states/wv/districts/house/14.md) — 48% (state house)
- [WV House District 10](/us/states/wv/districts/house/10.md) — 39% (state house)
- [WV House District 13](/us/states/wv/districts/house/13.md) — 7% (state house)
- [WV House District 12](/us/states/wv/districts/house/12.md) — 4% (state house)
- [WV House District 11](/us/states/wv/districts/house/11.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
