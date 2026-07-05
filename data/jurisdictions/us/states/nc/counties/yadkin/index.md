---
type: Jurisdiction
title: "Yadkin County, NC"
classification: county
fips: "37197"
state: "NC"
demographics:
  population: 37574
  population_under_18: 7761
  population_18_64: 21936
  population_65_plus: 7877
  median_household_income: 62932
  poverty_rate: 13.98
  homeownership_rate: 76.93
  unemployment_rate: 5.31
  median_home_value: 181200
  gini_index: 0.4613
  vacancy_rate: 13.01
  race_white: 31232
  race_black: 647
  race_asian: 23
  race_native: 277
  hispanic: 4676
  bachelors_plus: 6116
districts:
  - to: "us/states/nc/districts/10"
    rel: in-district
    area_weight: 0.9945
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.0054
  - to: "us/states/nc/districts/senate/36"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/house/77"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Yadkin County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37574 |
| Under 18 | 7761 |
| 18–64 | 21936 |
| 65+ | 7877 |
| Median household income | 62932 |
| Poverty rate | 13.98 |
| Homeownership rate | 76.93 |
| Unemployment rate | 5.31 |
| Median home value | 181200 |
| Gini index | 0.4613 |
| Vacancy rate | 13.01 |
| White | 31232 |
| Black | 647 |
| Asian | 23 |
| Native | 277 |
| Hispanic/Latino | 4676 |
| Bachelor's or higher | 6116 |

## Districts

- [NC-10](/us/states/nc/districts/10.md) — 99% (congressional)
- [NC-05](/us/states/nc/districts/05.md) — 1% (congressional)
- [NC Senate District 36](/us/states/nc/districts/senate/36.md) — 100% (state senate)
- [NC House District 77](/us/states/nc/districts/house/77.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
