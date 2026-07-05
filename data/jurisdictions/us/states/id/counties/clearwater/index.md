---
type: Jurisdiction
title: "Clearwater County, ID"
classification: county
fips: "16035"
state: "ID"
demographics:
  population: 9012
  population_under_18: 1341
  population_18_64: 5057
  population_65_plus: 2614
  median_household_income: 60000
  poverty_rate: 13.23
  homeownership_rate: 82.87
  unemployment_rate: 4.51
  median_home_value: 268200
  gini_index: 0.4324
  vacancy_rate: 21.4
  race_white: 7988
  race_black: 20
  race_asian: 87
  race_native: 181
  hispanic: 411
  bachelors_plus: 1663
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9997
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

# Clearwater County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9012 |
| Under 18 | 1341 |
| 18–64 | 5057 |
| 65+ | 2614 |
| Median household income | 60000 |
| Poverty rate | 13.23 |
| Homeownership rate | 82.87 |
| Unemployment rate | 4.51 |
| Median home value | 268200 |
| Gini index | 0.4324 |
| Vacancy rate | 21.4 |
| White | 7988 |
| Black | 20 |
| Asian | 87 |
| Native | 181 |
| Hispanic/Latino | 411 |
| Bachelor's or higher | 1663 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 2](/us/states/id/districts/senate/2.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
