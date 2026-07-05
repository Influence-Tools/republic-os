---
type: Jurisdiction
title: "Beltrami County, MN"
classification: county
fips: "27007"
state: "MN"
demographics:
  population: 46512
  population_under_18: 11484
  population_18_64: 26852
  population_65_plus: 8176
  median_household_income: 68975
  poverty_rate: 16.14
  homeownership_rate: 70.12
  unemployment_rate: 4.68
  median_home_value: 237500
  gini_index: 0.444
  vacancy_rate: 16.37
  race_white: 32778
  race_black: 480
  race_asian: 287
  race_native: 8972
  hispanic: 1187
  bachelors_plus: 12754
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/2a"
    rel: in-district
    area_weight: 0.7767
  - to: "us/states/mn/districts/house/2b"
    rel: in-district
    area_weight: 0.2232
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Beltrami County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46512 |
| Under 18 | 11484 |
| 18–64 | 26852 |
| 65+ | 8176 |
| Median household income | 68975 |
| Poverty rate | 16.14 |
| Homeownership rate | 70.12 |
| Unemployment rate | 4.68 |
| Median home value | 237500 |
| Gini index | 0.444 |
| Vacancy rate | 16.37 |
| White | 32778 |
| Black | 480 |
| Asian | 287 |
| Native | 8972 |
| Hispanic/Latino | 1187 |
| Bachelor's or higher | 12754 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 2](/us/states/mn/districts/senate/2.md) — 100% (state senate)
- [MN House District 2A](/us/states/mn/districts/house/2a.md) — 78% (state house)
- [MN House District 2B](/us/states/mn/districts/house/2b.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
