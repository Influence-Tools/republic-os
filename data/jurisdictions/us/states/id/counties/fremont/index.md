---
type: Jurisdiction
title: "Fremont County, ID"
classification: county
fips: "16043"
state: "ID"
demographics:
  population: 13943
  population_under_18: 3340
  population_18_64: 8056
  population_65_plus: 2547
  median_household_income: 72683
  poverty_rate: 10.07
  homeownership_rate: 82.64
  unemployment_rate: 3.86
  median_home_value: 314200
  gini_index: 0.4293
  vacancy_rate: 47.17
  race_white: 11905
  race_black: 45
  race_asian: 15
  race_native: 128
  hispanic: 1732
  bachelors_plus: 2748
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/id/districts/senate/31"
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

# Fremont County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13943 |
| Under 18 | 3340 |
| 18–64 | 8056 |
| 65+ | 2547 |
| Median household income | 72683 |
| Poverty rate | 10.07 |
| Homeownership rate | 82.64 |
| Unemployment rate | 3.86 |
| Median home value | 314200 |
| Gini index | 0.4293 |
| Vacancy rate | 47.17 |
| White | 11905 |
| Black | 45 |
| Asian | 15 |
| Native | 128 |
| Hispanic/Latino | 1732 |
| Bachelor's or higher | 2748 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 31](/us/states/id/districts/senate/31.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
