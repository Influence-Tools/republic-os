---
type: Jurisdiction
title: "Appomattox County, VA"
classification: county
fips: "51011"
state: "VA"
demographics:
  population: 16610
  population_under_18: 3661
  population_18_64: 9440
  population_65_plus: 3509
  median_household_income: 62853
  poverty_rate: 13.99
  homeownership_rate: 75.78
  unemployment_rate: 5.12
  median_home_value: 207600
  gini_index: 0.4199
  vacancy_rate: 10.99
  race_white: 12820
  race_black: 2637
  race_asian: 66
  race_native: 1
  hispanic: 399
  bachelors_plus: 2760
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Appomattox County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16610 |
| Under 18 | 3661 |
| 18–64 | 9440 |
| 65+ | 3509 |
| Median household income | 62853 |
| Poverty rate | 13.99 |
| Homeownership rate | 75.78 |
| Unemployment rate | 5.12 |
| Median home value | 207600 |
| Gini index | 0.4199 |
| Vacancy rate | 10.99 |
| White | 12820 |
| Black | 2637 |
| Asian | 66 |
| Native | 1 |
| Hispanic/Latino | 399 |
| Bachelor's or higher | 2760 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 56](/us/states/va/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
