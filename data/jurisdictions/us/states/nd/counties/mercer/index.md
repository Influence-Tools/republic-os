---
type: Jurisdiction
title: "Mercer County, ND"
classification: county
fips: "38057"
state: "ND"
demographics:
  population: 8337
  population_under_18: 1949
  population_18_64: 4512
  population_65_plus: 1876
  median_household_income: 80946
  poverty_rate: 9.67
  homeownership_rate: 81.05
  unemployment_rate: 2.53
  median_home_value: 198500
  gini_index: 0.3997
  vacancy_rate: 22.99
  race_white: 7647
  race_black: 1
  race_asian: 42
  race_native: 204
  hispanic: 231
  bachelors_plus: 1680
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/33"
    rel: in-district
    area_weight: 0.9228
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.0771
  - to: "us/states/nd/districts/house/33"
    rel: in-district
    area_weight: 0.9228
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.0771
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Mercer County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8337 |
| Under 18 | 1949 |
| 18–64 | 4512 |
| 65+ | 1876 |
| Median household income | 80946 |
| Poverty rate | 9.67 |
| Homeownership rate | 81.05 |
| Unemployment rate | 2.53 |
| Median home value | 198500 |
| Gini index | 0.3997 |
| Vacancy rate | 22.99 |
| White | 7647 |
| Black | 1 |
| Asian | 42 |
| Native | 204 |
| Hispanic/Latino | 231 |
| Bachelor's or higher | 1680 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 33](/us/states/nd/districts/senate/33.md) — 92% (state senate)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 8% (state senate)
- [ND House District 33](/us/states/nd/districts/house/33.md) — 92% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
