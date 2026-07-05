---
type: Jurisdiction
title: "Wayne County, WV"
classification: county
fips: "54099"
state: "WV"
demographics:
  population: 38164
  population_under_18: 7783
  population_18_64: 21896
  population_65_plus: 8485
  median_household_income: 58878
  poverty_rate: 14.58
  homeownership_rate: 78.59
  unemployment_rate: 4.89
  median_home_value: 127100
  gini_index: 0.4621
  vacancy_rate: 13.69
  race_white: 36590
  race_black: 366
  race_asian: 17
  race_native: 0
  hispanic: 346
  bachelors_plus: 7680
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/wv/districts/senate/5"
    rel: in-district
    area_weight: 0.6711
  - to: "us/states/wv/districts/senate/6"
    rel: in-district
    area_weight: 0.3283
  - to: "us/states/wv/districts/house/29"
    rel: in-district
    area_weight: 0.6868
  - to: "us/states/wv/districts/house/28"
    rel: in-district
    area_weight: 0.2907
  - to: "us/states/wv/districts/house/27"
    rel: in-district
    area_weight: 0.0218
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Wayne County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38164 |
| Under 18 | 7783 |
| 18–64 | 21896 |
| 65+ | 8485 |
| Median household income | 58878 |
| Poverty rate | 14.58 |
| Homeownership rate | 78.59 |
| Unemployment rate | 4.89 |
| Median home value | 127100 |
| Gini index | 0.4621 |
| Vacancy rate | 13.69 |
| White | 36590 |
| Black | 366 |
| Asian | 17 |
| Native | 0 |
| Hispanic/Latino | 346 |
| Bachelor's or higher | 7680 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 5](/us/states/wv/districts/senate/5.md) — 67% (state senate)
- [WV Senate District 6](/us/states/wv/districts/senate/6.md) — 33% (state senate)
- [WV House District 29](/us/states/wv/districts/house/29.md) — 69% (state house)
- [WV House District 28](/us/states/wv/districts/house/28.md) — 29% (state house)
- [WV House District 27](/us/states/wv/districts/house/27.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
