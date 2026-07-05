---
type: Jurisdiction
title: "Grayson County, KY"
classification: county
fips: "21085"
state: "KY"
demographics:
  population: 26707
  population_under_18: 6349
  population_18_64: 15524
  population_65_plus: 4834
  median_household_income: 50757
  poverty_rate: 20.07
  homeownership_rate: 74.57
  unemployment_rate: 6.64
  median_home_value: 164600
  gini_index: 0.4823
  vacancy_rate: 24.24
  race_white: 25475
  race_black: 218
  race_asian: 105
  race_native: 10
  hispanic: 430
  bachelors_plus: 4358
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/5"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/18"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Grayson County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26707 |
| Under 18 | 6349 |
| 18–64 | 15524 |
| 65+ | 4834 |
| Median household income | 50757 |
| Poverty rate | 20.07 |
| Homeownership rate | 74.57 |
| Unemployment rate | 6.64 |
| Median home value | 164600 |
| Gini index | 0.4823 |
| Vacancy rate | 24.24 |
| White | 25475 |
| Black | 218 |
| Asian | 105 |
| Native | 10 |
| Hispanic/Latino | 430 |
| Bachelor's or higher | 4358 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 5](/us/states/ky/districts/senate/5.md) — 100% (state senate)
- [KY House District 18](/us/states/ky/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
