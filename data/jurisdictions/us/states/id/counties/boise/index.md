---
type: Jurisdiction
title: "Boise County, ID"
classification: county
fips: "16015"
state: "ID"
demographics:
  population: 8273
  population_under_18: 1274
  population_18_64: 4660
  population_65_plus: 2339
  median_household_income: 78774
  poverty_rate: 7.72
  homeownership_rate: 90.29
  unemployment_rate: 3.4
  median_home_value: 476100
  gini_index: 0.3654
  vacancy_rate: 36.84
  race_white: 7017
  race_black: 22
  race_asian: 125
  race_native: 103
  hispanic: 422
  bachelors_plus: 2642
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/id/districts/senate/8"
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

# Boise County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8273 |
| Under 18 | 1274 |
| 18–64 | 4660 |
| 65+ | 2339 |
| Median household income | 78774 |
| Poverty rate | 7.72 |
| Homeownership rate | 90.29 |
| Unemployment rate | 3.4 |
| Median home value | 476100 |
| Gini index | 0.3654 |
| Vacancy rate | 36.84 |
| White | 7017 |
| Black | 22 |
| Asian | 125 |
| Native | 103 |
| Hispanic/Latino | 422 |
| Bachelor's or higher | 2642 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 8](/us/states/id/districts/senate/8.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
