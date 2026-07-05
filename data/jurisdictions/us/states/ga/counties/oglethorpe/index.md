---
type: Jurisdiction
title: "Oglethorpe County, GA"
classification: county
fips: "13221"
state: "GA"
demographics:
  population: 15509
  population_under_18: 3332
  population_18_64: 9208
  population_65_plus: 2969
  median_household_income: 75034
  poverty_rate: 11.6
  homeownership_rate: 83.83
  unemployment_rate: 3.06
  median_home_value: 231600
  gini_index: 0.4486
  vacancy_rate: 16.89
  race_white: 11472
  race_black: 2393
  race_asian: 123
  race_native: 23
  hispanic: 1051
  bachelors_plus: 3963
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/124"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Oglethorpe County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15509 |
| Under 18 | 3332 |
| 18–64 | 9208 |
| 65+ | 2969 |
| Median household income | 75034 |
| Poverty rate | 11.6 |
| Homeownership rate | 83.83 |
| Unemployment rate | 3.06 |
| Median home value | 231600 |
| Gini index | 0.4486 |
| Vacancy rate | 16.89 |
| White | 11472 |
| Black | 2393 |
| Asian | 123 |
| Native | 23 |
| Hispanic/Latino | 1051 |
| Bachelor's or higher | 3963 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 24](/us/states/ga/districts/senate/24.md) — 100% (state senate)
- [GA House District 124](/us/states/ga/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
