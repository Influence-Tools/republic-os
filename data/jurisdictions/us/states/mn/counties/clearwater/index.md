---
type: Jurisdiction
title: "Clearwater County, MN"
classification: county
fips: "27029"
state: "MN"
demographics:
  population: 8616
  population_under_18: 2158
  population_18_64: 4628
  population_65_plus: 1830
  median_household_income: 64475
  poverty_rate: 12.58
  homeownership_rate: 80.14
  unemployment_rate: 7.67
  median_home_value: 192100
  gini_index: 0.4398
  vacancy_rate: 25.27
  race_white: 7229
  race_black: 14
  race_asian: 69
  race_native: 585
  hispanic: 81
  bachelors_plus: 1505
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.6102
  - to: "us/states/mn/districts/house/2a"
    rel: in-district
    area_weight: 0.3898
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Clearwater County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8616 |
| Under 18 | 2158 |
| 18–64 | 4628 |
| 65+ | 1830 |
| Median household income | 64475 |
| Poverty rate | 12.58 |
| Homeownership rate | 80.14 |
| Unemployment rate | 7.67 |
| Median home value | 192100 |
| Gini index | 0.4398 |
| Vacancy rate | 25.27 |
| White | 7229 |
| Black | 14 |
| Asian | 69 |
| Native | 585 |
| Hispanic/Latino | 81 |
| Bachelor's or higher | 1505 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 100% (state senate)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 61% (state house)
- [MN House District 2A](/us/states/mn/districts/house/2a.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
