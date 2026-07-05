---
type: Jurisdiction
title: "Scotland County, MO"
classification: county
fips: "29199"
state: "MO"
demographics:
  population: 4686
  population_under_18: 1399
  population_18_64: 2380
  population_65_plus: 907
  median_household_income: 68913
  poverty_rate: 7.31
  homeownership_rate: 82.39
  unemployment_rate: 0.24
  median_home_value: 158800
  gini_index: 0.3951
  vacancy_rate: 29.58
  race_white: 4500
  race_black: 6
  race_asian: 2
  race_native: 8
  hispanic: 9
  bachelors_plus: 608
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Scotland County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4686 |
| Under 18 | 1399 |
| 18–64 | 2380 |
| 65+ | 907 |
| Median household income | 68913 |
| Poverty rate | 7.31 |
| Homeownership rate | 82.39 |
| Unemployment rate | 0.24 |
| Median home value | 158800 |
| Gini index | 0.3951 |
| Vacancy rate | 29.58 |
| White | 4500 |
| Black | 6 |
| Asian | 2 |
| Native | 8 |
| Hispanic/Latino | 9 |
| Bachelor's or higher | 608 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
