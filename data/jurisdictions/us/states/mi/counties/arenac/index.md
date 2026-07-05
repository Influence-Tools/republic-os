---
type: Jurisdiction
title: "Arenac County, MI"
classification: county
fips: "26011"
state: "MI"
demographics:
  population: 15077
  population_under_18: 2782
  population_18_64: 8191
  population_65_plus: 4104
  median_household_income: 58811
  poverty_rate: 11.74
  homeownership_rate: 86.25
  unemployment_rate: 6.0
  median_home_value: 150600
  gini_index: 0.4039
  vacancy_rate: 31.42
  race_white: 14086
  race_black: 109
  race_asian: 29
  race_native: 57
  hispanic: 336
  bachelors_plus: 2490
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.5387
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.5401
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.5401
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Arenac County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15077 |
| Under 18 | 2782 |
| 18–64 | 8191 |
| 65+ | 4104 |
| Median household income | 58811 |
| Poverty rate | 11.74 |
| Homeownership rate | 86.25 |
| Unemployment rate | 6.0 |
| Median home value | 150600 |
| Gini index | 0.4039 |
| Vacancy rate | 31.42 |
| White | 14086 |
| Black | 109 |
| Asian | 29 |
| Native | 57 |
| Hispanic/Latino | 336 |
| Bachelor's or higher | 2490 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 54% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 54% (state senate)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 54% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
