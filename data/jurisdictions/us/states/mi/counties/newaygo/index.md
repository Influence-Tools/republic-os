---
type: Jurisdiction
title: "Newaygo County, MI"
classification: county
fips: "26123"
state: "MI"
demographics:
  population: 50792
  population_under_18: 11112
  population_18_64: 29168
  population_65_plus: 10512
  median_household_income: 63304
  poverty_rate: 12.82
  homeownership_rate: 86.55
  unemployment_rate: 4.36
  median_home_value: 186700
  gini_index: 0.4104
  vacancy_rate: 21.18
  race_white: 44881
  race_black: 407
  race_asian: 214
  race_native: 165
  hispanic: 3175
  bachelors_plus: 8634
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/101"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Newaygo County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50792 |
| Under 18 | 11112 |
| 18–64 | 29168 |
| 65+ | 10512 |
| Median household income | 63304 |
| Poverty rate | 12.82 |
| Homeownership rate | 86.55 |
| Unemployment rate | 4.36 |
| Median home value | 186700 |
| Gini index | 0.4104 |
| Vacancy rate | 21.18 |
| White | 44881 |
| Black | 407 |
| Asian | 214 |
| Native | 165 |
| Hispanic/Latino | 3175 |
| Bachelor's or higher | 8634 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 33](/us/states/mi/districts/senate/33.md) — 100% (state senate)
- [MI House District 101](/us/states/mi/districts/house/101.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
