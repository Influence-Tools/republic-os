---
type: Jurisdiction
title: "Wabash County, IN"
classification: county
fips: "18169"
state: "IN"
demographics:
  population: 30844
  population_under_18: 6505
  population_18_64: 17608
  population_65_plus: 6731
  median_household_income: 66806
  poverty_rate: 11.09
  homeownership_rate: 80.48
  unemployment_rate: 3.44
  median_home_value: 157200
  gini_index: 0.4194
  vacancy_rate: 10.09
  race_white: 28833
  race_black: 284
  race_asian: 130
  race_native: 21
  hispanic: 982
  bachelors_plus: 6541
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/50"
    rel: in-district
    area_weight: 0.8691
  - to: "us/states/in/districts/house/22"
    rel: in-district
    area_weight: 0.1308
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Wabash County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30844 |
| Under 18 | 6505 |
| 18–64 | 17608 |
| 65+ | 6731 |
| Median household income | 66806 |
| Poverty rate | 11.09 |
| Homeownership rate | 80.48 |
| Unemployment rate | 3.44 |
| Median home value | 157200 |
| Gini index | 0.4194 |
| Vacancy rate | 10.09 |
| White | 28833 |
| Black | 284 |
| Asian | 130 |
| Native | 21 |
| Hispanic/Latino | 982 |
| Bachelor's or higher | 6541 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 17](/us/states/in/districts/senate/17.md) — 100% (state senate)
- [IN House District 50](/us/states/in/districts/house/50.md) — 87% (state house)
- [IN House District 22](/us/states/in/districts/house/22.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
