---
type: Jurisdiction
title: "Hawaii County, HI"
classification: county
fips: "15001"
state: "HI"
demographics:
  population: 205769
  population_under_18: 42438
  population_18_64: 114330
  population_65_plus: 49001
  median_household_income: 78639
  poverty_rate: 14.94
  homeownership_rate: 73.98
  unemployment_rate: 6.0
  median_home_value: 519300
  gini_index: 0.4804
  vacancy_rate: 18.36
  race_white: 63553
  race_black: 1678
  race_asian: 42748
  race_native: 921
  hispanic: 24003
  bachelors_plus: 65444
districts:
  - to: "us/states/hi/districts/02"
    rel: in-district
    area_weight: 0.7904
  - to: "us/states/hi/districts/senate/4"
    rel: in-district
    area_weight: 0.3224
  - to: "us/states/hi/districts/senate/3"
    rel: in-district
    area_weight: 0.3125
  - to: "us/states/hi/districts/senate/2"
    rel: in-district
    area_weight: 0.0873
  - to: "us/states/hi/districts/senate/1"
    rel: in-district
    area_weight: 0.0708
  - to: "us/states/hi/districts/house/5"
    rel: in-district
    area_weight: 0.3561
  - to: "us/states/hi/districts/house/1"
    rel: in-district
    area_weight: 0.1543
  - to: "us/states/hi/districts/house/7"
    rel: in-district
    area_weight: 0.0954
  - to: "us/states/hi/districts/house/8"
    rel: in-district
    area_weight: 0.0873
  - to: "us/states/hi/districts/house/4"
    rel: in-district
    area_weight: 0.0557
  - to: "us/states/hi/districts/house/6"
    rel: in-district
    area_weight: 0.0218
  - to: "us/states/hi/districts/house/3"
    rel: in-district
    area_weight: 0.0181
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, hi]
timestamp: "2026-07-03"
---

# Hawaii County, HI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 205769 |
| Under 18 | 42438 |
| 18–64 | 114330 |
| 65+ | 49001 |
| Median household income | 78639 |
| Poverty rate | 14.94 |
| Homeownership rate | 73.98 |
| Unemployment rate | 6.0 |
| Median home value | 519300 |
| Gini index | 0.4804 |
| Vacancy rate | 18.36 |
| White | 63553 |
| Black | 1678 |
| Asian | 42748 |
| Native | 921 |
| Hispanic/Latino | 24003 |
| Bachelor's or higher | 65444 |

## Districts

- [HI-02](/us/states/hi/districts/02.md) — 79% (congressional)
- [HI Senate District 4](/us/states/hi/districts/senate/4.md) — 32% (state senate)
- [HI Senate District 3](/us/states/hi/districts/senate/3.md) — 31% (state senate)
- [HI Senate District 2](/us/states/hi/districts/senate/2.md) — 9% (state senate)
- [HI Senate District 1](/us/states/hi/districts/senate/1.md) — 7% (state senate)
- [HI House District 5](/us/states/hi/districts/house/5.md) — 36% (state house)
- [HI House District 1](/us/states/hi/districts/house/1.md) — 15% (state house)
- [HI House District 7](/us/states/hi/districts/house/7.md) — 10% (state house)
- [HI House District 8](/us/states/hi/districts/house/8.md) — 9% (state house)
- [HI House District 4](/us/states/hi/districts/house/4.md) — 6% (state house)
- [HI House District 6](/us/states/hi/districts/house/6.md) — 2% (state house)
- [HI House District 3](/us/states/hi/districts/house/3.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
