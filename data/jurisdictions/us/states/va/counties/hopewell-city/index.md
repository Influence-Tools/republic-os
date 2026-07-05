---
type: Jurisdiction
title: "Hopewell city, VA"
classification: county
fips: "51670"
state: "VA"
demographics:
  population: 22959
  population_under_18: 6154
  population_18_64: 7448
  population_65_plus: 9357
  median_household_income: 54729
  poverty_rate: 21.79
  homeownership_rate: 57.9
  unemployment_rate: 9.24
  median_home_value: 181600
  gini_index: 0.4643
  vacancy_rate: 11.42
  race_white: 9436
  race_black: 10004
  race_asian: 247
  race_native: 6
  hispanic: 2052
  bachelors_plus: 2704
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/va/districts/house/75"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Hopewell city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22959 |
| Under 18 | 6154 |
| 18–64 | 7448 |
| 65+ | 9357 |
| Median household income | 54729 |
| Poverty rate | 21.79 |
| Homeownership rate | 57.9 |
| Unemployment rate | 9.24 |
| Median home value | 181600 |
| Gini index | 0.4643 |
| Vacancy rate | 11.42 |
| White | 9436 |
| Black | 10004 |
| Asian | 247 |
| Native | 6 |
| Hispanic/Latino | 2052 |
| Bachelor's or higher | 2704 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 100% (state senate)
- [VA House District 75](/us/states/va/districts/house/75.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
