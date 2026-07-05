---
type: Jurisdiction
title: "Polk County, MN"
classification: county
fips: "27119"
state: "MN"
demographics:
  population: 30705
  population_under_18: 7520
  population_18_64: 17323
  population_65_plus: 5862
  median_household_income: 73107
  poverty_rate: 11.88
  homeownership_rate: 71.27
  unemployment_rate: 3.59
  median_home_value: 222800
  gini_index: 0.4337
  vacancy_rate: 15.9
  race_white: 26349
  race_black: 604
  race_asian: 247
  race_native: 232
  hispanic: 2122
  bachelors_plus: 7663
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/mn/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mn/districts/house/1b"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Polk County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30705 |
| Under 18 | 7520 |
| 18–64 | 17323 |
| 65+ | 5862 |
| Median household income | 73107 |
| Poverty rate | 11.88 |
| Homeownership rate | 71.27 |
| Unemployment rate | 3.59 |
| Median home value | 222800 |
| Gini index | 0.4337 |
| Vacancy rate | 15.9 |
| White | 26349 |
| Black | 604 |
| Asian | 247 |
| Native | 232 |
| Hispanic/Latino | 2122 |
| Bachelor's or higher | 7663 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 1](/us/states/mn/districts/senate/1.md) — 100% (state senate)
- [MN House District 1B](/us/states/mn/districts/house/1b.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
