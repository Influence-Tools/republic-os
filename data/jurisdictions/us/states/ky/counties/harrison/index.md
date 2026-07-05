---
type: Jurisdiction
title: "Harrison County, KY"
classification: county
fips: "21097"
state: "KY"
demographics:
  population: 19140
  population_under_18: 4476
  population_18_64: 10998
  population_65_plus: 3666
  median_household_income: 66442
  poverty_rate: 17.14
  homeownership_rate: 71.42
  unemployment_rate: 3.23
  median_home_value: 202100
  gini_index: 0.4609
  vacancy_rate: 10.91
  race_white: 17927
  race_black: 334
  race_asian: 16
  race_native: 11
  hispanic: 446
  bachelors_plus: 4282
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9945
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.0055
  - to: "us/states/ky/districts/senate/27"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/70"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Harrison County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19140 |
| Under 18 | 4476 |
| 18–64 | 10998 |
| 65+ | 3666 |
| Median household income | 66442 |
| Poverty rate | 17.14 |
| Homeownership rate | 71.42 |
| Unemployment rate | 3.23 |
| Median home value | 202100 |
| Gini index | 0.4609 |
| Vacancy rate | 10.91 |
| White | 17927 |
| Black | 334 |
| Asian | 16 |
| Native | 11 |
| Hispanic/Latino | 446 |
| Bachelor's or higher | 4282 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 99% (congressional)
- [KY-06](/us/states/ky/districts/06.md) — 1% (congressional)
- [KY Senate District 27](/us/states/ky/districts/senate/27.md) — 100% (state senate)
- [KY House District 70](/us/states/ky/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
