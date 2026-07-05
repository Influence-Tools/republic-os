---
type: Jurisdiction
title: "Cedar County, NE"
classification: county
fips: "31027"
state: "NE"
demographics:
  population: 8315
  population_under_18: 2122
  population_18_64: 4336
  population_65_plus: 1857
  median_household_income: 73578
  poverty_rate: 7.07
  homeownership_rate: 79.56
  unemployment_rate: 1.73
  median_home_value: 185000
  gini_index: 0.4259
  vacancy_rate: 11.67
  race_white: 7945
  race_black: 12
  race_asian: 24
  race_native: 18
  hispanic: 211
  bachelors_plus: 1721
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

# Cedar County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8315 |
| Under 18 | 2122 |
| 18–64 | 4336 |
| 65+ | 1857 |
| Median household income | 73578 |
| Poverty rate | 7.07 |
| Homeownership rate | 79.56 |
| Unemployment rate | 1.73 |
| Median home value | 185000 |
| Gini index | 0.4259 |
| Vacancy rate | 11.67 |
| White | 7945 |
| Black | 12 |
| Asian | 24 |
| Native | 18 |
| Hispanic/Latino | 211 |
| Bachelor's or higher | 1721 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
