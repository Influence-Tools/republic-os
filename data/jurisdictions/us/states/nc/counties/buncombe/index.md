---
type: Jurisdiction
title: "Buncombe County, NC"
classification: county
fips: "37021"
state: "NC"
demographics:
  population: 274360
  population_under_18: 48925
  population_18_64: 167144
  population_65_plus: 58291
  median_household_income: 74436
  poverty_rate: 11.84
  homeownership_rate: 66.18
  unemployment_rate: 4.29
  median_home_value: 391800
  gini_index: 0.4811
  vacancy_rate: 24.26
  race_white: 224885
  race_black: 13276
  race_asian: 3089
  race_native: 559
  hispanic: 23475
  bachelors_plus: 133068
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/senate/46"
    rel: in-district
    area_weight: 0.5627
  - to: "us/states/nc/districts/senate/49"
    rel: in-district
    area_weight: 0.4369
  - to: "us/states/nc/districts/house/115"
    rel: in-district
    area_weight: 0.5331
  - to: "us/states/nc/districts/house/114"
    rel: in-district
    area_weight: 0.3826
  - to: "us/states/nc/districts/house/116"
    rel: in-district
    area_weight: 0.0838
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Buncombe County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 274360 |
| Under 18 | 48925 |
| 18–64 | 167144 |
| 65+ | 58291 |
| Median household income | 74436 |
| Poverty rate | 11.84 |
| Homeownership rate | 66.18 |
| Unemployment rate | 4.29 |
| Median home value | 391800 |
| Gini index | 0.4811 |
| Vacancy rate | 24.26 |
| White | 224885 |
| Black | 13276 |
| Asian | 3089 |
| Native | 559 |
| Hispanic/Latino | 23475 |
| Bachelor's or higher | 133068 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 46](/us/states/nc/districts/senate/46.md) — 56% (state senate)
- [NC Senate District 49](/us/states/nc/districts/senate/49.md) — 44% (state senate)
- [NC House District 115](/us/states/nc/districts/house/115.md) — 53% (state house)
- [NC House District 114](/us/states/nc/districts/house/114.md) — 38% (state house)
- [NC House District 116](/us/states/nc/districts/house/116.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
