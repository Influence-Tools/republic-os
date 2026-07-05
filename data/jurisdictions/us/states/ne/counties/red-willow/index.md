---
type: Jurisdiction
title: "Red Willow County, NE"
classification: county
fips: "31145"
state: "NE"
demographics:
  population: 10557
  population_under_18: 2367
  population_18_64: 5970
  population_65_plus: 2220
  median_household_income: 63697
  poverty_rate: 14.04
  homeownership_rate: 73.02
  unemployment_rate: 1.38
  median_home_value: 159600
  gini_index: 0.4581
  vacancy_rate: 12.54
  race_white: 9385
  race_black: 103
  race_asian: 27
  race_native: 17
  hispanic: 670
  bachelors_plus: 2306
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

# Red Willow County, NE

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10557 |
| Under 18 | 2367 |
| 18–64 | 5970 |
| 65+ | 2220 |
| Median household income | 63697 |
| Poverty rate | 14.04 |
| Homeownership rate | 73.02 |
| Unemployment rate | 1.38 |
| Median home value | 159600 |
| Gini index | 0.4581 |
| Vacancy rate | 12.54 |
| White | 9385 |
| Black | 103 |
| Asian | 27 |
| Native | 17 |
| Hispanic/Latino | 670 |
| Bachelor's or higher | 2306 |

## Districts

- [NE-03](/us/states/ne/districts/03.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
