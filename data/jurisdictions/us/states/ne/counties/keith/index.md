---
type: Jurisdiction
title: "Keith County, NE"
classification: county
fips: "31101"
state: "NE"
demographics:
  population: 8219
  population_under_18: 1692
  population_18_64: 4233
  population_65_plus: 2294
  median_household_income: 60645
  poverty_rate: 10.37
  homeownership_rate: 71.12
  unemployment_rate: 2.03
  median_home_value: 168000
  gini_index: 0.4209
  vacancy_rate: 25.46
  race_white: 7190
  race_black: 91
  race_asian: 59
  race_native: 20
  hispanic: 749
  bachelors_plus: 1766
districts:
  - to: "us/states/ne/districts/03"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ne]
timestamp: "2026-07-03"
---

# Keith County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8219 |
| Under 18 | 1692 |
| 18–64 | 4233 |
| 65+ | 2294 |
| Median household income | 60645 |
| Poverty rate | 10.37 |
| Homeownership rate | 71.12 |
| Unemployment rate | 2.03 |
| Median home value | 168000 |
| Gini index | 0.4209 |
| Vacancy rate | 25.46 |
| White | 7190 |
| Black | 91 |
| Asian | 59 |
| Native | 20 |
| Hispanic/Latino | 749 |
| Bachelor's or higher | 1766 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
