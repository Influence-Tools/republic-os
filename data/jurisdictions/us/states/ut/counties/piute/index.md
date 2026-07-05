---
type: Jurisdiction
title: "Piute County, UT"
classification: county
fips: "49031"
state: "UT"
demographics:
  population: 1694
  population_under_18: 327
  population_18_64: 860
  population_65_plus: 507
  median_household_income: 48393
  poverty_rate: 10.2
  homeownership_rate: 95.5
  unemployment_rate: 5.86
  median_home_value: 264800
  gini_index: 0.455
  vacancy_rate: 36.13
  race_white: 1545
  race_black: 2
  race_asian: 0
  race_native: 0
  hispanic: 128
  bachelors_plus: 327
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/house/70"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Piute County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1694 |
| Under 18 | 327 |
| 18–64 | 860 |
| 65+ | 507 |
| Median household income | 48393 |
| Poverty rate | 10.2 |
| Homeownership rate | 95.5 |
| Unemployment rate | 5.86 |
| Median home value | 264800 |
| Gini index | 0.455 |
| Vacancy rate | 36.13 |
| White | 1545 |
| Black | 2 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 128 |
| Bachelor's or higher | 327 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 100% (state senate)
- [UT House District 70](/us/states/ut/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
