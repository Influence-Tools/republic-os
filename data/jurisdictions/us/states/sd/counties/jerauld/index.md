---
type: Jurisdiction
title: "Jerauld County, SD"
classification: county
fips: "46073"
state: "SD"
demographics:
  population: 1772
  population_under_18: 404
  population_18_64: 823
  population_65_plus: 545
  median_household_income: 73750
  poverty_rate: 8.31
  homeownership_rate: 84.08
  unemployment_rate: 1.74
  median_home_value: 150800
  gini_index: 0.4675
  vacancy_rate: 18.48
  race_white: 1617
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 124
  bachelors_plus: 322
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sd/districts/house/20"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Jerauld County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1772 |
| Under 18 | 404 |
| 18–64 | 823 |
| 65+ | 545 |
| Median household income | 73750 |
| Poverty rate | 8.31 |
| Homeownership rate | 84.08 |
| Unemployment rate | 1.74 |
| Median home value | 150800 |
| Gini index | 0.4675 |
| Vacancy rate | 18.48 |
| White | 1617 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 124 |
| Bachelor's or higher | 322 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 20](/us/states/sd/districts/senate/20.md) — 100% (state senate)
- [SD House District 20](/us/states/sd/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
