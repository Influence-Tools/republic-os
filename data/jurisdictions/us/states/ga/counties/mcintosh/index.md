---
type: Jurisdiction
title: "McIntosh County, GA"
classification: county
fips: "13191"
state: "GA"
demographics:
  population: 11312
  population_under_18: 1712
  population_18_64: 6252
  population_65_plus: 3348
  median_household_income: 50273
  poverty_rate: 22.99
  homeownership_rate: 80.03
  unemployment_rate: 3.17
  median_home_value: 182700
  gini_index: 0.4941
  vacancy_rate: 26.03
  race_white: 7218
  race_black: 3177
  race_asian: 43
  race_native: 22
  hispanic: 302
  bachelors_plus: 2488
districts:
  - to: "us/states/ga/districts/01"
    rel: in-district
    area_weight: 0.845
  - to: "us/states/ga/districts/senate/3"
    rel: in-district
    area_weight: 0.8266
  - to: "us/states/ga/districts/house/167"
    rel: in-district
    area_weight: 0.8266
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# McIntosh County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11312 |
| Under 18 | 1712 |
| 18–64 | 6252 |
| 65+ | 3348 |
| Median household income | 50273 |
| Poverty rate | 22.99 |
| Homeownership rate | 80.03 |
| Unemployment rate | 3.17 |
| Median home value | 182700 |
| Gini index | 0.4941 |
| Vacancy rate | 26.03 |
| White | 7218 |
| Black | 3177 |
| Asian | 43 |
| Native | 22 |
| Hispanic/Latino | 302 |
| Bachelor's or higher | 2488 |

## Districts

- [GA-01](/us/states/ga/districts/01.md) — 84% (congressional)
- [GA Senate District 3](/us/states/ga/districts/senate/3.md) — 83% (state senate)
- [GA House District 167](/us/states/ga/districts/house/167.md) — 83% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
