---
type: Jurisdiction
title: "Montgomery County, MO"
classification: county
fips: "29139"
state: "MO"
demographics:
  population: 11426
  population_under_18: 2504
  population_18_64: 6583
  population_65_plus: 2339
  median_household_income: 65500
  poverty_rate: 13.89
  homeownership_rate: 73.45
  unemployment_rate: 2.99
  median_home_value: 178700
  gini_index: 0.4206
  vacancy_rate: 20.44
  race_white: 10635
  race_black: 97
  race_asian: 9
  race_native: 71
  hispanic: 266
  bachelors_plus: 1817
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/mo/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/61"
    rel: in-district
    area_weight: 0.6659
  - to: "us/states/mo/districts/house/42"
    rel: in-district
    area_weight: 0.334
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Montgomery County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11426 |
| Under 18 | 2504 |
| 18–64 | 6583 |
| 65+ | 2339 |
| Median household income | 65500 |
| Poverty rate | 13.89 |
| Homeownership rate | 73.45 |
| Unemployment rate | 2.99 |
| Median home value | 178700 |
| Gini index | 0.4206 |
| Vacancy rate | 20.44 |
| White | 10635 |
| Black | 97 |
| Asian | 9 |
| Native | 71 |
| Hispanic/Latino | 266 |
| Bachelor's or higher | 1817 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 10](/us/states/mo/districts/senate/10.md) — 100% (state senate)
- [MO House District 61](/us/states/mo/districts/house/61.md) — 67% (state house)
- [MO House District 42](/us/states/mo/districts/house/42.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
