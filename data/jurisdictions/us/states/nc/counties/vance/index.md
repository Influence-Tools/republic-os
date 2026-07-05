---
type: Jurisdiction
title: "Vance County, NC"
classification: county
fips: "37181"
state: "NC"
demographics:
  population: 42322
  population_under_18: 10160
  population_18_64: 23999
  population_65_plus: 8163
  median_household_income: 50465
  poverty_rate: 19.79
  homeownership_rate: 60.15
  unemployment_rate: 8.22
  median_home_value: 161500
  gini_index: 0.454
  vacancy_rate: 17.15
  race_white: 16070
  race_black: 20032
  race_asian: 288
  race_native: 509
  hispanic: 4006
  bachelors_plus: 6283
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/nc/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/32"
    rel: in-district
    area_weight: 0.5938
  - to: "us/states/nc/districts/house/7"
    rel: in-district
    area_weight: 0.4061
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Vance County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42322 |
| Under 18 | 10160 |
| 18–64 | 23999 |
| 65+ | 8163 |
| Median household income | 50465 |
| Poverty rate | 19.79 |
| Homeownership rate | 60.15 |
| Unemployment rate | 8.22 |
| Median home value | 161500 |
| Gini index | 0.454 |
| Vacancy rate | 17.15 |
| White | 16070 |
| Black | 20032 |
| Asian | 288 |
| Native | 509 |
| Hispanic/Latino | 4006 |
| Bachelor's or higher | 6283 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 11](/us/states/nc/districts/senate/11.md) — 100% (state senate)
- [NC House District 32](/us/states/nc/districts/house/32.md) — 59% (state house)
- [NC House District 7](/us/states/nc/districts/house/7.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
