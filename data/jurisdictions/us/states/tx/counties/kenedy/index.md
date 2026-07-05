---
type: Jurisdiction
title: "Kenedy County, TX"
classification: county
fips: "48261"
state: "TX"
demographics:
  population: 145
  population_under_18: 20
  population_18_64: 68
  population_65_plus: 57
  median_household_income: 38882
  poverty_rate: 15.28
  homeownership_rate: 52.73
  unemployment_rate: 0.0
  gini_index: 0.4242
  vacancy_rate: 56.69
  race_white: 29
  race_black: 1
  race_asian: 1
  race_native: 1
  hispanic: 128
  bachelors_plus: 27
districts:
  - to: "us/states/tx/districts/34"
    rel: in-district
    area_weight: 0.8029
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.7933
  - to: "us/states/tx/districts/house/31"
    rel: in-district
    area_weight: 0.7933
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Kenedy County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 145 |
| Under 18 | 20 |
| 18–64 | 68 |
| 65+ | 57 |
| Median household income | 38882 |
| Poverty rate | 15.28 |
| Homeownership rate | 52.73 |
| Unemployment rate | 0.0 |
| Gini index | 0.4242 |
| Vacancy rate | 56.69 |
| White | 29 |
| Black | 1 |
| Asian | 1 |
| Native | 1 |
| Hispanic/Latino | 128 |
| Bachelor's or higher | 27 |

## Districts

- [TX-34](/us/states/tx/districts/34.md) — 80% (congressional)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 79% (state senate)
- [TX House District 31](/us/states/tx/districts/house/31.md) — 79% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
