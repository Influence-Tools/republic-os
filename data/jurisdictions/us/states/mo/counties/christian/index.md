---
type: Jurisdiction
title: "Christian County, MO"
classification: county
fips: "29043"
state: "MO"
demographics:
  population: 92915
  population_under_18: 23318
  population_18_64: 54040
  population_65_plus: 15557
  median_household_income: 83437
  poverty_rate: 8.17
  homeownership_rate: 75.91
  unemployment_rate: 3.36
  median_home_value: 274900
  gini_index: 0.4292
  vacancy_rate: 4.1
  race_white: 84787
  race_black: 653
  race_asian: 750
  race_native: 304
  hispanic: 3505
  bachelors_plus: 28494
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/138"
    rel: in-district
    area_weight: 0.5037
  - to: "us/states/mo/districts/house/140"
    rel: in-district
    area_weight: 0.263
  - to: "us/states/mo/districts/house/139"
    rel: in-district
    area_weight: 0.2331
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Christian County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92915 |
| Under 18 | 23318 |
| 18–64 | 54040 |
| 65+ | 15557 |
| Median household income | 83437 |
| Poverty rate | 8.17 |
| Homeownership rate | 75.91 |
| Unemployment rate | 3.36 |
| Median home value | 274900 |
| Gini index | 0.4292 |
| Vacancy rate | 4.1 |
| White | 84787 |
| Black | 653 |
| Asian | 750 |
| Native | 304 |
| Hispanic/Latino | 3505 |
| Bachelor's or higher | 28494 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 29](/us/states/mo/districts/senate/29.md) — 100% (state senate)
- [MO House District 138](/us/states/mo/districts/house/138.md) — 50% (state house)
- [MO House District 140](/us/states/mo/districts/house/140.md) — 26% (state house)
- [MO House District 139](/us/states/mo/districts/house/139.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
