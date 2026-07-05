---
type: Jurisdiction
title: "Lake County, CO"
classification: county
fips: "08065"
state: "CO"
demographics:
  population: 7380
  population_under_18: 1369
  population_18_64: 4895
  population_65_plus: 1116
  median_household_income: 96575
  poverty_rate: 7.91
  homeownership_rate: 75.63
  unemployment_rate: 2.2
  median_home_value: 466100
  gini_index: 0.4061
  vacancy_rate: 24.18
  race_white: 4739
  race_black: 4
  race_asian: 11
  race_native: 35
  hispanic: 2423
  bachelors_plus: 3538
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9955
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/co/districts/house/13"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Lake County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7380 |
| Under 18 | 1369 |
| 18–64 | 4895 |
| 65+ | 1116 |
| Median household income | 96575 |
| Poverty rate | 7.91 |
| Homeownership rate | 75.63 |
| Unemployment rate | 2.2 |
| Median home value | 466100 |
| Gini index | 0.4061 |
| Vacancy rate | 24.18 |
| White | 4739 |
| Black | 4 |
| Asian | 11 |
| Native | 35 |
| Hispanic/Latino | 2423 |
| Bachelor's or higher | 3538 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 100% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 100% (state senate)
- [CO House District 13](/us/states/co/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
