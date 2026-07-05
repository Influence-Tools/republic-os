---
type: Jurisdiction
title: "San Juan County, CO"
classification: county
fips: "08111"
state: "CO"
demographics:
  population: 724
  population_under_18: 93
  population_18_64: 373
  population_65_plus: 258
  median_household_income: 77824
  poverty_rate: 21.27
  homeownership_rate: 52.88
  unemployment_rate: 9.41
  median_home_value: 432500
  gini_index: 0.4373
  vacancy_rate: 45.93
  race_white: 619
  race_black: 0
  race_asian: 0
  race_native: 7
  hispanic: 132
  bachelors_plus: 421
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/house/59"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# San Juan County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 724 |
| Under 18 | 93 |
| 18–64 | 373 |
| 65+ | 258 |
| Median household income | 77824 |
| Poverty rate | 21.27 |
| Homeownership rate | 52.88 |
| Unemployment rate | 9.41 |
| Median home value | 432500 |
| Gini index | 0.4373 |
| Vacancy rate | 45.93 |
| White | 619 |
| Black | 0 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 132 |
| Bachelor's or higher | 421 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 59](/us/states/co/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
