---
type: Jurisdiction
title: "St. Francois County, MO"
classification: county
fips: "29187"
state: "MO"
demographics:
  population: 66999
  population_under_18: 14011
  population_18_64: 41449
  population_65_plus: 11539
  median_household_income: 57477
  poverty_rate: 15.94
  homeownership_rate: 68.2
  unemployment_rate: 4.53
  median_home_value: 169300
  gini_index: 0.4366
  vacancy_rate: 14.26
  race_white: 60518
  race_black: 1873
  race_asian: 253
  race_native: 239
  hispanic: 1268
  bachelors_plus: 11093
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/117"
    rel: in-district
    area_weight: 0.5228
  - to: "us/states/mo/districts/house/116"
    rel: in-district
    area_weight: 0.4769
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# St. Francois County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66999 |
| Under 18 | 14011 |
| 18–64 | 41449 |
| 65+ | 11539 |
| Median household income | 57477 |
| Poverty rate | 15.94 |
| Homeownership rate | 68.2 |
| Unemployment rate | 4.53 |
| Median home value | 169300 |
| Gini index | 0.4366 |
| Vacancy rate | 14.26 |
| White | 60518 |
| Black | 1873 |
| Asian | 253 |
| Native | 239 |
| Hispanic/Latino | 1268 |
| Bachelor's or higher | 11093 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 3](/us/states/mo/districts/senate/3.md) — 100% (state senate)
- [MO House District 117](/us/states/mo/districts/house/117.md) — 52% (state house)
- [MO House District 116](/us/states/mo/districts/house/116.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
