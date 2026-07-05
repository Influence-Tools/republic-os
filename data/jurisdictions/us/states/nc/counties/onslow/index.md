---
type: Jurisdiction
title: "Onslow County, NC"
classification: county
fips: "37133"
state: "NC"
demographics:
  population: 207906
  population_under_18: 51514
  population_18_64: 135203
  population_65_plus: 21189
  median_household_income: 68148
  poverty_rate: 11.59
  homeownership_rate: 63.74
  unemployment_rate: 5.37
  median_home_value: 236400
  gini_index: 0.4203
  vacancy_rate: 13.84
  race_white: 139725
  race_black: 25041
  race_asian: 3934
  race_native: 1465
  hispanic: 29152
  bachelors_plus: 40106
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.8993
  - to: "us/states/nc/districts/senate/6"
    rel: in-district
    area_weight: 0.8853
  - to: "us/states/nc/districts/house/14"
    rel: in-district
    area_weight: 0.3528
  - to: "us/states/nc/districts/house/15"
    rel: in-district
    area_weight: 0.3376
  - to: "us/states/nc/districts/house/16"
    rel: in-district
    area_weight: 0.1949
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Onslow County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 207906 |
| Under 18 | 51514 |
| 18–64 | 135203 |
| 65+ | 21189 |
| Median household income | 68148 |
| Poverty rate | 11.59 |
| Homeownership rate | 63.74 |
| Unemployment rate | 5.37 |
| Median home value | 236400 |
| Gini index | 0.4203 |
| Vacancy rate | 13.84 |
| White | 139725 |
| Black | 25041 |
| Asian | 3934 |
| Native | 1465 |
| Hispanic/Latino | 29152 |
| Bachelor's or higher | 40106 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 90% (congressional)
- [NC Senate District 6](/us/states/nc/districts/senate/6.md) — 89% (state senate)
- [NC House District 14](/us/states/nc/districts/house/14.md) — 35% (state house)
- [NC House District 15](/us/states/nc/districts/house/15.md) — 34% (state house)
- [NC House District 16](/us/states/nc/districts/house/16.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
