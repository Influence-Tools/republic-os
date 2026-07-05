---
type: Jurisdiction
title: "Powhatan County, VA"
classification: county
fips: "51145"
state: "VA"
demographics:
  population: 31555
  population_under_18: 5770
  population_18_64: 19528
  population_65_plus: 6257
  median_household_income: 110537
  poverty_rate: 4.55
  homeownership_rate: 93.24
  unemployment_rate: 3.65
  median_home_value: 416000
  gini_index: 0.4059
  vacancy_rate: 5.79
  race_white: 26832
  race_black: 2306
  race_asian: 90
  race_native: 165
  hispanic: 919
  bachelors_plus: 10907
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/72"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Powhatan County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31555 |
| Under 18 | 5770 |
| 18–64 | 19528 |
| 65+ | 6257 |
| Median household income | 110537 |
| Poverty rate | 4.55 |
| Homeownership rate | 93.24 |
| Unemployment rate | 3.65 |
| Median home value | 416000 |
| Gini index | 0.4059 |
| Vacancy rate | 5.79 |
| White | 26832 |
| Black | 2306 |
| Asian | 90 |
| Native | 165 |
| Hispanic/Latino | 919 |
| Bachelor's or higher | 10907 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 72](/us/states/va/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
