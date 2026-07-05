---
type: Jurisdiction
title: "Oldham County, TX"
classification: county
fips: "48359"
state: "TX"
demographics:
  population: 2249
  population_under_18: 867
  population_18_64: 1118
  population_65_plus: 264
  median_household_income: 79900
  poverty_rate: 20.68
  homeownership_rate: 73.62
  unemployment_rate: 1.72
  median_home_value: 162800
  gini_index: 0.3937
  vacancy_rate: 20.88
  race_white: 1592
  race_black: 197
  race_asian: 7
  race_native: 0
  hispanic: 625
  bachelors_plus: 337
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/86"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Oldham County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2249 |
| Under 18 | 867 |
| 18–64 | 1118 |
| 65+ | 264 |
| Median household income | 79900 |
| Poverty rate | 20.68 |
| Homeownership rate | 73.62 |
| Unemployment rate | 1.72 |
| Median home value | 162800 |
| Gini index | 0.3937 |
| Vacancy rate | 20.88 |
| White | 1592 |
| Black | 197 |
| Asian | 7 |
| Native | 0 |
| Hispanic/Latino | 625 |
| Bachelor's or higher | 337 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 86](/us/states/tx/districts/house/86.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
