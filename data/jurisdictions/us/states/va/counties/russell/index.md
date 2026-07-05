---
type: Jurisdiction
title: "Russell County, VA"
classification: county
fips: "51167"
state: "VA"
demographics:
  population: 25538
  population_under_18: 4817
  population_18_64: 14688
  population_65_plus: 6033
  median_household_income: 50012
  poverty_rate: 16.68
  homeownership_rate: 76.31
  unemployment_rate: 3.61
  median_home_value: 120600
  gini_index: 0.4599
  vacancy_rate: 16.39
  race_white: 24711
  race_black: 287
  race_asian: 23
  race_native: 35
  hispanic: 180
  bachelors_plus: 3293
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/44"
    rel: in-district
    area_weight: 0.6244
  - to: "us/states/va/districts/house/43"
    rel: in-district
    area_weight: 0.3756
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Russell County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25538 |
| Under 18 | 4817 |
| 18–64 | 14688 |
| 65+ | 6033 |
| Median household income | 50012 |
| Poverty rate | 16.68 |
| Homeownership rate | 76.31 |
| Unemployment rate | 3.61 |
| Median home value | 120600 |
| Gini index | 0.4599 |
| Vacancy rate | 16.39 |
| White | 24711 |
| Black | 287 |
| Asian | 23 |
| Native | 35 |
| Hispanic/Latino | 180 |
| Bachelor's or higher | 3293 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 44](/us/states/va/districts/house/44.md) — 62% (state house)
- [VA House District 43](/us/states/va/districts/house/43.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
