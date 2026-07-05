---
type: Jurisdiction
title: "Lincoln County, KY"
classification: county
fips: "21137"
state: "KY"
demographics:
  population: 24504
  population_under_18: 5971
  population_18_64: 13996
  population_65_plus: 4537
  median_household_income: 52440
  poverty_rate: 16.29
  homeownership_rate: 76.42
  unemployment_rate: 6.53
  median_home_value: 147300
  gini_index: 0.4605
  vacancy_rate: 11.27
  race_white: 22651
  race_black: 495
  race_asian: 23
  race_native: 1
  hispanic: 523
  bachelors_plus: 3824
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9928
  - to: "us/states/ky/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/80"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Lincoln County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24504 |
| Under 18 | 5971 |
| 18–64 | 13996 |
| 65+ | 4537 |
| Median household income | 52440 |
| Poverty rate | 16.29 |
| Homeownership rate | 76.42 |
| Unemployment rate | 6.53 |
| Median home value | 147300 |
| Gini index | 0.4605 |
| Vacancy rate | 11.27 |
| White | 22651 |
| Black | 495 |
| Asian | 23 |
| Native | 1 |
| Hispanic/Latino | 523 |
| Bachelor's or higher | 3824 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 99% (congressional)
- [KY Senate District 21](/us/states/ky/districts/senate/21.md) — 100% (state senate)
- [KY House District 80](/us/states/ky/districts/house/80.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
