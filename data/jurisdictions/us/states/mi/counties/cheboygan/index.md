---
type: Jurisdiction
title: "Cheboygan County, MI"
classification: county
fips: "26031"
state: "MI"
demographics:
  population: 25865
  population_under_18: 3968
  population_18_64: 14403
  population_65_plus: 7494
  median_household_income: 62875
  poverty_rate: 12.36
  homeownership_rate: 85.63
  unemployment_rate: 6.1
  median_home_value: 192500
  gini_index: 0.4512
  vacancy_rate: 37.27
  race_white: 23120
  race_black: 238
  race_asian: 141
  race_native: 580
  hispanic: 440
  bachelors_plus: 6886
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.9002
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.898
  - to: "us/states/mi/districts/house/106"
    rel: in-district
    area_weight: 0.8852
  - to: "us/states/mi/districts/house/107"
    rel: in-district
    area_weight: 0.013
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Cheboygan County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25865 |
| Under 18 | 3968 |
| 18–64 | 14403 |
| 65+ | 7494 |
| Median household income | 62875 |
| Poverty rate | 12.36 |
| Homeownership rate | 85.63 |
| Unemployment rate | 6.1 |
| Median home value | 192500 |
| Gini index | 0.4512 |
| Vacancy rate | 37.27 |
| White | 23120 |
| Black | 238 |
| Asian | 141 |
| Native | 580 |
| Hispanic/Latino | 440 |
| Bachelor's or higher | 6886 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 90% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 90% (state senate)
- [MI House District 106](/us/states/mi/districts/house/106.md) — 89% (state house)
- [MI House District 107](/us/states/mi/districts/house/107.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
