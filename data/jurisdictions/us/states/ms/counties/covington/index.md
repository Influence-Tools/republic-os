---
type: Jurisdiction
title: "Covington County, MS"
classification: county
fips: "28031"
state: "MS"
demographics:
  population: 18148
  population_under_18: 4410
  population_18_64: 10539
  population_65_plus: 3199
  median_household_income: 45051
  poverty_rate: 19.77
  homeownership_rate: 77.52
  unemployment_rate: 3.45
  median_home_value: 105100
  gini_index: 0.488
  vacancy_rate: 12.79
  race_white: 10880
  race_black: 6313
  race_asian: 44
  race_native: 5
  hispanic: 471
  bachelors_plus: 2830
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/senate/41"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ms/districts/house/90"
    rel: in-district
    area_weight: 0.8742
  - to: "us/states/ms/districts/house/91"
    rel: in-district
    area_weight: 0.1257
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Covington County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18148 |
| Under 18 | 4410 |
| 18–64 | 10539 |
| 65+ | 3199 |
| Median household income | 45051 |
| Poverty rate | 19.77 |
| Homeownership rate | 77.52 |
| Unemployment rate | 3.45 |
| Median home value | 105100 |
| Gini index | 0.488 |
| Vacancy rate | 12.79 |
| White | 10880 |
| Black | 6313 |
| Asian | 44 |
| Native | 5 |
| Hispanic/Latino | 471 |
| Bachelor's or higher | 2830 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 41](/us/states/ms/districts/senate/41.md) — 100% (state senate)
- [MS House District 90](/us/states/ms/districts/house/90.md) — 87% (state house)
- [MS House District 91](/us/states/ms/districts/house/91.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
