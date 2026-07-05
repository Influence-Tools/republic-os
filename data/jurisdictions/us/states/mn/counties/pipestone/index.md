---
type: Jurisdiction
title: "Pipestone County, MN"
classification: county
fips: "27117"
state: "MN"
demographics:
  population: 9284
  population_under_18: 2494
  population_18_64: 4882
  population_65_plus: 1908
  median_household_income: 69628
  poverty_rate: 10.53
  homeownership_rate: 80.81
  unemployment_rate: 3.2
  median_home_value: 140200
  gini_index: 0.4331
  vacancy_rate: 8.18
  race_white: 7985
  race_black: 118
  race_asian: 102
  race_native: 116
  hispanic: 799
  bachelors_plus: 1769
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Pipestone County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9284 |
| Under 18 | 2494 |
| 18–64 | 4882 |
| 65+ | 1908 |
| Median household income | 69628 |
| Poverty rate | 10.53 |
| Homeownership rate | 80.81 |
| Unemployment rate | 3.2 |
| Median home value | 140200 |
| Gini index | 0.4331 |
| Vacancy rate | 8.18 |
| White | 7985 |
| Black | 118 |
| Asian | 102 |
| Native | 116 |
| Hispanic/Latino | 799 |
| Bachelor's or higher | 1769 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
