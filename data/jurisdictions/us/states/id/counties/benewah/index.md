---
type: Jurisdiction
title: "Benewah County, ID"
classification: county
fips: "16009"
state: "ID"
demographics:
  population: 10142
  population_under_18: 2235
  population_18_64: 5481
  population_65_plus: 2426
  median_household_income: 59794
  poverty_rate: 12.89
  homeownership_rate: 73.18
  unemployment_rate: 3.7
  median_home_value: 293500
  gini_index: 0.4423
  vacancy_rate: 14.4
  race_white: 8549
  race_black: 55
  race_asian: 1
  race_native: 839
  hispanic: 387
  bachelors_plus: 1906
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/2"
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

# Benewah County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10142 |
| Under 18 | 2235 |
| 18–64 | 5481 |
| 65+ | 2426 |
| Median household income | 59794 |
| Poverty rate | 12.89 |
| Homeownership rate | 73.18 |
| Unemployment rate | 3.7 |
| Median home value | 293500 |
| Gini index | 0.4423 |
| Vacancy rate | 14.4 |
| White | 8549 |
| Black | 55 |
| Asian | 1 |
| Native | 839 |
| Hispanic/Latino | 387 |
| Bachelor's or higher | 1906 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 2](/us/states/id/districts/senate/2.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
