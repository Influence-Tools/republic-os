---
type: Jurisdiction
title: "Henry County, KY"
classification: county
fips: "21103"
state: "KY"
demographics:
  population: 15856
  population_under_18: 3722
  population_18_64: 9220
  population_65_plus: 2914
  median_household_income: 63347
  poverty_rate: 16.42
  homeownership_rate: 76.26
  unemployment_rate: 4.96
  median_home_value: 197900
  gini_index: 0.4493
  vacancy_rate: 8.32
  race_white: 14304
  race_black: 421
  race_asian: 78
  race_native: 53
  hispanic: 651
  bachelors_plus: 2300
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/senate/7"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Henry County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15856 |
| Under 18 | 3722 |
| 18–64 | 9220 |
| 65+ | 2914 |
| Median household income | 63347 |
| Poverty rate | 16.42 |
| Homeownership rate | 76.26 |
| Unemployment rate | 4.96 |
| Median home value | 197900 |
| Gini index | 0.4493 |
| Vacancy rate | 8.32 |
| White | 14304 |
| Black | 421 |
| Asian | 78 |
| Native | 53 |
| Hispanic/Latino | 651 |
| Bachelor's or higher | 2300 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 7](/us/states/ky/districts/senate/7.md) — 100% (state senate)
- [KY House District 47](/us/states/ky/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
