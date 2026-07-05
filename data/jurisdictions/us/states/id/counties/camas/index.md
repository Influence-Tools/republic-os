---
type: Jurisdiction
title: "Camas County, ID"
classification: county
fips: "16025"
state: "ID"
demographics:
  population: 1124
  population_under_18: 297
  population_18_64: 610
  population_65_plus: 217
  median_household_income: 57955
  poverty_rate: 5.87
  homeownership_rate: 80.0
  unemployment_rate: 0.0
  median_home_value: 304000
  gini_index: 0.4234
  vacancy_rate: 47.37
  race_white: 867
  race_black: 0
  race_asian: 0
  race_native: 21
  hispanic: 157
  bachelors_plus: 349
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/24"
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

# Camas County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1124 |
| Under 18 | 297 |
| 18–64 | 610 |
| 65+ | 217 |
| Median household income | 57955 |
| Poverty rate | 5.87 |
| Homeownership rate | 80.0 |
| Unemployment rate | 0.0 |
| Median home value | 304000 |
| Gini index | 0.4234 |
| Vacancy rate | 47.37 |
| White | 867 |
| Black | 0 |
| Asian | 0 |
| Native | 21 |
| Hispanic/Latino | 157 |
| Bachelor's or higher | 349 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 24](/us/states/id/districts/senate/24.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
