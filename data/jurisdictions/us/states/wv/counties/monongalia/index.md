---
type: Jurisdiction
title: "Monongalia County, WV"
classification: county
fips: "54061"
state: "WV"
demographics:
  population: 107163
  population_under_18: 17265
  population_18_64: 75528
  population_65_plus: 14370
  median_household_income: 65346
  poverty_rate: 19.71
  homeownership_rate: 57.85
  unemployment_rate: 4.72
  median_home_value: 267700
  gini_index: 0.5149
  vacancy_rate: 10.62
  race_white: 93057
  race_black: 3486
  race_asian: 3738
  race_native: 98
  hispanic: 3397
  bachelors_plus: 50299
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.6897
  - to: "us/states/wv/districts/senate/13"
    rel: in-district
    area_weight: 0.3101
  - to: "us/states/wv/districts/house/77"
    rel: in-district
    area_weight: 0.6297
  - to: "us/states/wv/districts/house/78"
    rel: in-district
    area_weight: 0.1902
  - to: "us/states/wv/districts/house/82"
    rel: in-district
    area_weight: 0.1301
  - to: "us/states/wv/districts/house/80"
    rel: in-district
    area_weight: 0.021
  - to: "us/states/wv/districts/house/81"
    rel: in-district
    area_weight: 0.0164
  - to: "us/states/wv/districts/house/79"
    rel: in-district
    area_weight: 0.0123
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Monongalia County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 107163 |
| Under 18 | 17265 |
| 18–64 | 75528 |
| 65+ | 14370 |
| Median household income | 65346 |
| Poverty rate | 19.71 |
| Homeownership rate | 57.85 |
| Unemployment rate | 4.72 |
| Median home value | 267700 |
| Gini index | 0.5149 |
| Vacancy rate | 10.62 |
| White | 93057 |
| Black | 3486 |
| Asian | 3738 |
| Native | 98 |
| Hispanic/Latino | 3397 |
| Bachelor's or higher | 50299 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 69% (state senate)
- [WV Senate District 13](/us/states/wv/districts/senate/13.md) — 31% (state senate)
- [WV House District 77](/us/states/wv/districts/house/77.md) — 63% (state house)
- [WV House District 78](/us/states/wv/districts/house/78.md) — 19% (state house)
- [WV House District 82](/us/states/wv/districts/house/82.md) — 13% (state house)
- [WV House District 80](/us/states/wv/districts/house/80.md) — 2% (state house)
- [WV House District 81](/us/states/wv/districts/house/81.md) — 2% (state house)
- [WV House District 79](/us/states/wv/districts/house/79.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
