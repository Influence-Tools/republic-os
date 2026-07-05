---
type: Jurisdiction
title: "Jasper County, MO"
classification: county
fips: "29097"
state: "MO"
demographics:
  population: 124357
  population_under_18: 30642
  population_18_64: 73664
  population_65_plus: 20051
  median_household_income: 60694
  poverty_rate: 16.97
  homeownership_rate: 62.8
  unemployment_rate: 3.63
  median_home_value: 166900
  gini_index: 0.4596
  vacancy_rate: 9.16
  race_white: 103636
  race_black: 2211
  race_asian: 1651
  race_native: 990
  hispanic: 12221
  bachelors_plus: 27388
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/127"
    rel: in-district
    area_weight: 0.4523
  - to: "us/states/mo/districts/house/163"
    rel: in-district
    area_weight: 0.3002
  - to: "us/states/mo/districts/house/162"
    rel: in-district
    area_weight: 0.2201
  - to: "us/states/mo/districts/house/161"
    rel: in-district
    area_weight: 0.0273
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Jasper County, MO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 124357 |
| Under 18 | 30642 |
| 18–64 | 73664 |
| 65+ | 20051 |
| Median household income | 60694 |
| Poverty rate | 16.97 |
| Homeownership rate | 62.8 |
| Unemployment rate | 3.63 |
| Median home value | 166900 |
| Gini index | 0.4596 |
| Vacancy rate | 9.16 |
| White | 103636 |
| Black | 2211 |
| Asian | 1651 |
| Native | 990 |
| Hispanic/Latino | 12221 |
| Bachelor's or higher | 27388 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 32](/us/states/mo/districts/senate/32.md) — 100% (state senate)
- [MO House District 127](/us/states/mo/districts/house/127.md) — 45% (state house)
- [MO House District 163](/us/states/mo/districts/house/163.md) — 30% (state house)
- [MO House District 162](/us/states/mo/districts/house/162.md) — 22% (state house)
- [MO House District 161](/us/states/mo/districts/house/161.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
