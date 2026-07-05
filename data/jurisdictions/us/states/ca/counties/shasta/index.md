---
type: Jurisdiction
title: "Shasta County, CA"
classification: county
fips: "06089"
state: "CA"
demographics:
  population: 181436
  population_under_18: 39148
  population_18_64: 103279
  population_65_plus: 39009
  median_household_income: 72636
  poverty_rate: 13.29
  homeownership_rate: 65.55
  unemployment_rate: 6.32
  median_home_value: 366400
  gini_index: 0.4658
  vacancy_rate: 11.04
  race_white: 141949
  race_black: 1651
  race_asian: 6375
  race_native: 3088
  hispanic: 21346
  bachelors_plus: 40413
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Shasta County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 181436 |
| Under 18 | 39148 |
| 18–64 | 103279 |
| 65+ | 39009 |
| Median household income | 72636 |
| Poverty rate | 13.29 |
| Homeownership rate | 65.55 |
| Unemployment rate | 6.32 |
| Median home value | 366400 |
| Gini index | 0.4658 |
| Vacancy rate | 11.04 |
| White | 141949 |
| Black | 1651 |
| Asian | 6375 |
| Native | 3088 |
| Hispanic/Latino | 21346 |
| Bachelor's or higher | 40413 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
