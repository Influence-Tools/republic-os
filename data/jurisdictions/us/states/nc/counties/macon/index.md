---
type: Jurisdiction
title: "Macon County, NC"
classification: county
fips: "37113"
state: "NC"
demographics:
  population: 37941
  population_under_18: 6723
  population_18_64: 20139
  population_65_plus: 11079
  median_household_income: 59061
  poverty_rate: 11.6
  homeownership_rate: 77.61
  unemployment_rate: 2.8
  median_home_value: 251900
  gini_index: 0.4832
  vacancy_rate: 32.37
  race_white: 32821
  race_black: 523
  race_asian: 295
  race_native: 141
  hispanic: 3806
  bachelors_plus: 11054
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/120"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Macon County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37941 |
| Under 18 | 6723 |
| 18–64 | 20139 |
| 65+ | 11079 |
| Median household income | 59061 |
| Poverty rate | 11.6 |
| Homeownership rate | 77.61 |
| Unemployment rate | 2.8 |
| Median home value | 251900 |
| Gini index | 0.4832 |
| Vacancy rate | 32.37 |
| White | 32821 |
| Black | 523 |
| Asian | 295 |
| Native | 141 |
| Hispanic/Latino | 3806 |
| Bachelor's or higher | 11054 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 120](/us/states/nc/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
