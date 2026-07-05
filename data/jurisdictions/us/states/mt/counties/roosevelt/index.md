---
type: Jurisdiction
title: "Roosevelt County, MT"
classification: county
fips: "30085"
state: "MT"
demographics:
  population: 10526
  population_under_18: 3465
  population_18_64: 5775
  population_65_plus: 1286
  median_household_income: 57063
  poverty_rate: 30.4
  homeownership_rate: 66.61
  unemployment_rate: 10.8
  median_home_value: 118800
  gini_index: 0.4581
  vacancy_rate: 23.98
  race_white: 3434
  race_black: 7
  race_asian: 100
  race_native: 6033
  hispanic: 301
  bachelors_plus: 1637
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/15"
    rel: in-district
    area_weight: 0.7582
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.2417
  - to: "us/states/mt/districts/house/29"
    rel: in-district
    area_weight: 0.6584
  - to: "us/states/mt/districts/house/31"
    rel: in-district
    area_weight: 0.2417
  - to: "us/states/mt/districts/house/30"
    rel: in-district
    area_weight: 0.0998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Roosevelt County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10526 |
| Under 18 | 3465 |
| 18–64 | 5775 |
| 65+ | 1286 |
| Median household income | 57063 |
| Poverty rate | 30.4 |
| Homeownership rate | 66.61 |
| Unemployment rate | 10.8 |
| Median home value | 118800 |
| Gini index | 0.4581 |
| Vacancy rate | 23.98 |
| White | 3434 |
| Black | 7 |
| Asian | 100 |
| Native | 6033 |
| Hispanic/Latino | 301 |
| Bachelor's or higher | 1637 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 15](/us/states/mt/districts/senate/15.md) — 76% (state senate)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 24% (state senate)
- [MT House District 29](/us/states/mt/districts/house/29.md) — 66% (state house)
- [MT House District 31](/us/states/mt/districts/house/31.md) — 24% (state house)
- [MT House District 30](/us/states/mt/districts/house/30.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
