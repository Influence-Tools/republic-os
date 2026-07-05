---
type: Jurisdiction
title: "Butte County, SD"
classification: county
fips: "46019"
state: "SD"
demographics:
  population: 10676
  population_under_18: 2647
  population_18_64: 5880
  population_65_plus: 2149
  median_household_income: 75652
  poverty_rate: 8.63
  homeownership_rate: 76.15
  unemployment_rate: 1.8
  median_home_value: 244600
  gini_index: 0.4573
  vacancy_rate: 9.97
  race_white: 9496
  race_black: 0
  race_asian: 50
  race_native: 167
  hispanic: 456
  bachelors_plus: 1815
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/28b"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Butte County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10676 |
| Under 18 | 2647 |
| 18–64 | 5880 |
| 65+ | 2149 |
| Median household income | 75652 |
| Poverty rate | 8.63 |
| Homeownership rate | 76.15 |
| Unemployment rate | 1.8 |
| Median home value | 244600 |
| Gini index | 0.4573 |
| Vacancy rate | 9.97 |
| White | 9496 |
| Black | 0 |
| Asian | 50 |
| Native | 167 |
| Hispanic/Latino | 456 |
| Bachelor's or higher | 1815 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 28](/us/states/sd/districts/senate/28.md) — 100% (state senate)
- [SD House District 28B](/us/states/sd/districts/house/28b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
