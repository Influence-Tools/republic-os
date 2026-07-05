---
type: Jurisdiction
title: "Sullivan County, MO"
classification: county
fips: "29211"
state: "MO"
demographics:
  population: 5857
  population_under_18: 1309
  population_18_64: 3330
  population_65_plus: 1218
  median_household_income: 56964
  poverty_rate: 13.67
  homeownership_rate: 75.15
  unemployment_rate: 2.46
  median_home_value: 115600
  gini_index: 0.4367
  vacancy_rate: 32.23
  race_white: 4691
  race_black: 157
  race_asian: 60
  race_native: 24
  hispanic: 1059
  bachelors_plus: 893
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/3"
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

# Sullivan County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5857 |
| Under 18 | 1309 |
| 18–64 | 3330 |
| 65+ | 1218 |
| Median household income | 56964 |
| Poverty rate | 13.67 |
| Homeownership rate | 75.15 |
| Unemployment rate | 2.46 |
| Median home value | 115600 |
| Gini index | 0.4367 |
| Vacancy rate | 32.23 |
| White | 4691 |
| Black | 157 |
| Asian | 60 |
| Native | 24 |
| Hispanic/Latino | 1059 |
| Bachelor's or higher | 893 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 3](/us/states/mo/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
