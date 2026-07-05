---
type: Jurisdiction
title: "Marlboro County, SC"
classification: county
fips: "45069"
state: "SC"
demographics:
  population: 25975
  population_under_18: 5171
  population_18_64: 15845
  population_65_plus: 4959
  median_household_income: 34301
  poverty_rate: 28.51
  homeownership_rate: 62.99
  unemployment_rate: 9.92
  median_home_value: 82000
  gini_index: 0.4992
  vacancy_rate: 18.95
  race_white: 10179
  race_black: 12429
  race_asian: 107
  race_native: 786
  hispanic: 708
  bachelors_plus: 2221
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/sc/districts/senate/29"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/sc/districts/house/54"
    rel: in-district
    area_weight: 0.9284
  - to: "us/states/sc/districts/house/55"
    rel: in-district
    area_weight: 0.0708
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Marlboro County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25975 |
| Under 18 | 5171 |
| 18–64 | 15845 |
| 65+ | 4959 |
| Median household income | 34301 |
| Poverty rate | 28.51 |
| Homeownership rate | 62.99 |
| Unemployment rate | 9.92 |
| Median home value | 82000 |
| Gini index | 0.4992 |
| Vacancy rate | 18.95 |
| White | 10179 |
| Black | 12429 |
| Asian | 107 |
| Native | 786 |
| Hispanic/Latino | 708 |
| Bachelor's or higher | 2221 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 100% (congressional)
- [SC Senate District 29](/us/states/sc/districts/senate/29.md) — 100% (state senate)
- [SC House District 54](/us/states/sc/districts/house/54.md) — 93% (state house)
- [SC House District 55](/us/states/sc/districts/house/55.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
