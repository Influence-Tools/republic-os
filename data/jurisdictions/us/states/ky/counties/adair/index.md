---
type: Jurisdiction
title: "Adair County, KY"
classification: county
fips: "21001"
state: "KY"
demographics:
  population: 19089
  population_under_18: 3761
  population_18_64: 11573
  population_65_plus: 3755
  median_household_income: 53553
  poverty_rate: 18.39
  homeownership_rate: 77.21
  unemployment_rate: 6.82
  median_home_value: 150800
  gini_index: 0.4725
  vacancy_rate: 17.48
  race_white: 17337
  race_black: 395
  race_asian: 45
  race_native: 3
  hispanic: 671
  bachelors_plus: 4169
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/senate/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/house/21"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Adair County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19089 |
| Under 18 | 3761 |
| 18–64 | 11573 |
| 65+ | 3755 |
| Median household income | 53553 |
| Poverty rate | 18.39 |
| Homeownership rate | 77.21 |
| Unemployment rate | 6.82 |
| Median home value | 150800 |
| Gini index | 0.4725 |
| Vacancy rate | 17.48 |
| White | 17337 |
| Black | 395 |
| Asian | 45 |
| Native | 3 |
| Hispanic/Latino | 671 |
| Bachelor's or higher | 4169 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 16](/us/states/ky/districts/senate/16.md) — 100% (state senate)
- [KY House District 21](/us/states/ky/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
