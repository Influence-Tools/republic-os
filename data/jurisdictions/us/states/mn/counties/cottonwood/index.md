---
type: Jurisdiction
title: "Cottonwood County, MN"
classification: county
fips: "27033"
state: "MN"
demographics:
  population: 11458
  population_under_18: 2884
  population_18_64: 5977
  population_65_plus: 2597
  median_household_income: 72941
  poverty_rate: 15.0
  homeownership_rate: 74.43
  unemployment_rate: 2.84
  median_home_value: 169300
  gini_index: 0.4301
  vacancy_rate: 10.41
  race_white: 9280
  race_black: 190
  race_asian: 455
  race_native: 93
  hispanic: 1298
  bachelors_plus: 2285
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/21b"
    rel: in-district
    area_weight: 0.2212
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Cottonwood County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11458 |
| Under 18 | 2884 |
| 18–64 | 5977 |
| 65+ | 2597 |
| Median household income | 72941 |
| Poverty rate | 15.0 |
| Homeownership rate | 74.43 |
| Unemployment rate | 2.84 |
| Median home value | 169300 |
| Gini index | 0.4301 |
| Vacancy rate | 10.41 |
| White | 9280 |
| Black | 190 |
| Asian | 455 |
| Native | 93 |
| Hispanic/Latino | 1298 |
| Bachelor's or higher | 2285 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 21](/us/states/mn/districts/senate/21.md) — 100% (state senate)
- [MN House District 21B](/us/states/mn/districts/house/21b.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
