---
type: Jurisdiction
title: "Lemhi County, ID"
classification: county
fips: "16059"
state: "ID"
demographics:
  population: 8249
  population_under_18: 1399
  population_18_64: 4300
  population_65_plus: 2550
  median_household_income: 53202
  poverty_rate: 12.84
  homeownership_rate: 79.27
  unemployment_rate: 2.03
  median_home_value: 326100
  gini_index: 0.4948
  vacancy_rate: 26.05
  race_white: 7624
  race_black: 8
  race_asian: 13
  race_native: 34
  hispanic: 324
  bachelors_plus: 2004
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/id/districts/senate/31"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Lemhi County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8249 |
| Under 18 | 1399 |
| 18–64 | 4300 |
| 65+ | 2550 |
| Median household income | 53202 |
| Poverty rate | 12.84 |
| Homeownership rate | 79.27 |
| Unemployment rate | 2.03 |
| Median home value | 326100 |
| Gini index | 0.4948 |
| Vacancy rate | 26.05 |
| White | 7624 |
| Black | 8 |
| Asian | 13 |
| Native | 34 |
| Hispanic/Latino | 324 |
| Bachelor's or higher | 2004 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 31](/us/states/id/districts/senate/31.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
