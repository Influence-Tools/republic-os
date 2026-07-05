---
type: Jurisdiction
title: "Goliad County, TX"
classification: county
fips: "48175"
state: "TX"
demographics:
  population: 7141
  population_under_18: 1412
  population_18_64: 3977
  population_65_plus: 1752
  median_household_income: 59359
  poverty_rate: 13.03
  homeownership_rate: 86.84
  unemployment_rate: 5.25
  median_home_value: 192500
  gini_index: 0.5209
  vacancy_rate: 20.75
  race_white: 5242
  race_black: 382
  race_asian: 1
  race_native: 31
  hispanic: 2308
  bachelors_plus: 1471
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/30"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Goliad County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7141 |
| Under 18 | 1412 |
| 18–64 | 3977 |
| 65+ | 1752 |
| Median household income | 59359 |
| Poverty rate | 13.03 |
| Homeownership rate | 86.84 |
| Unemployment rate | 5.25 |
| Median home value | 192500 |
| Gini index | 0.5209 |
| Vacancy rate | 20.75 |
| White | 5242 |
| Black | 382 |
| Asian | 1 |
| Native | 31 |
| Hispanic/Latino | 2308 |
| Bachelor's or higher | 1471 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 30](/us/states/tx/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
