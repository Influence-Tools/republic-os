---
type: Jurisdiction
title: "Brunswick County, NC"
classification: county
fips: "37019"
state: "NC"
demographics:
  population: 152568
  population_under_18: 21421
  population_18_64: 79543
  population_65_plus: 51604
  median_household_income: 77024
  poverty_rate: 9.23
  homeownership_rate: 84.59
  unemployment_rate: 4.65
  median_home_value: 349800
  gini_index: 0.4386
  vacancy_rate: 30.23
  race_white: 124657
  race_black: 12809
  race_asian: 1020
  race_native: 505
  hispanic: 8583
  bachelors_plus: 58355
districts:
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.8508
  - to: "us/states/nc/districts/senate/8"
    rel: in-district
    area_weight: 0.8476
  - to: "us/states/nc/districts/house/17"
    rel: in-district
    area_weight: 0.6171
  - to: "us/states/nc/districts/house/19"
    rel: in-district
    area_weight: 0.2304
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Brunswick County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 152568 |
| Under 18 | 21421 |
| 18–64 | 79543 |
| 65+ | 51604 |
| Median household income | 77024 |
| Poverty rate | 9.23 |
| Homeownership rate | 84.59 |
| Unemployment rate | 4.65 |
| Median home value | 349800 |
| Gini index | 0.4386 |
| Vacancy rate | 30.23 |
| White | 124657 |
| Black | 12809 |
| Asian | 1020 |
| Native | 505 |
| Hispanic/Latino | 8583 |
| Bachelor's or higher | 58355 |

## Districts

- [NC-07](/us/states/nc/districts/07.md) — 85% (congressional)
- [NC Senate District 8](/us/states/nc/districts/senate/8.md) — 85% (state senate)
- [NC House District 17](/us/states/nc/districts/house/17.md) — 62% (state house)
- [NC House District 19](/us/states/nc/districts/house/19.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
