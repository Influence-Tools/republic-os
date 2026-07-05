---
type: Jurisdiction
title: "Greeley County, KS"
classification: county
fips: "20071"
state: "KS"
demographics:
  population: 1304
  population_under_18: 405
  population_18_64: 660
  population_65_plus: 239
  median_household_income: 80565
  poverty_rate: 7.11
  homeownership_rate: 75.05
  unemployment_rate: 0.15
  median_home_value: 115200
  gini_index: 0.355
  vacancy_rate: 17.91
  race_white: 1172
  race_black: 2
  race_asian: 0
  race_native: 28
  hispanic: 220
  bachelors_plus: 337
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/118"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Greeley County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1304 |
| Under 18 | 405 |
| 18–64 | 660 |
| 65+ | 239 |
| Median household income | 80565 |
| Poverty rate | 7.11 |
| Homeownership rate | 75.05 |
| Unemployment rate | 0.15 |
| Median home value | 115200 |
| Gini index | 0.355 |
| Vacancy rate | 17.91 |
| White | 1172 |
| Black | 2 |
| Asian | 0 |
| Native | 28 |
| Hispanic/Latino | 220 |
| Bachelor's or higher | 337 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 39](/us/states/ks/districts/senate/39.md) — 100% (state senate)
- [KS House District 118](/us/states/ks/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
