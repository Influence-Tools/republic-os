---
type: Jurisdiction
title: "Lincoln County, MS"
classification: county
fips: "28085"
state: "MS"
demographics:
  population: 34877
  population_under_18: 8045
  population_18_64: 20632
  population_65_plus: 6200
  median_household_income: 51119
  poverty_rate: 21.16
  homeownership_rate: 74.93
  unemployment_rate: 3.18
  median_home_value: 155800
  gini_index: 0.4712
  vacancy_rate: 17.59
  race_white: 23583
  race_black: 10469
  race_asian: 168
  race_native: 29
  hispanic: 455
  bachelors_plus: 6195
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/92"
    rel: in-district
    area_weight: 0.5893
  - to: "us/states/ms/districts/house/53"
    rel: in-district
    area_weight: 0.4107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lincoln County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34877 |
| Under 18 | 8045 |
| 18–64 | 20632 |
| 65+ | 6200 |
| Median household income | 51119 |
| Poverty rate | 21.16 |
| Homeownership rate | 74.93 |
| Unemployment rate | 3.18 |
| Median home value | 155800 |
| Gini index | 0.4712 |
| Vacancy rate | 17.59 |
| White | 23583 |
| Black | 10469 |
| Asian | 168 |
| Native | 29 |
| Hispanic/Latino | 455 |
| Bachelor's or higher | 6195 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 39](/us/states/ms/districts/senate/39.md) — 100% (state senate)
- [MS House District 92](/us/states/ms/districts/house/92.md) — 59% (state house)
- [MS House District 53](/us/states/ms/districts/house/53.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
