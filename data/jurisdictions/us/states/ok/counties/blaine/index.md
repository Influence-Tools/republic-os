---
type: Jurisdiction
title: "Blaine County, OK"
classification: county
fips: "40011"
state: "OK"
demographics:
  population: 8570
  population_under_18: 2108
  population_18_64: 4778
  population_65_plus: 1684
  median_household_income: 61642
  poverty_rate: 17.36
  homeownership_rate: 73.44
  unemployment_rate: 8.4
  median_home_value: 126900
  gini_index: 0.4351
  vacancy_rate: 26.2
  race_white: 6164
  race_black: 332
  race_asian: 3
  race_native: 575
  hispanic: 1078
  bachelors_plus: 1290
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/59"
    rel: in-district
    area_weight: 0.7734
  - to: "us/states/ok/districts/house/55"
    rel: in-district
    area_weight: 0.2264
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Blaine County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8570 |
| Under 18 | 2108 |
| 18–64 | 4778 |
| 65+ | 1684 |
| Median household income | 61642 |
| Poverty rate | 17.36 |
| Homeownership rate | 73.44 |
| Unemployment rate | 8.4 |
| Median home value | 126900 |
| Gini index | 0.4351 |
| Vacancy rate | 26.2 |
| White | 6164 |
| Black | 332 |
| Asian | 3 |
| Native | 575 |
| Hispanic/Latino | 1078 |
| Bachelor's or higher | 1290 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 26](/us/states/ok/districts/senate/26.md) — 100% (state senate)
- [OK House District 59](/us/states/ok/districts/house/59.md) — 77% (state house)
- [OK House District 55](/us/states/ok/districts/house/55.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
