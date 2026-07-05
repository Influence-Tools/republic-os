---
type: Jurisdiction
title: "Park County, CO"
classification: county
fips: "08093"
state: "CO"
demographics:
  population: 17907
  population_under_18: 2554
  population_18_64: 11091
  population_65_plus: 4262
  median_household_income: 103670
  poverty_rate: 4.96
  homeownership_rate: 86.23
  unemployment_rate: 3.32
  median_home_value: 532100
  gini_index: 0.447
  vacancy_rate: 36.1
  race_white: 15913
  race_black: 169
  race_asian: 200
  race_native: 71
  hispanic: 1366
  bachelors_plus: 8290
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Park County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17907 |
| Under 18 | 2554 |
| 18–64 | 11091 |
| 65+ | 4262 |
| Median household income | 103670 |
| Poverty rate | 4.96 |
| Homeownership rate | 86.23 |
| Unemployment rate | 3.32 |
| Median home value | 532100 |
| Gini index | 0.447 |
| Vacancy rate | 36.1 |
| White | 15913 |
| Black | 169 |
| Asian | 200 |
| Native | 71 |
| Hispanic/Latino | 1366 |
| Bachelor's or higher | 8290 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 100% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
