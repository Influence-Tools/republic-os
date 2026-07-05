---
type: Jurisdiction
title: "Edmonson County, KY"
classification: county
fips: "21061"
state: "KY"
demographics:
  population: 12355
  population_under_18: 2225
  population_18_64: 7440
  population_65_plus: 2690
  median_household_income: 54937
  poverty_rate: 15.32
  homeownership_rate: 80.13
  unemployment_rate: 7.66
  median_home_value: 160300
  gini_index: 0.4485
  vacancy_rate: 20.93
  race_white: 11383
  race_black: 82
  race_asian: 77
  race_native: 10
  hispanic: 211
  bachelors_plus: 1483
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/9"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/house/19"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Edmonson County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12355 |
| Under 18 | 2225 |
| 18–64 | 7440 |
| 65+ | 2690 |
| Median household income | 54937 |
| Poverty rate | 15.32 |
| Homeownership rate | 80.13 |
| Unemployment rate | 7.66 |
| Median home value | 160300 |
| Gini index | 0.4485 |
| Vacancy rate | 20.93 |
| White | 11383 |
| Black | 82 |
| Asian | 77 |
| Native | 10 |
| Hispanic/Latino | 211 |
| Bachelor's or higher | 1483 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 9](/us/states/ky/districts/senate/9.md) — 100% (state senate)
- [KY House District 19](/us/states/ky/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
