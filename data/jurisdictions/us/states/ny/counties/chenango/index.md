---
type: Jurisdiction
title: "Chenango County, NY"
classification: county
fips: "36017"
state: "NY"
demographics:
  population: 46321
  population_under_18: 9569
  population_18_64: 26405
  population_65_plus: 10347
  median_household_income: 62948
  poverty_rate: 11.81
  homeownership_rate: 75.38
  unemployment_rate: 6.41
  median_home_value: 137900
  gini_index: 0.4049
  vacancy_rate: 19.1
  race_white: 42977
  race_black: 341
  race_asian: 233
  race_native: 30
  hispanic: 1181
  bachelors_plus: 9472
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ny/districts/senate/53"
    rel: in-district
    area_weight: 0.5865
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 0.4134
  - to: "us/states/ny/districts/house/121"
    rel: in-district
    area_weight: 0.7205
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.2795
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Chenango County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46321 |
| Under 18 | 9569 |
| 18–64 | 26405 |
| 65+ | 10347 |
| Median household income | 62948 |
| Poverty rate | 11.81 |
| Homeownership rate | 75.38 |
| Unemployment rate | 6.41 |
| Median home value | 137900 |
| Gini index | 0.4049 |
| Vacancy rate | 19.1 |
| White | 42977 |
| Black | 341 |
| Asian | 233 |
| Native | 30 |
| Hispanic/Latino | 1181 |
| Bachelor's or higher | 9472 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 53](/us/states/ny/districts/senate/53.md) — 59% (state senate)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 41% (state senate)
- [NY House District 121](/us/states/ny/districts/house/121.md) — 72% (state house)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
