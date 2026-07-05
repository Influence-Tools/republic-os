---
type: Jurisdiction
title: "Beaver County, OK"
classification: county
fips: "40007"
state: "OK"
demographics:
  population: 5028
  population_under_18: 1237
  population_18_64: 2784
  population_65_plus: 1007
  median_household_income: 64276
  poverty_rate: 13.25
  homeownership_rate: 80.87
  unemployment_rate: 2.62
  median_home_value: 130100
  gini_index: 0.4397
  vacancy_rate: 32.29
  race_white: 3461
  race_black: 37
  race_asian: 3
  race_native: 58
  hispanic: 1439
  bachelors_plus: 943
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/61"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Beaver County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5028 |
| Under 18 | 1237 |
| 18–64 | 2784 |
| 65+ | 1007 |
| Median household income | 64276 |
| Poverty rate | 13.25 |
| Homeownership rate | 80.87 |
| Unemployment rate | 2.62 |
| Median home value | 130100 |
| Gini index | 0.4397 |
| Vacancy rate | 32.29 |
| White | 3461 |
| Black | 37 |
| Asian | 3 |
| Native | 58 |
| Hispanic/Latino | 1439 |
| Bachelor's or higher | 943 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 61](/us/states/ok/districts/house/61.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
