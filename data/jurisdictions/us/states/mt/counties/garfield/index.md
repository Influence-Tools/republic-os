---
type: Jurisdiction
title: "Garfield County, MT"
classification: county
fips: "30033"
state: "MT"
demographics:
  population: 1094
  population_under_18: 272
  population_18_64: 533
  population_65_plus: 289
  median_household_income: 69583
  poverty_rate: 13.41
  homeownership_rate: 72.22
  unemployment_rate: 0.0
  median_home_value: 169900
  gini_index: 0.4801
  vacancy_rate: 40.82
  race_white: 1058
  race_black: 0
  race_asian: 0
  race_native: 12
  hispanic: 0
  bachelors_plus: 202
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/35"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Garfield County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1094 |
| Under 18 | 272 |
| 18–64 | 533 |
| 65+ | 289 |
| Median household income | 69583 |
| Poverty rate | 13.41 |
| Homeownership rate | 72.22 |
| Unemployment rate | 0.0 |
| Median home value | 169900 |
| Gini index | 0.4801 |
| Vacancy rate | 40.82 |
| White | 1058 |
| Black | 0 |
| Asian | 0 |
| Native | 12 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 202 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 18](/us/states/mt/districts/senate/18.md) — 100% (state senate)
- [MT House District 35](/us/states/mt/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
