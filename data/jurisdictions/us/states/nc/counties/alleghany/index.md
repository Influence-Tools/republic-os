---
type: Jurisdiction
title: "Alleghany County, NC"
classification: county
fips: "37005"
state: "NC"
demographics:
  population: 11174
  population_under_18: 1832
  population_18_64: 5907
  population_65_plus: 3435
  median_household_income: 47172
  poverty_rate: 15.98
  homeownership_rate: 74.43
  unemployment_rate: 3.71
  median_home_value: 214800
  gini_index: 0.4905
  vacancy_rate: 33.66
  race_white: 9932
  race_black: 193
  race_asian: 52
  race_native: 9
  hispanic: 1274
  bachelors_plus: 2728
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/93"
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

# Alleghany County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11174 |
| Under 18 | 1832 |
| 18–64 | 5907 |
| 65+ | 3435 |
| Median household income | 47172 |
| Poverty rate | 15.98 |
| Homeownership rate | 74.43 |
| Unemployment rate | 3.71 |
| Median home value | 214800 |
| Gini index | 0.4905 |
| Vacancy rate | 33.66 |
| White | 9932 |
| Black | 193 |
| Asian | 52 |
| Native | 9 |
| Hispanic/Latino | 1274 |
| Bachelor's or higher | 2728 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 100% (state senate)
- [NC House District 93](/us/states/nc/districts/house/93.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
