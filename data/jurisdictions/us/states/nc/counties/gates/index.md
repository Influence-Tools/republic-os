---
type: Jurisdiction
title: "Gates County, NC"
classification: county
fips: "37073"
state: "NC"
demographics:
  population: 10376
  population_under_18: 1994
  population_18_64: 6025
  population_65_plus: 2357
  median_household_income: 66333
  poverty_rate: 9.41
  homeownership_rate: 80.87
  unemployment_rate: 5.85
  median_home_value: 170800
  gini_index: 0.3834
  vacancy_rate: 13.16
  race_white: 6569
  race_black: 3220
  race_asian: 0
  race_native: 56
  hispanic: 225
  bachelors_plus: 1154
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/house/5"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Gates County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10376 |
| Under 18 | 1994 |
| 18–64 | 6025 |
| 65+ | 2357 |
| Median household income | 66333 |
| Poverty rate | 9.41 |
| Homeownership rate | 80.87 |
| Unemployment rate | 5.85 |
| Median home value | 170800 |
| Gini index | 0.3834 |
| Vacancy rate | 13.16 |
| White | 6569 |
| Black | 3220 |
| Asian | 0 |
| Native | 56 |
| Hispanic/Latino | 225 |
| Bachelor's or higher | 1154 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 100% (state senate)
- [NC House District 5](/us/states/nc/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
