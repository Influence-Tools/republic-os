---
type: Jurisdiction
title: "Emmet County, MI"
classification: county
fips: "26047"
state: "MI"
demographics:
  population: 34125
  population_under_18: 6188
  population_18_64: 19416
  population_65_plus: 8521
  median_household_income: 78112
  poverty_rate: 8.54
  homeownership_rate: 77.04
  unemployment_rate: 3.22
  median_home_value: 315700
  gini_index: 0.4727
  vacancy_rate: 30.89
  race_white: 30564
  race_black: 210
  race_asian: 176
  race_native: 612
  hispanic: 714
  bachelors_plus: 15054
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.5445
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.5467
  - to: "us/states/mi/districts/house/107"
    rel: in-district
    area_weight: 0.5467
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Emmet County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34125 |
| Under 18 | 6188 |
| 18–64 | 19416 |
| 65+ | 8521 |
| Median household income | 78112 |
| Poverty rate | 8.54 |
| Homeownership rate | 77.04 |
| Unemployment rate | 3.22 |
| Median home value | 315700 |
| Gini index | 0.4727 |
| Vacancy rate | 30.89 |
| White | 30564 |
| Black | 210 |
| Asian | 176 |
| Native | 612 |
| Hispanic/Latino | 714 |
| Bachelor's or higher | 15054 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 54% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 55% (state senate)
- [MI House District 107](/us/states/mi/districts/house/107.md) — 55% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
