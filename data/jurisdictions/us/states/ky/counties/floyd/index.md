---
type: Jurisdiction
title: "Floyd County, KY"
classification: county
fips: "21071"
state: "KY"
demographics:
  population: 35224
  population_under_18: 7729
  population_18_64: 20588
  population_65_plus: 6907
  median_household_income: 41279
  poverty_rate: 28.05
  homeownership_rate: 72.18
  unemployment_rate: 7.67
  median_home_value: 98700
  gini_index: 0.4892
  vacancy_rate: 16.02
  race_white: 33726
  race_black: 195
  race_asian: 134
  race_native: 17
  hispanic: 329
  bachelors_plus: 5537
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/29"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/house/95"
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

# Floyd County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35224 |
| Under 18 | 7729 |
| 18–64 | 20588 |
| 65+ | 6907 |
| Median household income | 41279 |
| Poverty rate | 28.05 |
| Homeownership rate | 72.18 |
| Unemployment rate | 7.67 |
| Median home value | 98700 |
| Gini index | 0.4892 |
| Vacancy rate | 16.02 |
| White | 33726 |
| Black | 195 |
| Asian | 134 |
| Native | 17 |
| Hispanic/Latino | 329 |
| Bachelor's or higher | 5537 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 29](/us/states/ky/districts/senate/29.md) — 100% (state senate)
- [KY House District 95](/us/states/ky/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
