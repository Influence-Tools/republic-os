---
type: Jurisdiction
title: "Greenlee County, AZ"
classification: county
fips: "04011"
state: "AZ"
demographics:
  population: 9409
  population_under_18: 2396
  population_18_64: 5684
  population_65_plus: 1329
  median_household_income: 71164
  poverty_rate: 8.19
  homeownership_rate: 53.02
  unemployment_rate: 2.33
  median_home_value: 158600
  gini_index: 0.4016
  vacancy_rate: 18.99
  race_white: 5409
  race_black: 134
  race_asian: 134
  race_native: 196
  hispanic: 4396
  bachelors_plus: 1802
districts:
  - to: "us/states/az/districts/06"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/az/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/az/districts/house/19"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Greenlee County, AZ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9409 |
| Under 18 | 2396 |
| 18–64 | 5684 |
| 65+ | 1329 |
| Median household income | 71164 |
| Poverty rate | 8.19 |
| Homeownership rate | 53.02 |
| Unemployment rate | 2.33 |
| Median home value | 158600 |
| Gini index | 0.4016 |
| Vacancy rate | 18.99 |
| White | 5409 |
| Black | 134 |
| Asian | 134 |
| Native | 196 |
| Hispanic/Latino | 4396 |
| Bachelor's or higher | 1802 |

## Districts

- [AZ-06](/us/states/az/districts/06.md) — 100% (congressional)
- [AZ Senate District 19](/us/states/az/districts/senate/19.md) — 100% (state senate)
- [AZ House District 19](/us/states/az/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
