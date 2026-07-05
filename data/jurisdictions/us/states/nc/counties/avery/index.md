---
type: Jurisdiction
title: "Avery County, NC"
classification: county
fips: "37011"
state: "NC"
demographics:
  population: 17680
  population_under_18: 2554
  population_18_64: 10946
  population_65_plus: 4180
  median_household_income: 61428
  poverty_rate: 10.16
  homeownership_rate: 83.01
  unemployment_rate: 4.85
  median_home_value: 265800
  gini_index: 0.4659
  vacancy_rate: 52.18
  race_white: 15338
  race_black: 676
  race_asian: 77
  race_native: 19
  hispanic: 1070
  bachelors_plus: 4542
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9947
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/85"
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

# Avery County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17680 |
| Under 18 | 2554 |
| 18–64 | 10946 |
| 65+ | 4180 |
| Median household income | 61428 |
| Poverty rate | 10.16 |
| Homeownership rate | 83.01 |
| Unemployment rate | 4.85 |
| Median home value | 265800 |
| Gini index | 0.4659 |
| Vacancy rate | 52.18 |
| White | 15338 |
| Black | 676 |
| Asian | 77 |
| Native | 19 |
| Hispanic/Latino | 1070 |
| Bachelor's or higher | 4542 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 99% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 100% (state senate)
- [NC House District 85](/us/states/nc/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
