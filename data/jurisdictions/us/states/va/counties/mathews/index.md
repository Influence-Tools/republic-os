---
type: Jurisdiction
title: "Mathews County, VA"
classification: county
fips: "51115"
state: "VA"
demographics:
  population: 8540
  population_under_18: 1229
  population_18_64: 4466
  population_65_plus: 2845
  median_household_income: 75880
  poverty_rate: 7.8
  homeownership_rate: 84.05
  unemployment_rate: 4.45
  median_home_value: 360900
  gini_index: 0.4405
  vacancy_rate: 27.42
  race_white: 7326
  race_black: 825
  race_asian: 0
  race_native: 7
  hispanic: 228
  bachelors_plus: 2462
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.4103
  - to: "us/states/va/districts/senate/26"
    rel: in-district
    area_weight: 0.3889
  - to: "us/states/va/districts/house/68"
    rel: in-district
    area_weight: 0.3889
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Mathews County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8540 |
| Under 18 | 1229 |
| 18–64 | 4466 |
| 65+ | 2845 |
| Median household income | 75880 |
| Poverty rate | 7.8 |
| Homeownership rate | 84.05 |
| Unemployment rate | 4.45 |
| Median home value | 360900 |
| Gini index | 0.4405 |
| Vacancy rate | 27.42 |
| White | 7326 |
| Black | 825 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 228 |
| Bachelor's or higher | 2462 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 41% (congressional)
- [VA Senate District 26](/us/states/va/districts/senate/26.md) — 39% (state senate)
- [VA House District 68](/us/states/va/districts/house/68.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
