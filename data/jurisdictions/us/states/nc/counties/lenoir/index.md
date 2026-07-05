---
type: Jurisdiction
title: "Lenoir County, NC"
classification: county
fips: "37107"
state: "NC"
demographics:
  population: 54919
  population_under_18: 12393
  population_18_64: 30745
  population_65_plus: 11781
  median_household_income: 45143
  poverty_rate: 21.95
  homeownership_rate: 59.21
  unemployment_rate: 9.03
  median_home_value: 120500
  gini_index: 0.4794
  vacancy_rate: 13.13
  race_white: 27167
  race_black: 21560
  race_asian: 425
  race_native: 139
  hispanic: 4843
  bachelors_plus: 8499
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/nc/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/12"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Lenoir County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54919 |
| Under 18 | 12393 |
| 18–64 | 30745 |
| 65+ | 11781 |
| Median household income | 45143 |
| Poverty rate | 21.95 |
| Homeownership rate | 59.21 |
| Unemployment rate | 9.03 |
| Median home value | 120500 |
| Gini index | 0.4794 |
| Vacancy rate | 13.13 |
| White | 27167 |
| Black | 21560 |
| Asian | 425 |
| Native | 139 |
| Hispanic/Latino | 4843 |
| Bachelor's or higher | 8499 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 3](/us/states/nc/districts/senate/3.md) — 100% (state senate)
- [NC House District 12](/us/states/nc/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
