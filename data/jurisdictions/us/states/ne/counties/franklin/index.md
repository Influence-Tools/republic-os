---
type: Jurisdiction
title: "Franklin County, NE"
classification: county
fips: "31061"
state: "NE"
demographics:
  population: 2846
  population_under_18: 576
  population_18_64: 1470
  population_65_plus: 800
  median_household_income: 60195
  poverty_rate: 12.27
  homeownership_rate: 83.22
  unemployment_rate: 2.66
  median_home_value: 95600
  gini_index: 0.5032
  vacancy_rate: 15.55
  race_white: 2667
  race_black: 5
  race_asian: 0
  race_native: 16
  hispanic: 99
  bachelors_plus: 589
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

# Franklin County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2846 |
| Under 18 | 576 |
| 18–64 | 1470 |
| 65+ | 800 |
| Median household income | 60195 |
| Poverty rate | 12.27 |
| Homeownership rate | 83.22 |
| Unemployment rate | 2.66 |
| Median home value | 95600 |
| Gini index | 0.5032 |
| Vacancy rate | 15.55 |
| White | 2667 |
| Black | 5 |
| Asian | 0 |
| Native | 16 |
| Hispanic/Latino | 99 |
| Bachelor's or higher | 589 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
