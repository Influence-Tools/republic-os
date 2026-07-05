---
type: Jurisdiction
title: "Maui County, HI"
classification: county
fips: "15009"
state: "HI"
demographics:
  population: 164522
  population_under_18: 34507
  population_18_64: 95886
  population_65_plus: 34129
  median_household_income: 97161
  poverty_rate: 9.17
  homeownership_rate: 65.61
  unemployment_rate: 5.49
  median_home_value: 904700
  gini_index: 0.4575
  vacancy_rate: 22.74
  race_white: 49680
  race_black: 1388
  race_asian: 46338
  race_native: 549
  hispanic: 17435
  bachelors_plus: 49219
districts:
  - to: "us/states/hi/districts/02"
    rel: in-district
    area_weight: 0.4863
  - to: "us/states/hi/districts/senate/7"
    rel: in-district
    area_weight: 0.3875
  - to: "us/states/hi/districts/senate/6"
    rel: in-district
    area_weight: 0.0694
  - to: "us/states/hi/districts/senate/5"
    rel: in-district
    area_weight: 0.0295
  - to: "us/states/hi/districts/house/13"
    rel: in-district
    area_weight: 0.2915
  - to: "us/states/hi/districts/house/12"
    rel: in-district
    area_weight: 0.1027
  - to: "us/states/hi/districts/house/14"
    rel: in-district
    area_weight: 0.0587
  - to: "us/states/hi/districts/house/11"
    rel: in-district
    area_weight: 0.015
  - to: "us/states/hi/districts/house/10"
    rel: in-district
    area_weight: 0.0094
  - to: "us/states/hi/districts/house/9"
    rel: in-district
    area_weight: 0.0091
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, hi]
timestamp: "2026-07-03"
---

# Maui County, HI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 164522 |
| Under 18 | 34507 |
| 18–64 | 95886 |
| 65+ | 34129 |
| Median household income | 97161 |
| Poverty rate | 9.17 |
| Homeownership rate | 65.61 |
| Unemployment rate | 5.49 |
| Median home value | 904700 |
| Gini index | 0.4575 |
| Vacancy rate | 22.74 |
| White | 49680 |
| Black | 1388 |
| Asian | 46338 |
| Native | 549 |
| Hispanic/Latino | 17435 |
| Bachelor's or higher | 49219 |

## Districts

- [HI-02](/us/states/hi/districts/02.md) — 49% (congressional)
- [HI Senate District 7](/us/states/hi/districts/senate/7.md) — 39% (state senate)
- [HI Senate District 6](/us/states/hi/districts/senate/6.md) — 7% (state senate)
- [HI Senate District 5](/us/states/hi/districts/senate/5.md) — 3% (state senate)
- [HI House District 13](/us/states/hi/districts/house/13.md) — 29% (state house)
- [HI House District 12](/us/states/hi/districts/house/12.md) — 10% (state house)
- [HI House District 14](/us/states/hi/districts/house/14.md) — 6% (state house)
- [HI House District 11](/us/states/hi/districts/house/11.md) — 2% (state house)
- [HI House District 10](/us/states/hi/districts/house/10.md) — 1% (state house)
- [HI House District 9](/us/states/hi/districts/house/9.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
