---
type: Jurisdiction
title: "Orleans County, VT"
classification: county
fips: "50019"
state: "VT"
demographics:
  population: 27606
  population_under_18: 5346
  population_18_64: 15655
  population_65_plus: 6605
  median_household_income: 70103
  poverty_rate: 11.73
  homeownership_rate: 79.71
  unemployment_rate: 5.28
  median_home_value: 223400
  gini_index: 0.4403
  vacancy_rate: 27.93
  race_white: 25862
  race_black: 255
  race_asian: 213
  race_native: 124
  hispanic: 527
  bachelors_plus: 8645
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Orleans County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27606 |
| Under 18 | 5346 |
| 18–64 | 15655 |
| 65+ | 6605 |
| Median household income | 70103 |
| Poverty rate | 11.73 |
| Homeownership rate | 79.71 |
| Unemployment rate | 5.28 |
| Median home value | 223400 |
| Gini index | 0.4403 |
| Vacancy rate | 27.93 |
| White | 25862 |
| Black | 255 |
| Asian | 213 |
| Native | 124 |
| Hispanic/Latino | 527 |
| Bachelor's or higher | 8645 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
