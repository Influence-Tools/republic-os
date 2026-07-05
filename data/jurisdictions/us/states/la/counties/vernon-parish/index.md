---
type: Jurisdiction
title: "Vernon Parish, LA"
classification: county
fips: "22115"
state: "LA"
demographics:
  population: 47117
  population_under_18: 11985
  population_18_64: 28538
  population_65_plus: 6594
  median_household_income: 57270
  poverty_rate: 19.0
  homeownership_rate: 56.0
  unemployment_rate: 5.68
  median_home_value: 156000
  gini_index: 0.4428
  vacancy_rate: 17.4
  race_white: 35086
  race_black: 5851
  race_asian: 787
  race_native: 470
  hispanic: 4446
  bachelors_plus: 7448
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/la/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/24"
    rel: in-district
    area_weight: 0.8251
  - to: "us/states/la/districts/house/30"
    rel: in-district
    area_weight: 0.1747
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Vernon Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47117 |
| Under 18 | 11985 |
| 18–64 | 28538 |
| 65+ | 6594 |
| Median household income | 57270 |
| Poverty rate | 19.0 |
| Homeownership rate | 56.0 |
| Unemployment rate | 5.68 |
| Median home value | 156000 |
| Gini index | 0.4428 |
| Vacancy rate | 17.4 |
| White | 35086 |
| Black | 5851 |
| Asian | 787 |
| Native | 470 |
| Hispanic/Latino | 4446 |
| Bachelor's or higher | 7448 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 30](/us/states/la/districts/senate/30.md) — 100% (state senate)
- [LA House District 24](/us/states/la/districts/house/24.md) — 83% (state house)
- [LA House District 30](/us/states/la/districts/house/30.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
