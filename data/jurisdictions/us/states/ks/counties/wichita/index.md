---
type: Jurisdiction
title: "Wichita County, KS"
classification: county
fips: "20203"
state: "KS"
demographics:
  population: 2091
  population_under_18: 635
  population_18_64: 954
  population_65_plus: 502
  median_household_income: 79063
  poverty_rate: 16.53
  homeownership_rate: 78.03
  unemployment_rate: 0.78
  median_home_value: 99300
  gini_index: 0.4754
  vacancy_rate: 10.43
  race_white: 1527
  race_black: 4
  race_asian: 0
  race_native: 8
  hispanic: 575
  bachelors_plus: 355
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/118"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Wichita County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2091 |
| Under 18 | 635 |
| 18–64 | 954 |
| 65+ | 502 |
| Median household income | 79063 |
| Poverty rate | 16.53 |
| Homeownership rate | 78.03 |
| Unemployment rate | 0.78 |
| Median home value | 99300 |
| Gini index | 0.4754 |
| Vacancy rate | 10.43 |
| White | 1527 |
| Black | 4 |
| Asian | 0 |
| Native | 8 |
| Hispanic/Latino | 575 |
| Bachelor's or higher | 355 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
