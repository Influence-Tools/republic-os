---
type: Jurisdiction
title: "Pender County, NC"
classification: county
fips: "37141"
state: "NC"
demographics:
  population: 65550
  population_under_18: 14710
  population_18_64: 38908
  population_65_plus: 11932
  median_household_income: 80396
  poverty_rate: 9.73
  homeownership_rate: 82.7
  unemployment_rate: 4.82
  median_home_value: 299000
  gini_index: 0.4317
  vacancy_rate: 20.58
  race_white: 49242
  race_black: 7951
  race_asian: 537
  race_native: 193
  hispanic: 5787
  bachelors_plus: 18869
districts:
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.9434
  - to: "us/states/nc/districts/senate/9"
    rel: in-district
    area_weight: 0.9443
  - to: "us/states/nc/districts/house/16"
    rel: in-district
    area_weight: 0.9442
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Pender County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65550 |
| Under 18 | 14710 |
| 18–64 | 38908 |
| 65+ | 11932 |
| Median household income | 80396 |
| Poverty rate | 9.73 |
| Homeownership rate | 82.7 |
| Unemployment rate | 4.82 |
| Median home value | 299000 |
| Gini index | 0.4317 |
| Vacancy rate | 20.58 |
| White | 49242 |
| Black | 7951 |
| Asian | 537 |
| Native | 193 |
| Hispanic/Latino | 5787 |
| Bachelor's or higher | 18869 |

## Districts

- [NC-07](/us/states/nc/districts/07.md) — 94% (congressional)
- [NC Senate District 9](/us/states/nc/districts/senate/9.md) — 94% (state senate)
- [NC House District 16](/us/states/nc/districts/house/16.md) — 94% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
