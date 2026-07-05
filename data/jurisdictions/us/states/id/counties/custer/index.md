---
type: Jurisdiction
title: "Custer County, ID"
classification: county
fips: "16037"
state: "ID"
demographics:
  population: 4470
  population_under_18: 623
  population_18_64: 2213
  population_65_plus: 1634
  median_household_income: 67574
  poverty_rate: 15.78
  homeownership_rate: 76.79
  unemployment_rate: 2.04
  median_home_value: 381700
  gini_index: 0.4224
  vacancy_rate: 38.06
  race_white: 3985
  race_black: 14
  race_asian: 137
  race_native: 17
  hispanic: 201
  bachelors_plus: 1329
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/id/districts/senate/8"
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

# Custer County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4470 |
| Under 18 | 623 |
| 18–64 | 2213 |
| 65+ | 1634 |
| Median household income | 67574 |
| Poverty rate | 15.78 |
| Homeownership rate | 76.79 |
| Unemployment rate | 2.04 |
| Median home value | 381700 |
| Gini index | 0.4224 |
| Vacancy rate | 38.06 |
| White | 3985 |
| Black | 14 |
| Asian | 137 |
| Native | 17 |
| Hispanic/Latino | 201 |
| Bachelor's or higher | 1329 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 8](/us/states/id/districts/senate/8.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
