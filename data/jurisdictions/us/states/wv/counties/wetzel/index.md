---
type: Jurisdiction
title: "Wetzel County, WV"
classification: county
fips: "54103"
state: "WV"
demographics:
  population: 14078
  population_under_18: 2988
  population_18_64: 7871
  population_65_plus: 3219
  median_household_income: 56836
  poverty_rate: 16.0
  homeownership_rate: 83.15
  unemployment_rate: 5.42
  median_home_value: 107900
  gini_index: 0.4416
  vacancy_rate: 16.23
  race_white: 13327
  race_black: 26
  race_asian: 6
  race_native: 0
  hispanic: 196
  bachelors_plus: 2411
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/house/72"
    rel: in-district
    area_weight: 0.4053
  - to: "us/states/wv/districts/house/8"
    rel: in-district
    area_weight: 0.3126
  - to: "us/states/wv/districts/house/7"
    rel: in-district
    area_weight: 0.2478
  - to: "us/states/wv/districts/house/77"
    rel: in-district
    area_weight: 0.0342
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Wetzel County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14078 |
| Under 18 | 2988 |
| 18–64 | 7871 |
| 65+ | 3219 |
| Median household income | 56836 |
| Poverty rate | 16.0 |
| Homeownership rate | 83.15 |
| Unemployment rate | 5.42 |
| Median home value | 107900 |
| Gini index | 0.4416 |
| Vacancy rate | 16.23 |
| White | 13327 |
| Black | 26 |
| Asian | 6 |
| Native | 0 |
| Hispanic/Latino | 196 |
| Bachelor's or higher | 2411 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 100% (state senate)
- [WV House District 72](/us/states/wv/districts/house/72.md) — 41% (state house)
- [WV House District 8](/us/states/wv/districts/house/8.md) — 31% (state house)
- [WV House District 7](/us/states/wv/districts/house/7.md) — 25% (state house)
- [WV House District 77](/us/states/wv/districts/house/77.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
