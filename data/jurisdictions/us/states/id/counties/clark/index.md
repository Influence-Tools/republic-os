---
type: Jurisdiction
title: "Clark County, ID"
classification: county
fips: "16033"
state: "ID"
demographics:
  population: 849
  population_under_18: 242
  population_18_64: 504
  population_65_plus: 103
  median_household_income: 55208
  poverty_rate: 11.74
  homeownership_rate: 61.29
  unemployment_rate: 2.08
  median_home_value: 216900
  gini_index: 0.3317
  vacancy_rate: 38.82
  race_white: 598
  race_black: 0
  race_asian: 0
  race_native: 1
  hispanic: 244
  bachelors_plus: 126
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/id/districts/senate/31"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Clark County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 849 |
| Under 18 | 242 |
| 18–64 | 504 |
| 65+ | 103 |
| Median household income | 55208 |
| Poverty rate | 11.74 |
| Homeownership rate | 61.29 |
| Unemployment rate | 2.08 |
| Median home value | 216900 |
| Gini index | 0.3317 |
| Vacancy rate | 38.82 |
| White | 598 |
| Black | 0 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 244 |
| Bachelor's or higher | 126 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 31](/us/states/id/districts/senate/31.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
