---
type: Jurisdiction
title: "North Slope Borough, AK"
classification: county
fips: "02185"
state: "AK"
demographics:
  population: 10810
  population_under_18: 3096
  population_18_64: 4025
  population_65_plus: 3689
  median_household_income: 95694
  poverty_rate: 11.07
  homeownership_rate: 49.15
  unemployment_rate: 7.6
  median_home_value: 218300
  gini_index: 0.4471
  vacancy_rate: 13.66
  race_white: 3401
  race_black: 194
  race_asian: 598
  race_native: 5413
  hispanic: 583
  bachelors_plus: 1541
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9504
  - to: "us/states/ak/districts/senate/t"
    rel: in-district
    area_weight: 0.949
  - to: "us/states/ak/districts/house/40"
    rel: in-district
    area_weight: 0.949
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# North Slope Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10810 |
| Under 18 | 3096 |
| 18–64 | 4025 |
| 65+ | 3689 |
| Median household income | 95694 |
| Poverty rate | 11.07 |
| Homeownership rate | 49.15 |
| Unemployment rate | 7.6 |
| Median home value | 218300 |
| Gini index | 0.4471 |
| Vacancy rate | 13.66 |
| White | 3401 |
| Black | 194 |
| Asian | 598 |
| Native | 5413 |
| Hispanic/Latino | 583 |
| Bachelor's or higher | 1541 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 95% (congressional)
- [AK Senate District T](/us/states/ak/districts/senate/t.md) — 95% (state senate)
- [AK House District 40](/us/states/ak/districts/house/40.md) — 95% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
