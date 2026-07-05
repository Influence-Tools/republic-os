---
type: Jurisdiction
title: "Sierra County, CA"
classification: county
fips: "06091"
state: "CA"
demographics:
  population: 2746
  population_under_18: 397
  population_18_64: 1386
  population_65_plus: 963
  median_household_income: 63355
  poverty_rate: 4.44
  homeownership_rate: 72.11
  unemployment_rate: 12.63
  median_home_value: 331900
  gini_index: 0.4339
  vacancy_rate: 42.5
  race_white: 2373
  race_black: 8
  race_asian: 0
  race_native: 0
  hispanic: 301
  bachelors_plus: 731
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Sierra County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2746 |
| Under 18 | 397 |
| 18–64 | 1386 |
| 65+ | 963 |
| Median household income | 63355 |
| Poverty rate | 4.44 |
| Homeownership rate | 72.11 |
| Unemployment rate | 12.63 |
| Median home value | 331900 |
| Gini index | 0.4339 |
| Vacancy rate | 42.5 |
| White | 2373 |
| Black | 8 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 301 |
| Bachelor's or higher | 731 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
