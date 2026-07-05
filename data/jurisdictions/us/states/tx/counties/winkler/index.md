---
type: Jurisdiction
title: "Winkler County, TX"
classification: county
fips: "48495"
state: "TX"
demographics:
  population: 7454
  population_under_18: 2180
  population_18_64: 4341
  population_65_plus: 933
  median_household_income: 86900
  poverty_rate: 16.22
  homeownership_rate: 85.99
  unemployment_rate: 3.6
  median_home_value: 148200
  gini_index: 0.3915
  vacancy_rate: 14.41
  race_white: 3773
  race_black: 294
  race_asian: 41
  race_native: 181
  hispanic: 4657
  bachelors_plus: 560
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/81"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Winkler County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7454 |
| Under 18 | 2180 |
| 18–64 | 4341 |
| 65+ | 933 |
| Median household income | 86900 |
| Poverty rate | 16.22 |
| Homeownership rate | 85.99 |
| Unemployment rate | 3.6 |
| Median home value | 148200 |
| Gini index | 0.3915 |
| Vacancy rate | 14.41 |
| White | 3773 |
| Black | 294 |
| Asian | 41 |
| Native | 181 |
| Hispanic/Latino | 4657 |
| Bachelor's or higher | 560 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 81](/us/states/tx/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
