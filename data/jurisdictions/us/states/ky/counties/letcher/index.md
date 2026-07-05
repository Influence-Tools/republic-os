---
type: Jurisdiction
title: "Letcher County, KY"
classification: county
fips: "21133"
state: "KY"
demographics:
  population: 20808
  population_under_18: 4542
  population_18_64: 11926
  population_65_plus: 4340
  median_household_income: 41793
  poverty_rate: 24.35
  homeownership_rate: 74.13
  unemployment_rate: 6.15
  median_home_value: 67400
  gini_index: 0.4295
  vacancy_rate: 20.18
  race_white: 20166
  race_black: 128
  race_asian: 40
  race_native: 8
  hispanic: 160
  bachelors_plus: 2683
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/senate/29"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/house/94"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Letcher County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20808 |
| Under 18 | 4542 |
| 18–64 | 11926 |
| 65+ | 4340 |
| Median household income | 41793 |
| Poverty rate | 24.35 |
| Homeownership rate | 74.13 |
| Unemployment rate | 6.15 |
| Median home value | 67400 |
| Gini index | 0.4295 |
| Vacancy rate | 20.18 |
| White | 20166 |
| Black | 128 |
| Asian | 40 |
| Native | 8 |
| Hispanic/Latino | 160 |
| Bachelor's or higher | 2683 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 29](/us/states/ky/districts/senate/29.md) — 100% (state senate)
- [KY House District 94](/us/states/ky/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
