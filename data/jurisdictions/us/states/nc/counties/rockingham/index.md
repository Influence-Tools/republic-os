---
type: Jurisdiction
title: "Rockingham County, NC"
classification: county
fips: "37157"
state: "NC"
demographics:
  population: 92131
  population_under_18: 18711
  population_18_64: 53944
  population_65_plus: 19476
  median_household_income: 57053
  poverty_rate: 16.28
  homeownership_rate: 72.07
  unemployment_rate: 5.79
  median_home_value: 168600
  gini_index: 0.4613
  vacancy_rate: 9.72
  race_white: 66859
  race_black: 15915
  race_asian: 302
  race_native: 476
  hispanic: 6605
  bachelors_plus: 15130
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/house/65"
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

# Rockingham County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92131 |
| Under 18 | 18711 |
| 18–64 | 53944 |
| 65+ | 19476 |
| Median household income | 57053 |
| Poverty rate | 16.28 |
| Homeownership rate | 72.07 |
| Unemployment rate | 5.79 |
| Median home value | 168600 |
| Gini index | 0.4613 |
| Vacancy rate | 9.72 |
| White | 66859 |
| Black | 15915 |
| Asian | 302 |
| Native | 476 |
| Hispanic/Latino | 6605 |
| Bachelor's or higher | 15130 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 26](/us/states/nc/districts/senate/26.md) — 100% (state senate)
- [NC House District 65](/us/states/nc/districts/house/65.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
