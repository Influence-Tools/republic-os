---
type: Jurisdiction
title: "Allamakee County, IA"
classification: county
fips: "19005"
state: "IA"
demographics:
  population: 14092
  population_under_18: 3448
  population_18_64: 7386
  population_65_plus: 3258
  median_household_income: 70694
  poverty_rate: 10.1
  homeownership_rate: 79.56
  unemployment_rate: 2.46
  median_home_value: 172300
  gini_index: 0.4169
  vacancy_rate: 23.33
  race_white: 12416
  race_black: 257
  race_asian: 57
  race_native: 124
  hispanic: 1289
  bachelors_plus: 2797
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/64"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Allamakee County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14092 |
| Under 18 | 3448 |
| 18–64 | 7386 |
| 65+ | 3258 |
| Median household income | 70694 |
| Poverty rate | 10.1 |
| Homeownership rate | 79.56 |
| Unemployment rate | 2.46 |
| Median home value | 172300 |
| Gini index | 0.4169 |
| Vacancy rate | 23.33 |
| White | 12416 |
| Black | 257 |
| Asian | 57 |
| Native | 124 |
| Hispanic/Latino | 1289 |
| Bachelor's or higher | 2797 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 32](/us/states/ia/districts/senate/32.md) — 100% (state senate)
- [IA House District 64](/us/states/ia/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
