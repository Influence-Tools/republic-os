---
type: Jurisdiction
title: "Gloucester County, VA"
classification: county
fips: "51073"
state: "VA"
demographics:
  population: 39526
  population_under_18: 7876
  population_18_64: 23383
  population_65_plus: 8267
  median_household_income: 84306
  poverty_rate: 5.17
  homeownership_rate: 80.38
  unemployment_rate: 2.97
  median_home_value: 331000
  gini_index: 0.3967
  vacancy_rate: 11.76
  race_white: 32841
  race_black: 3215
  race_asian: 328
  race_native: 72
  hispanic: 1680
  bachelors_plus: 10144
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.8794
  - to: "us/states/va/districts/senate/26"
    rel: in-district
    area_weight: 0.8619
  - to: "us/states/va/districts/house/68"
    rel: in-district
    area_weight: 0.8324
  - to: "us/states/va/districts/house/69"
    rel: in-district
    area_weight: 0.0298
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Gloucester County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39526 |
| Under 18 | 7876 |
| 18–64 | 23383 |
| 65+ | 8267 |
| Median household income | 84306 |
| Poverty rate | 5.17 |
| Homeownership rate | 80.38 |
| Unemployment rate | 2.97 |
| Median home value | 331000 |
| Gini index | 0.3967 |
| Vacancy rate | 11.76 |
| White | 32841 |
| Black | 3215 |
| Asian | 328 |
| Native | 72 |
| Hispanic/Latino | 1680 |
| Bachelor's or higher | 10144 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 88% (congressional)
- [VA Senate District 26](/us/states/va/districts/senate/26.md) — 86% (state senate)
- [VA House District 68](/us/states/va/districts/house/68.md) — 83% (state house)
- [VA House District 69](/us/states/va/districts/house/69.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
