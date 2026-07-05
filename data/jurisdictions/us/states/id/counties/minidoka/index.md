---
type: Jurisdiction
title: "Minidoka County, ID"
classification: county
fips: "16067"
state: "ID"
demographics:
  population: 22208
  population_under_18: 6265
  population_18_64: 12367
  population_65_plus: 3576
  median_household_income: 70377
  poverty_rate: 14.54
  homeownership_rate: 69.17
  unemployment_rate: 3.43
  median_home_value: 262600
  gini_index: 0.4419
  vacancy_rate: 6.21
  race_white: 14884
  race_black: 22
  race_asian: 94
  race_native: 407
  hispanic: 8227
  bachelors_plus: 3103
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/27"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Minidoka County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22208 |
| Under 18 | 6265 |
| 18–64 | 12367 |
| 65+ | 3576 |
| Median household income | 70377 |
| Poverty rate | 14.54 |
| Homeownership rate | 69.17 |
| Unemployment rate | 3.43 |
| Median home value | 262600 |
| Gini index | 0.4419 |
| Vacancy rate | 6.21 |
| White | 14884 |
| Black | 22 |
| Asian | 94 |
| Native | 407 |
| Hispanic/Latino | 8227 |
| Bachelor's or higher | 3103 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 27](/us/states/id/districts/senate/27.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
