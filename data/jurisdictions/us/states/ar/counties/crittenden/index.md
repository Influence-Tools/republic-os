---
type: Jurisdiction
title: "Crittenden County, AR"
classification: county
fips: "05035"
state: "AR"
demographics:
  population: 47266
  population_under_18: 12759
  population_18_64: 27286
  population_65_plus: 7221
  median_household_income: 55358
  poverty_rate: 20.99
  homeownership_rate: 57.35
  unemployment_rate: 10.23
  median_home_value: 160200
  gini_index: 0.4548
  vacancy_rate: 14.89
  race_white: 18471
  race_black: 24045
  race_asian: 358
  race_native: 56
  hispanic: 1555
  bachelors_plus: 6810
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ar/districts/senate/9"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ar/districts/house/35"
    rel: in-district
    area_weight: 0.6922
  - to: "us/states/ar/districts/house/63"
    rel: in-district
    area_weight: 0.3064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Crittenden County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47266 |
| Under 18 | 12759 |
| 18–64 | 27286 |
| 65+ | 7221 |
| Median household income | 55358 |
| Poverty rate | 20.99 |
| Homeownership rate | 57.35 |
| Unemployment rate | 10.23 |
| Median home value | 160200 |
| Gini index | 0.4548 |
| Vacancy rate | 14.89 |
| White | 18471 |
| Black | 24045 |
| Asian | 358 |
| Native | 56 |
| Hispanic/Latino | 1555 |
| Bachelor's or higher | 6810 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 9](/us/states/ar/districts/senate/9.md) — 100% (state senate)
- [AR House District 35](/us/states/ar/districts/house/35.md) — 69% (state house)
- [AR House District 63](/us/states/ar/districts/house/63.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
