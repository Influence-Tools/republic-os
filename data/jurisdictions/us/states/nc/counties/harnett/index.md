---
type: Jurisdiction
title: "Harnett County, NC"
classification: county
fips: "37085"
state: "NC"
demographics:
  population: 139150
  population_under_18: 35394
  population_18_64: 84683
  population_65_plus: 19073
  median_household_income: 71287
  poverty_rate: 13.75
  homeownership_rate: 71.03
  unemployment_rate: 4.69
  median_home_value: 246200
  gini_index: 0.4415
  vacancy_rate: 9.21
  race_white: 86245
  race_black: 28104
  race_asian: 1331
  race_native: 1674
  hispanic: 21043
  bachelors_plus: 30283
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/nc/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/6"
    rel: in-district
    area_weight: 0.748
  - to: "us/states/nc/districts/house/53"
    rel: in-district
    area_weight: 0.2516
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Harnett County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 139150 |
| Under 18 | 35394 |
| 18–64 | 84683 |
| 65+ | 19073 |
| Median household income | 71287 |
| Poverty rate | 13.75 |
| Homeownership rate | 71.03 |
| Unemployment rate | 4.69 |
| Median home value | 246200 |
| Gini index | 0.4415 |
| Vacancy rate | 9.21 |
| White | 86245 |
| Black | 28104 |
| Asian | 1331 |
| Native | 1674 |
| Hispanic/Latino | 21043 |
| Bachelor's or higher | 30283 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 100% (congressional)
- [NC Senate District 12](/us/states/nc/districts/senate/12.md) — 100% (state senate)
- [NC House District 6](/us/states/nc/districts/house/6.md) — 75% (state house)
- [NC House District 53](/us/states/nc/districts/house/53.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
