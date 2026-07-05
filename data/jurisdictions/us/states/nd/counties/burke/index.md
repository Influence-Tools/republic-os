---
type: Jurisdiction
title: "Burke County, ND"
classification: county
fips: "38013"
state: "ND"
demographics:
  population: 2156
  population_under_18: 583
  population_18_64: 1120
  population_65_plus: 453
  median_household_income: 91591
  poverty_rate: 5.89
  homeownership_rate: 75.11
  unemployment_rate: 3.73
  median_home_value: 158100
  gini_index: 0.4451
  vacancy_rate: 33.63
  race_white: 1872
  race_black: 37
  race_asian: 45
  race_native: 39
  hispanic: 54
  bachelors_plus: 385
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nd/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/2"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Burke County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2156 |
| Under 18 | 583 |
| 18–64 | 1120 |
| 65+ | 453 |
| Median household income | 91591 |
| Poverty rate | 5.89 |
| Homeownership rate | 75.11 |
| Unemployment rate | 3.73 |
| Median home value | 158100 |
| Gini index | 0.4451 |
| Vacancy rate | 33.63 |
| White | 1872 |
| Black | 37 |
| Asian | 45 |
| Native | 39 |
| Hispanic/Latino | 54 |
| Bachelor's or higher | 385 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 2](/us/states/nd/districts/senate/2.md) — 100% (state senate)
- [ND House District 2](/us/states/nd/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
