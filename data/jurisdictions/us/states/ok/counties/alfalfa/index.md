---
type: Jurisdiction
title: "Alfalfa County, OK"
classification: county
fips: "40003"
state: "OK"
demographics:
  population: 5696
  population_under_18: 1045
  population_18_64: 3482
  population_65_plus: 1169
  median_household_income: 64615
  poverty_rate: 16.51
  homeownership_rate: 77.5
  unemployment_rate: 4.29
  median_home_value: 101500
  gini_index: 0.4177
  vacancy_rate: 21.41
  race_white: 4668
  race_black: 213
  race_asian: 24
  race_native: 141
  hispanic: 351
  bachelors_plus: 1120
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/58"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Alfalfa County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5696 |
| Under 18 | 1045 |
| 18–64 | 3482 |
| 65+ | 1169 |
| Median household income | 64615 |
| Poverty rate | 16.51 |
| Homeownership rate | 77.5 |
| Unemployment rate | 4.29 |
| Median home value | 101500 |
| Gini index | 0.4177 |
| Vacancy rate | 21.41 |
| White | 4668 |
| Black | 213 |
| Asian | 24 |
| Native | 141 |
| Hispanic/Latino | 351 |
| Bachelor's or higher | 1120 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 19](/us/states/ok/districts/senate/19.md) — 100% (state senate)
- [OK House District 58](/us/states/ok/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
