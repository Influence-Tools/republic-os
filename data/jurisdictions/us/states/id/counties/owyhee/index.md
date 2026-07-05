---
type: Jurisdiction
title: "Owyhee County, ID"
classification: county
fips: "16073"
state: "ID"
demographics:
  population: 12503
  population_under_18: 3056
  population_18_64: 7033
  population_65_plus: 2414
  median_household_income: 64406
  poverty_rate: 12.24
  homeownership_rate: 72.62
  unemployment_rate: 2.05
  median_home_value: 359800
  gini_index: 0.4076
  vacancy_rate: 10.89
  race_white: 8729
  race_black: 66
  race_asian: 17
  race_native: 611
  hispanic: 3103
  bachelors_plus: 1395
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/id/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Owyhee County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12503 |
| Under 18 | 3056 |
| 18–64 | 7033 |
| 65+ | 2414 |
| Median household income | 64406 |
| Poverty rate | 12.24 |
| Homeownership rate | 72.62 |
| Unemployment rate | 2.05 |
| Median home value | 359800 |
| Gini index | 0.4076 |
| Vacancy rate | 10.89 |
| White | 8729 |
| Black | 66 |
| Asian | 17 |
| Native | 611 |
| Hispanic/Latino | 3103 |
| Bachelor's or higher | 1395 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 23](/us/states/id/districts/senate/23.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
