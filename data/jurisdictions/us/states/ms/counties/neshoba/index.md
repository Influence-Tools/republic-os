---
type: Jurisdiction
title: "Neshoba County, MS"
classification: county
fips: "28099"
state: "MS"
demographics:
  population: 28932
  population_under_18: 7954
  population_18_64: 16085
  population_65_plus: 4893
  median_household_income: 57013
  poverty_rate: 23.1
  homeownership_rate: 78.08
  unemployment_rate: 7.47
  median_home_value: 100000
  gini_index: 0.4527
  vacancy_rate: 15.13
  race_white: 16601
  race_black: 6143
  race_asian: 190
  race_native: 4555
  hispanic: 238
  bachelors_plus: 4983
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/house/44"
    rel: in-district
    area_weight: 0.823
  - to: "us/states/ms/districts/house/45"
    rel: in-district
    area_weight: 0.1769
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Neshoba County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28932 |
| Under 18 | 7954 |
| 18–64 | 16085 |
| 65+ | 4893 |
| Median household income | 57013 |
| Poverty rate | 23.1 |
| Homeownership rate | 78.08 |
| Unemployment rate | 7.47 |
| Median home value | 100000 |
| Gini index | 0.4527 |
| Vacancy rate | 15.13 |
| White | 16601 |
| Black | 6143 |
| Asian | 190 |
| Native | 4555 |
| Hispanic/Latino | 238 |
| Bachelor's or higher | 4983 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 18](/us/states/ms/districts/senate/18.md) — 100% (state senate)
- [MS House District 44](/us/states/ms/districts/house/44.md) — 82% (state house)
- [MS House District 45](/us/states/ms/districts/house/45.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
