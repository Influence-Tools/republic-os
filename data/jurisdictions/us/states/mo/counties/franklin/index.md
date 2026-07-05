---
type: Jurisdiction
title: "Franklin County, MO"
classification: county
fips: "29071"
state: "MO"
demographics:
  population: 105950
  population_under_18: 23693
  population_18_64: 61914
  population_65_plus: 20343
  median_household_income: 73165
  poverty_rate: 8.16
  homeownership_rate: 76.52
  unemployment_rate: 4.32
  median_home_value: 227600
  gini_index: 0.4198
  vacancy_rate: 7.07
  race_white: 94646
  race_black: 922
  race_asian: 490
  race_native: 76
  hispanic: 2461
  bachelors_plus: 23602
districts:
  - to: "us/states/mo/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mo/districts/senate/26"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/118"
    rel: in-district
    area_weight: 0.5434
  - to: "us/states/mo/districts/house/109"
    rel: in-district
    area_weight: 0.321
  - to: "us/states/mo/districts/house/119"
    rel: in-district
    area_weight: 0.1352
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Franklin County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 105950 |
| Under 18 | 23693 |
| 18–64 | 61914 |
| 65+ | 20343 |
| Median household income | 73165 |
| Poverty rate | 8.16 |
| Homeownership rate | 76.52 |
| Unemployment rate | 4.32 |
| Median home value | 227600 |
| Gini index | 0.4198 |
| Vacancy rate | 7.07 |
| White | 94646 |
| Black | 922 |
| Asian | 490 |
| Native | 76 |
| Hispanic/Latino | 2461 |
| Bachelor's or higher | 23602 |

## Districts

- [MO-02](/us/states/mo/districts/02.md) — 100% (congressional)
- [MO Senate District 26](/us/states/mo/districts/senate/26.md) — 100% (state senate)
- [MO House District 118](/us/states/mo/districts/house/118.md) — 54% (state house)
- [MO House District 109](/us/states/mo/districts/house/109.md) — 32% (state house)
- [MO House District 119](/us/states/mo/districts/house/119.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
