---
type: Jurisdiction
title: "Latimer County, OK"
classification: county
fips: "40077"
state: "OK"
demographics:
  population: 9518
  population_under_18: 2088
  population_18_64: 5325
  population_65_plus: 2105
  median_household_income: 41405
  poverty_rate: 20.7
  homeownership_rate: 72.37
  unemployment_rate: 5.69
  median_home_value: 107900
  gini_index: 0.4466
  vacancy_rate: 17.09
  race_white: 5907
  race_black: 128
  race_asian: 26
  race_native: 2441
  hispanic: 391
  bachelors_plus: 933
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/17"
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

# Latimer County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9518 |
| Under 18 | 2088 |
| 18–64 | 5325 |
| 65+ | 2105 |
| Median household income | 41405 |
| Poverty rate | 20.7 |
| Homeownership rate | 72.37 |
| Unemployment rate | 5.69 |
| Median home value | 107900 |
| Gini index | 0.4466 |
| Vacancy rate | 17.09 |
| White | 5907 |
| Black | 128 |
| Asian | 26 |
| Native | 2441 |
| Hispanic/Latino | 391 |
| Bachelor's or higher | 933 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 7](/us/states/ok/districts/senate/7.md) — 100% (state senate)
- [OK House District 17](/us/states/ok/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
