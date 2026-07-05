---
type: Jurisdiction
title: "Bonner County, ID"
classification: county
fips: "16017"
state: "ID"
demographics:
  population: 51049
  population_under_18: 9996
  population_18_64: 27576
  population_65_plus: 13477
  median_household_income: 66979
  poverty_rate: 11.12
  homeownership_rate: 78.28
  unemployment_rate: 4.82
  median_home_value: 487900
  gini_index: 0.4828
  vacancy_rate: 24.51
  race_white: 45936
  race_black: 177
  race_asian: 279
  race_native: 221
  hispanic: 2028
  bachelors_plus: 14735
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/id/districts/senate/1"
    rel: in-district
    area_weight: 0.9068
  - to: "us/states/id/districts/senate/2"
    rel: in-district
    area_weight: 0.0931
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Bonner County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51049 |
| Under 18 | 9996 |
| 18–64 | 27576 |
| 65+ | 13477 |
| Median household income | 66979 |
| Poverty rate | 11.12 |
| Homeownership rate | 78.28 |
| Unemployment rate | 4.82 |
| Median home value | 487900 |
| Gini index | 0.4828 |
| Vacancy rate | 24.51 |
| White | 45936 |
| Black | 177 |
| Asian | 279 |
| Native | 221 |
| Hispanic/Latino | 2028 |
| Bachelor's or higher | 14735 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 1](/us/states/id/districts/senate/1.md) — 91% (state senate)
- [ID Senate District 2](/us/states/id/districts/senate/2.md) — 9% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
