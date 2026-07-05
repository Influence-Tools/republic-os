---
type: Jurisdiction
title: "Power County, ID"
classification: county
fips: "16077"
state: "ID"
demographics:
  population: 8133
  population_under_18: 2423
  population_18_64: 4329
  population_65_plus: 1381
  median_household_income: 61146
  poverty_rate: 9.47
  homeownership_rate: 73.68
  unemployment_rate: 5.62
  median_home_value: 212900
  gini_index: 0.3834
  vacancy_rate: 5.09
  race_white: 5093
  race_black: 36
  race_asian: 0
  race_native: 119
  hispanic: 2787
  bachelors_plus: 993
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/28"
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

# Power County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8133 |
| Under 18 | 2423 |
| 18–64 | 4329 |
| 65+ | 1381 |
| Median household income | 61146 |
| Poverty rate | 9.47 |
| Homeownership rate | 73.68 |
| Unemployment rate | 5.62 |
| Median home value | 212900 |
| Gini index | 0.3834 |
| Vacancy rate | 5.09 |
| White | 5093 |
| Black | 36 |
| Asian | 0 |
| Native | 119 |
| Hispanic/Latino | 2787 |
| Bachelor's or higher | 993 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 28](/us/states/id/districts/senate/28.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
