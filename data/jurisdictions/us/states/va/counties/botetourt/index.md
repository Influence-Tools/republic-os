---
type: Jurisdiction
title: "Botetourt County, VA"
classification: county
fips: "51023"
state: "VA"
demographics:
  population: 34004
  population_under_18: 6324
  population_18_64: 19408
  population_65_plus: 8272
  median_household_income: 81213
  poverty_rate: 6.16
  homeownership_rate: 85.53
  unemployment_rate: 2.4
  median_home_value: 289200
  gini_index: 0.4044
  vacancy_rate: 12.27
  race_white: 30833
  race_black: 872
  race_asian: 244
  race_native: 70
  hispanic: 850
  bachelors_plus: 10096
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/37"
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

# Botetourt County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34004 |
| Under 18 | 6324 |
| 18–64 | 19408 |
| 65+ | 8272 |
| Median household income | 81213 |
| Poverty rate | 6.16 |
| Homeownership rate | 85.53 |
| Unemployment rate | 2.4 |
| Median home value | 289200 |
| Gini index | 0.4044 |
| Vacancy rate | 12.27 |
| White | 30833 |
| Black | 872 |
| Asian | 244 |
| Native | 70 |
| Hispanic/Latino | 850 |
| Bachelor's or higher | 10096 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
