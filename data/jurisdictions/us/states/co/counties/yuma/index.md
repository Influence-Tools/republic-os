---
type: Jurisdiction
title: "Yuma County, CO"
classification: county
fips: "08125"
state: "CO"
demographics:
  population: 9979
  population_under_18: 2953
  population_18_64: 2800
  population_65_plus: 4226
  median_household_income: 60545
  poverty_rate: 17.93
  homeownership_rate: 68.93
  unemployment_rate: 4.46
  median_home_value: 211700
  gini_index: 0.4672
  vacancy_rate: 5.95
  race_white: 7086
  race_black: 25
  race_asian: 27
  race_native: 75
  hispanic: 3021
  bachelors_plus: 2251
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Yuma County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9979 |
| Under 18 | 2953 |
| 18–64 | 2800 |
| 65+ | 4226 |
| Median household income | 60545 |
| Poverty rate | 17.93 |
| Homeownership rate | 68.93 |
| Unemployment rate | 4.46 |
| Median home value | 211700 |
| Gini index | 0.4672 |
| Vacancy rate | 5.95 |
| White | 7086 |
| Black | 25 |
| Asian | 27 |
| Native | 75 |
| Hispanic/Latino | 3021 |
| Bachelor's or higher | 2251 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 100% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
