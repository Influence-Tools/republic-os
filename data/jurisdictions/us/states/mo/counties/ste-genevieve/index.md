---
type: Jurisdiction
title: "Ste. Genevieve County, MO"
classification: county
fips: "29186"
state: "MO"
demographics:
  population: 18571
  population_under_18: 3973
  population_18_64: 10613
  population_65_plus: 3985
  median_household_income: 66339
  poverty_rate: 8.15
  homeownership_rate: 82.96
  unemployment_rate: 4.22
  median_home_value: 222200
  gini_index: 0.4123
  vacancy_rate: 14.28
  race_white: 17445
  race_black: 227
  race_asian: 9
  race_native: 17
  hispanic: 279
  bachelors_plus: 2987
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/mo/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/145"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Ste. Genevieve County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18571 |
| Under 18 | 3973 |
| 18–64 | 10613 |
| 65+ | 3985 |
| Median household income | 66339 |
| Poverty rate | 8.15 |
| Homeownership rate | 82.96 |
| Unemployment rate | 4.22 |
| Median home value | 222200 |
| Gini index | 0.4123 |
| Vacancy rate | 14.28 |
| White | 17445 |
| Black | 227 |
| Asian | 9 |
| Native | 17 |
| Hispanic/Latino | 279 |
| Bachelor's or higher | 2987 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 3](/us/states/mo/districts/senate/3.md) — 100% (state senate)
- [MO House District 145](/us/states/mo/districts/house/145.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
