---
type: Jurisdiction
title: "Breathitt County, KY"
classification: county
fips: "21025"
state: "KY"
demographics:
  population: 13276
  population_under_18: 2812
  population_18_64: 7983
  population_65_plus: 2481
  median_household_income: 34808
  poverty_rate: 33.13
  homeownership_rate: 76.59
  unemployment_rate: 9.32
  median_home_value: 70300
  gini_index: 0.4906
  vacancy_rate: 16.9
  race_white: 12769
  race_black: 77
  race_asian: 40
  race_native: 23
  hispanic: 149
  bachelors_plus: 2193
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/84"
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

# Breathitt County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13276 |
| Under 18 | 2812 |
| 18–64 | 7983 |
| 65+ | 2481 |
| Median household income | 34808 |
| Poverty rate | 33.13 |
| Homeownership rate | 76.59 |
| Unemployment rate | 9.32 |
| Median home value | 70300 |
| Gini index | 0.4906 |
| Vacancy rate | 16.9 |
| White | 12769 |
| Black | 77 |
| Asian | 40 |
| Native | 23 |
| Hispanic/Latino | 149 |
| Bachelor's or higher | 2193 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 84](/us/states/ky/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
