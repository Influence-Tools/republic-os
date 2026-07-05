---
type: Jurisdiction
title: "Taylor County, WV"
classification: county
fips: "54091"
state: "WV"
demographics:
  population: 16487
  population_under_18: 3376
  population_18_64: 9594
  population_65_plus: 3517
  median_household_income: 57795
  poverty_rate: 13.86
  homeownership_rate: 83.93
  unemployment_rate: 7.51
  median_home_value: 148800
  gini_index: 0.4368
  vacancy_rate: 11.15
  race_white: 15680
  race_black: 114
  race_asian: 0
  race_native: 22
  hispanic: 169
  bachelors_plus: 3531
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/12"
    rel: in-district
    area_weight: 0.5356
  - to: "us/states/wv/districts/senate/14"
    rel: in-district
    area_weight: 0.464
  - to: "us/states/wv/districts/house/73"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Taylor County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16487 |
| Under 18 | 3376 |
| 18–64 | 9594 |
| 65+ | 3517 |
| Median household income | 57795 |
| Poverty rate | 13.86 |
| Homeownership rate | 83.93 |
| Unemployment rate | 7.51 |
| Median home value | 148800 |
| Gini index | 0.4368 |
| Vacancy rate | 11.15 |
| White | 15680 |
| Black | 114 |
| Asian | 0 |
| Native | 22 |
| Hispanic/Latino | 169 |
| Bachelor's or higher | 3531 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 12](/us/states/wv/districts/senate/12.md) — 54% (state senate)
- [WV Senate District 14](/us/states/wv/districts/senate/14.md) — 46% (state senate)
- [WV House District 73](/us/states/wv/districts/house/73.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
