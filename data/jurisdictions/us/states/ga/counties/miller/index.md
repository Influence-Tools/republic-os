---
type: Jurisdiction
title: "Miller County, GA"
classification: county
fips: "13201"
state: "GA"
demographics:
  population: 5850
  population_under_18: 1315
  population_18_64: 3217
  population_65_plus: 1318
  median_household_income: 51425
  poverty_rate: 23.77
  homeownership_rate: 70.46
  unemployment_rate: 3.91
  median_home_value: 124000
  gini_index: 0.4668
  vacancy_rate: 9.91
  race_white: 3796
  race_black: 1648
  race_asian: 52
  race_native: 18
  hispanic: 194
  bachelors_plus: 1172
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Miller County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5850 |
| Under 18 | 1315 |
| 18–64 | 3217 |
| 65+ | 1318 |
| Median household income | 51425 |
| Poverty rate | 23.77 |
| Homeownership rate | 70.46 |
| Unemployment rate | 3.91 |
| Median home value | 124000 |
| Gini index | 0.4668 |
| Vacancy rate | 9.91 |
| White | 3796 |
| Black | 1648 |
| Asian | 52 |
| Native | 18 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 1172 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
