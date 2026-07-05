---
type: Jurisdiction
title: "West Baton Rouge Parish, LA"
classification: county
fips: "22121"
state: "LA"
demographics:
  population: 27974
  population_under_18: 6848
  population_18_64: 16972
  population_65_plus: 4154
  median_household_income: 87299
  poverty_rate: 12.91
  homeownership_rate: 76.81
  unemployment_rate: 6.99
  median_home_value: 229900
  gini_index: 0.4226
  vacancy_rate: 8.98
  race_white: 14727
  race_black: 11465
  race_asian: 148
  race_native: 7
  hispanic: 1279
  bachelors_plus: 5804
districts:
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.8573
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.1426
  - to: "us/states/la/districts/house/18"
    rel: in-district
    area_weight: 0.7436
  - to: "us/states/la/districts/house/29"
    rel: in-district
    area_weight: 0.2563
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# West Baton Rouge Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27974 |
| Under 18 | 6848 |
| 18–64 | 16972 |
| 65+ | 4154 |
| Median household income | 87299 |
| Poverty rate | 12.91 |
| Homeownership rate | 76.81 |
| Unemployment rate | 6.99 |
| Median home value | 229900 |
| Gini index | 0.4226 |
| Vacancy rate | 8.98 |
| White | 14727 |
| Black | 11465 |
| Asian | 148 |
| Native | 7 |
| Hispanic/Latino | 1279 |
| Bachelor's or higher | 5804 |

## Districts

- [LA-06](/us/states/la/districts/06.md) — 100% (congressional)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 86% (state senate)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 14% (state senate)
- [LA House District 18](/us/states/la/districts/house/18.md) — 74% (state house)
- [LA House District 29](/us/states/la/districts/house/29.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
