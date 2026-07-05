---
type: Jurisdiction
title: "Bon Homme County, SD"
classification: county
fips: "46009"
state: "SD"
demographics:
  population: 7044
  population_under_18: 1307
  population_18_64: 4223
  population_65_plus: 1514
  median_household_income: 64435
  poverty_rate: 10.57
  homeownership_rate: 80.48
  unemployment_rate: 2.2
  median_home_value: 134100
  gini_index: 0.4311
  vacancy_rate: 14.92
  race_white: 6096
  race_black: 164
  race_asian: 7
  race_native: 404
  hispanic: 166
  bachelors_plus: 1348
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/sd/districts/senate/19"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/sd/districts/house/19"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Bon Homme County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7044 |
| Under 18 | 1307 |
| 18–64 | 4223 |
| 65+ | 1514 |
| Median household income | 64435 |
| Poverty rate | 10.57 |
| Homeownership rate | 80.48 |
| Unemployment rate | 2.2 |
| Median home value | 134100 |
| Gini index | 0.4311 |
| Vacancy rate | 14.92 |
| White | 6096 |
| Black | 164 |
| Asian | 7 |
| Native | 404 |
| Hispanic/Latino | 166 |
| Bachelor's or higher | 1348 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 19](/us/states/sd/districts/senate/19.md) — 100% (state senate)
- [SD House District 19](/us/states/sd/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
