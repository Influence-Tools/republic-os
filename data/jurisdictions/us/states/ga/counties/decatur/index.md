---
type: Jurisdiction
title: "Decatur County, GA"
classification: county
fips: "13087"
state: "GA"
demographics:
  population: 29195
  population_under_18: 7061
  population_18_64: 17137
  population_65_plus: 4997
  median_household_income: 53317
  poverty_rate: 22.04
  homeownership_rate: 62.12
  unemployment_rate: 6.34
  median_home_value: 158800
  gini_index: 0.4791
  vacancy_rate: 19.63
  race_white: 14368
  race_black: 12291
  race_asian: 210
  race_native: 575
  hispanic: 2067
  bachelors_plus: 4160
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/171"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Decatur County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29195 |
| Under 18 | 7061 |
| 18–64 | 17137 |
| 65+ | 4997 |
| Median household income | 53317 |
| Poverty rate | 22.04 |
| Homeownership rate | 62.12 |
| Unemployment rate | 6.34 |
| Median home value | 158800 |
| Gini index | 0.4791 |
| Vacancy rate | 19.63 |
| White | 14368 |
| Black | 12291 |
| Asian | 210 |
| Native | 575 |
| Hispanic/Latino | 2067 |
| Bachelor's or higher | 4160 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 11](/us/states/ga/districts/senate/11.md) — 100% (state senate)
- [GA House District 171](/us/states/ga/districts/house/171.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
