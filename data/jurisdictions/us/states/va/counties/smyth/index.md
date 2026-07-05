---
type: Jurisdiction
title: "Smyth County, VA"
classification: county
fips: "51173"
state: "VA"
demographics:
  population: 29420
  population_under_18: 6231
  population_18_64: 8108
  population_65_plus: 15081
  median_household_income: 49883
  poverty_rate: 16.83
  homeownership_rate: 70.99
  unemployment_rate: 3.05
  median_home_value: 139600
  gini_index: 0.4724
  vacancy_rate: 16.05
  race_white: 27843
  race_black: 628
  race_asian: 23
  race_native: 18
  hispanic: 629
  bachelors_plus: 4997
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/46"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Smyth County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29420 |
| Under 18 | 6231 |
| 18–64 | 8108 |
| 65+ | 15081 |
| Median household income | 49883 |
| Poverty rate | 16.83 |
| Homeownership rate | 70.99 |
| Unemployment rate | 3.05 |
| Median home value | 139600 |
| Gini index | 0.4724 |
| Vacancy rate | 16.05 |
| White | 27843 |
| Black | 628 |
| Asian | 23 |
| Native | 18 |
| Hispanic/Latino | 629 |
| Bachelor's or higher | 4997 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 100% (state senate)
- [VA House District 46](/us/states/va/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
