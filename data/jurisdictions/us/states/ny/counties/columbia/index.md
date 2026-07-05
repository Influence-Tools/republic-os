---
type: Jurisdiction
title: "Columbia County, NY"
classification: county
fips: "36021"
state: "NY"
demographics:
  population: 61100
  population_under_18: 9724
  population_18_64: 35353
  population_65_plus: 16023
  median_household_income: 81528
  poverty_rate: 12.11
  homeownership_rate: 76.29
  unemployment_rate: 5.44
  median_home_value: 347100
  gini_index: 0.5099
  vacancy_rate: 20.26
  race_white: 50909
  race_black: 2208
  race_asian: 1323
  race_native: 119
  hispanic: 3827
  bachelors_plus: 28315
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/41"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/house/106"
    rel: in-district
    area_weight: 0.8146
  - to: "us/states/ny/districts/house/107"
    rel: in-district
    area_weight: 0.1854
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Columbia County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61100 |
| Under 18 | 9724 |
| 18–64 | 35353 |
| 65+ | 16023 |
| Median household income | 81528 |
| Poverty rate | 12.11 |
| Homeownership rate | 76.29 |
| Unemployment rate | 5.44 |
| Median home value | 347100 |
| Gini index | 0.5099 |
| Vacancy rate | 20.26 |
| White | 50909 |
| Black | 2208 |
| Asian | 1323 |
| Native | 119 |
| Hispanic/Latino | 3827 |
| Bachelor's or higher | 28315 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 41](/us/states/ny/districts/senate/41.md) — 100% (state senate)
- [NY House District 106](/us/states/ny/districts/house/106.md) — 81% (state house)
- [NY House District 107](/us/states/ny/districts/house/107.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
