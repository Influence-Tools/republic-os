---
type: Jurisdiction
title: "Beaverhead County, MT"
classification: county
fips: "30001"
state: "MT"
demographics:
  population: 9713
  population_under_18: 1699
  population_18_64: 5700
  population_65_plus: 2314
  median_household_income: 61268
  poverty_rate: 11.43
  homeownership_rate: 65.84
  unemployment_rate: 1.28
  median_home_value: 308300
  gini_index: 0.4256
  vacancy_rate: 15.66
  race_white: 8870
  race_black: 52
  race_asian: 29
  race_native: 129
  hispanic: 508
  bachelors_plus: 3299
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/mt/districts/senate/35"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/house/70"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Beaverhead County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9713 |
| Under 18 | 1699 |
| 18–64 | 5700 |
| 65+ | 2314 |
| Median household income | 61268 |
| Poverty rate | 11.43 |
| Homeownership rate | 65.84 |
| Unemployment rate | 1.28 |
| Median home value | 308300 |
| Gini index | 0.4256 |
| Vacancy rate | 15.66 |
| White | 8870 |
| Black | 52 |
| Asian | 29 |
| Native | 129 |
| Hispanic/Latino | 508 |
| Bachelor's or higher | 3299 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 35](/us/states/mt/districts/senate/35.md) — 100% (state senate)
- [MT House District 70](/us/states/mt/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
