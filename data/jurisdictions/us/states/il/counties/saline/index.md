---
type: Jurisdiction
title: "Saline County, IL"
classification: county
fips: "17165"
state: "IL"
demographics:
  population: 23213
  population_under_18: 4799
  population_18_64: 13418
  population_65_plus: 4996
  median_household_income: 53117
  poverty_rate: 18.94
  homeownership_rate: 72.55
  unemployment_rate: 7.73
  median_home_value: 94300
  gini_index: 0.5251
  vacancy_rate: 13.19
  race_white: 21292
  race_black: 719
  race_asian: 127
  race_native: 24
  hispanic: 502
  bachelors_plus: 4289
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Saline County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23213 |
| Under 18 | 4799 |
| 18–64 | 13418 |
| 65+ | 4996 |
| Median household income | 53117 |
| Poverty rate | 18.94 |
| Homeownership rate | 72.55 |
| Unemployment rate | 7.73 |
| Median home value | 94300 |
| Gini index | 0.5251 |
| Vacancy rate | 13.19 |
| White | 21292 |
| Black | 719 |
| Asian | 127 |
| Native | 24 |
| Hispanic/Latino | 502 |
| Bachelor's or higher | 4289 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
