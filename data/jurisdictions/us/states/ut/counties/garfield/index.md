---
type: Jurisdiction
title: "Garfield County, UT"
classification: county
fips: "49017"
state: "UT"
demographics:
  population: 5219
  population_under_18: 1123
  population_18_64: 2926
  population_65_plus: 1170
  median_household_income: 61875
  poverty_rate: 9.81
  homeownership_rate: 70.32
  unemployment_rate: 4.09
  median_home_value: 318100
  gini_index: 0.4557
  vacancy_rate: 43.59
  race_white: 4925
  race_black: 6
  race_asian: 0
  race_native: 27
  hispanic: 381
  bachelors_plus: 1376
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.7008
  - to: "us/states/ut/districts/senate/26"
    rel: in-district
    area_weight: 0.2992
  - to: "us/states/ut/districts/house/69"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Garfield County, UT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5219 |
| Under 18 | 1123 |
| 18–64 | 2926 |
| 65+ | 1170 |
| Median household income | 61875 |
| Poverty rate | 9.81 |
| Homeownership rate | 70.32 |
| Unemployment rate | 4.09 |
| Median home value | 318100 |
| Gini index | 0.4557 |
| Vacancy rate | 43.59 |
| White | 4925 |
| Black | 6 |
| Asian | 0 |
| Native | 27 |
| Hispanic/Latino | 381 |
| Bachelor's or higher | 1376 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 70% (state senate)
- [UT Senate District 26](/us/states/ut/districts/senate/26.md) — 30% (state senate)
- [UT House District 69](/us/states/ut/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
