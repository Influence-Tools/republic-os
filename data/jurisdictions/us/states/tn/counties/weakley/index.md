---
type: Jurisdiction
title: "Weakley County, TN"
classification: county
fips: "47183"
state: "TN"
demographics:
  population: 33016
  population_under_18: 6286
  population_18_64: 20679
  population_65_plus: 6051
  median_household_income: 51880
  poverty_rate: 19.04
  homeownership_rate: 66.3
  unemployment_rate: 4.0
  median_home_value: 151200
  gini_index: 0.4401
  vacancy_rate: 11.11
  race_white: 28200
  race_black: 2597
  race_asian: 446
  race_native: 96
  hispanic: 1007
  bachelors_plus: 6647
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/76"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Weakley County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33016 |
| Under 18 | 6286 |
| 18–64 | 20679 |
| 65+ | 6051 |
| Median household income | 51880 |
| Poverty rate | 19.04 |
| Homeownership rate | 66.3 |
| Unemployment rate | 4.0 |
| Median home value | 151200 |
| Gini index | 0.4401 |
| Vacancy rate | 11.11 |
| White | 28200 |
| Black | 2597 |
| Asian | 446 |
| Native | 96 |
| Hispanic/Latino | 1007 |
| Bachelor's or higher | 6647 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 76](/us/states/tn/districts/house/76.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
