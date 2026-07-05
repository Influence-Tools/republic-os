---
type: Jurisdiction
title: "Rolette County, ND"
classification: county
fips: "38079"
state: "ND"
demographics:
  population: 11924
  population_under_18: 3843
  population_18_64: 6509
  population_65_plus: 1572
  median_household_income: 59517
  poverty_rate: 24.33
  homeownership_rate: 62.83
  unemployment_rate: 4.01
  median_home_value: 103800
  gini_index: 0.4633
  vacancy_rate: 17.85
  race_white: 2192
  race_black: 17
  race_asian: 62
  race_native: 9074
  hispanic: 151
  bachelors_plus: 1712
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/senate/9"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/9"
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

# Rolette County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11924 |
| Under 18 | 3843 |
| 18–64 | 6509 |
| 65+ | 1572 |
| Median household income | 59517 |
| Poverty rate | 24.33 |
| Homeownership rate | 62.83 |
| Unemployment rate | 4.01 |
| Median home value | 103800 |
| Gini index | 0.4633 |
| Vacancy rate | 17.85 |
| White | 2192 |
| Black | 17 |
| Asian | 62 |
| Native | 9074 |
| Hispanic/Latino | 151 |
| Bachelor's or higher | 1712 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 9](/us/states/nd/districts/senate/9.md) — 100% (state senate)
- [ND House District 9](/us/states/nd/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
