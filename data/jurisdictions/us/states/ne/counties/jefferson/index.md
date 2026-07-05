---
type: Jurisdiction
title: "Jefferson County, NE"
classification: county
fips: "31095"
state: "NE"
demographics:
  population: 7161
  population_under_18: 1626
  population_18_64: 3756
  population_65_plus: 1779
  median_household_income: 59044
  poverty_rate: 10.13
  homeownership_rate: 74.87
  unemployment_rate: 1.17
  median_home_value: 129500
  gini_index: 0.4313
  vacancy_rate: 14.76
  race_white: 6664
  race_black: 22
  race_asian: 2
  race_native: 15
  hispanic: 420
  bachelors_plus: 1233
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Jefferson County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7161 |
| Under 18 | 1626 |
| 18–64 | 3756 |
| 65+ | 1779 |
| Median household income | 59044 |
| Poverty rate | 10.13 |
| Homeownership rate | 74.87 |
| Unemployment rate | 1.17 |
| Median home value | 129500 |
| Gini index | 0.4313 |
| Vacancy rate | 14.76 |
| White | 6664 |
| Black | 22 |
| Asian | 2 |
| Native | 15 |
| Hispanic/Latino | 420 |
| Bachelor's or higher | 1233 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
