---
type: Jurisdiction
title: "Menard County, TX"
classification: county
fips: "48327"
state: "TX"
demographics:
  population: 1955
  population_under_18: 417
  population_18_64: 885
  population_65_plus: 653
  median_household_income: 53043
  poverty_rate: 18.86
  homeownership_rate: 80.68
  unemployment_rate: 10.8
  median_home_value: 108500
  gini_index: 0.4595
  vacancy_rate: 31.89
  race_white: 1469
  race_black: 8
  race_asian: 0
  race_native: 29
  hispanic: 503
  bachelors_plus: 474
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Menard County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1955 |
| Under 18 | 417 |
| 18–64 | 885 |
| 65+ | 653 |
| Median household income | 53043 |
| Poverty rate | 18.86 |
| Homeownership rate | 80.68 |
| Unemployment rate | 10.8 |
| Median home value | 108500 |
| Gini index | 0.4595 |
| Vacancy rate | 31.89 |
| White | 1469 |
| Black | 8 |
| Asian | 0 |
| Native | 29 |
| Hispanic/Latino | 503 |
| Bachelor's or higher | 474 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
