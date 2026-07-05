---
type: Jurisdiction
title: "West Feliciana Parish, LA"
classification: county
fips: "22125"
state: "LA"
demographics:
  population: 15327
  population_under_18: 2449
  population_18_64: 10550
  population_65_plus: 2328
  median_household_income: 77452
  poverty_rate: 11.81
  homeownership_rate: 75.68
  unemployment_rate: 4.14
  median_home_value: 245700
  gini_index: 0.4511
  vacancy_rate: 22.01
  race_white: 7811
  race_black: 6609
  race_asian: 55
  race_native: 71
  hispanic: 626
  bachelors_plus: 3374
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.8853
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.1147
  - to: "us/states/la/districts/house/18"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# West Feliciana Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15327 |
| Under 18 | 2449 |
| 18–64 | 10550 |
| 65+ | 2328 |
| Median household income | 77452 |
| Poverty rate | 11.81 |
| Homeownership rate | 75.68 |
| Unemployment rate | 4.14 |
| Median home value | 245700 |
| Gini index | 0.4511 |
| Vacancy rate | 22.01 |
| White | 7811 |
| Black | 6609 |
| Asian | 55 |
| Native | 71 |
| Hispanic/Latino | 626 |
| Bachelor's or higher | 3374 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 89% (state senate)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 11% (state senate)
- [LA House District 18](/us/states/la/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
