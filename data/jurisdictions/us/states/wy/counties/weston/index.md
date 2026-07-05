---
type: Jurisdiction
title: "Weston County, WY"
classification: county
fips: "56045"
state: "WY"
demographics:
  population: 6826
  population_under_18: 1340
  population_18_64: 3976
  population_65_plus: 1510
  median_household_income: 89509
  poverty_rate: 9.01
  homeownership_rate: 86.83
  unemployment_rate: 1.03
  median_home_value: 221700
  gini_index: 0.4149
  vacancy_rate: 16.38
  race_white: 5819
  race_black: 18
  race_asian: 48
  race_native: 173
  hispanic: 365
  bachelors_plus: 1294
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/1"
    rel: in-district
    area_weight: 0.5484
  - to: "us/states/wy/districts/senate/3"
    rel: in-district
    area_weight: 0.4514
  - to: "us/states/wy/districts/house/1"
    rel: in-district
    area_weight: 0.5483
  - to: "us/states/wy/districts/house/2"
    rel: in-district
    area_weight: 0.4514
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Weston County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6826 |
| Under 18 | 1340 |
| 18–64 | 3976 |
| 65+ | 1510 |
| Median household income | 89509 |
| Poverty rate | 9.01 |
| Homeownership rate | 86.83 |
| Unemployment rate | 1.03 |
| Median home value | 221700 |
| Gini index | 0.4149 |
| Vacancy rate | 16.38 |
| White | 5819 |
| Black | 18 |
| Asian | 48 |
| Native | 173 |
| Hispanic/Latino | 365 |
| Bachelor's or higher | 1294 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 1](/us/states/wy/districts/senate/1.md) — 55% (state senate)
- [WY Senate District 3](/us/states/wy/districts/senate/3.md) — 45% (state senate)
- [WY House District 1](/us/states/wy/districts/house/1.md) — 55% (state house)
- [WY House District 2](/us/states/wy/districts/house/2.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
