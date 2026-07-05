---
type: Jurisdiction
title: "Gem County, ID"
classification: county
fips: "16045"
state: "ID"
demographics:
  population: 20614
  population_under_18: 4523
  population_18_64: 11336
  population_65_plus: 4755
  median_household_income: 64605
  poverty_rate: 11.98
  homeownership_rate: 76.03
  unemployment_rate: 2.95
  median_home_value: 428700
  gini_index: 0.4253
  vacancy_rate: 3.91
  race_white: 17758
  race_black: 2
  race_asian: 159
  race_native: 155
  hispanic: 1992
  bachelors_plus: 3597
districts:
  - to: "us/states/id/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/14"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Gem County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20614 |
| Under 18 | 4523 |
| 18–64 | 11336 |
| 65+ | 4755 |
| Median household income | 64605 |
| Poverty rate | 11.98 |
| Homeownership rate | 76.03 |
| Unemployment rate | 2.95 |
| Median home value | 428700 |
| Gini index | 0.4253 |
| Vacancy rate | 3.91 |
| White | 17758 |
| Black | 2 |
| Asian | 159 |
| Native | 155 |
| Hispanic/Latino | 1992 |
| Bachelor's or higher | 3597 |

## Districts

- [ID-01](/us/states/id/districts/01.md) — 100% (congressional)
- [ID Senate District 14](/us/states/id/districts/senate/14.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
