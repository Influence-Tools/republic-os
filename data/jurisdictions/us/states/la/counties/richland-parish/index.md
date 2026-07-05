---
type: Jurisdiction
title: "Richland Parish, LA"
classification: county
fips: "22083"
state: "LA"
demographics:
  population: 19822
  population_under_18: 4682
  population_18_64: 11514
  population_65_plus: 3626
  median_household_income: 53544
  poverty_rate: 24.05
  homeownership_rate: 66.8
  unemployment_rate: 8.89
  median_home_value: 141900
  gini_index: 0.487
  vacancy_rate: 17.11
  race_white: 12014
  race_black: 7095
  race_asian: 12
  race_native: 19
  hispanic: 455
  bachelors_plus: 3281
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.9392
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.0608
  - to: "us/states/la/districts/house/19"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Richland Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19822 |
| Under 18 | 4682 |
| 18–64 | 11514 |
| 65+ | 3626 |
| Median household income | 53544 |
| Poverty rate | 24.05 |
| Homeownership rate | 66.8 |
| Unemployment rate | 8.89 |
| Median home value | 141900 |
| Gini index | 0.487 |
| Vacancy rate | 17.11 |
| White | 12014 |
| Black | 7095 |
| Asian | 12 |
| Native | 19 |
| Hispanic/Latino | 455 |
| Bachelor's or higher | 3281 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 94% (state senate)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 6% (state senate)
- [LA House District 19](/us/states/la/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
