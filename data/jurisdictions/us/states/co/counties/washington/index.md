---
type: Jurisdiction
title: "Washington County, CO"
classification: county
fips: "08121"
state: "CO"
demographics:
  population: 4831
  population_under_18: 1113
  population_18_64: 1474
  population_65_plus: 2244
  median_household_income: 67167
  poverty_rate: 8.08
  homeownership_rate: 73.62
  unemployment_rate: 3.1
  median_home_value: 226200
  gini_index: 0.4198
  vacancy_rate: 9.49
  race_white: 4201
  race_black: 57
  race_asian: 27
  race_native: 30
  hispanic: 569
  bachelors_plus: 1106
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Washington County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4831 |
| Under 18 | 1113 |
| 18–64 | 1474 |
| 65+ | 2244 |
| Median household income | 67167 |
| Poverty rate | 8.08 |
| Homeownership rate | 73.62 |
| Unemployment rate | 3.1 |
| Median home value | 226200 |
| Gini index | 0.4198 |
| Vacancy rate | 9.49 |
| White | 4201 |
| Black | 57 |
| Asian | 27 |
| Native | 30 |
| Hispanic/Latino | 569 |
| Bachelor's or higher | 1106 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
