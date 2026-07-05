---
type: Jurisdiction
title: "Pickens County, GA"
classification: county
fips: "13227"
state: "GA"
demographics:
  population: 34951
  population_under_18: 6557
  population_18_64: 20363
  population_65_plus: 8031
  median_household_income: 78930
  poverty_rate: 11.96
  homeownership_rate: 81.21
  unemployment_rate: 3.02
  median_home_value: 332700
  gini_index: 0.4301
  vacancy_rate: 13.69
  race_white: 32224
  race_black: 207
  race_asian: 115
  race_native: 70
  hispanic: 1410
  bachelors_plus: 9171
districts:
  - to: "us/states/ga/districts/11"
    rel: in-district
    area_weight: 0.9946
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/11"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Pickens County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34951 |
| Under 18 | 6557 |
| 18–64 | 20363 |
| 65+ | 8031 |
| Median household income | 78930 |
| Poverty rate | 11.96 |
| Homeownership rate | 81.21 |
| Unemployment rate | 3.02 |
| Median home value | 332700 |
| Gini index | 0.4301 |
| Vacancy rate | 13.69 |
| White | 32224 |
| Black | 207 |
| Asian | 115 |
| Native | 70 |
| Hispanic/Latino | 1410 |
| Bachelor's or higher | 9171 |

## Districts

- [GA-11](/us/states/ga/districts/11.md) — 99% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 11](/us/states/ga/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
