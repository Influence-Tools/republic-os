---
type: Jurisdiction
title: "East Feliciana Parish, LA"
classification: county
fips: "22037"
state: "LA"
demographics:
  population: 19271
  population_under_18: 3357
  population_18_64: 12025
  population_65_plus: 3889
  median_household_income: 73085
  poverty_rate: 16.23
  homeownership_rate: 85.63
  unemployment_rate: 5.88
  median_home_value: 228100
  gini_index: 0.4797
  vacancy_rate: 22.17
  race_white: 10577
  race_black: 7639
  race_asian: 39
  race_native: 57
  hispanic: 391
  bachelors_plus: 3629
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/la/districts/house/62"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# East Feliciana Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19271 |
| Under 18 | 3357 |
| 18–64 | 12025 |
| 65+ | 3889 |
| Median household income | 73085 |
| Poverty rate | 16.23 |
| Homeownership rate | 85.63 |
| Unemployment rate | 5.88 |
| Median home value | 228100 |
| Gini index | 0.4797 |
| Vacancy rate | 22.17 |
| White | 10577 |
| Black | 7639 |
| Asian | 39 |
| Native | 57 |
| Hispanic/Latino | 391 |
| Bachelor's or higher | 3629 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 100% (state senate)
- [LA House District 62](/us/states/la/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
