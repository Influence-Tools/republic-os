---
type: Jurisdiction
title: "Williamson County, IL"
classification: county
fips: "17199"
state: "IL"
demographics:
  population: 66876
  population_under_18: 14227
  population_18_64: 39513
  population_65_plus: 13136
  median_household_income: 65604
  poverty_rate: 13.75
  homeownership_rate: 70.65
  unemployment_rate: 5.01
  median_home_value: 156400
  gini_index: 0.4417
  vacancy_rate: 9.67
  race_white: 59489
  race_black: 2988
  race_asian: 1000
  race_native: 186
  hispanic: 1947
  bachelors_plus: 17778
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.6138
  - to: "us/states/il/districts/house/118"
    rel: in-district
    area_weight: 0.3862
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Williamson County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66876 |
| Under 18 | 14227 |
| 18–64 | 39513 |
| 65+ | 13136 |
| Median household income | 65604 |
| Poverty rate | 13.75 |
| Homeownership rate | 70.65 |
| Unemployment rate | 5.01 |
| Median home value | 156400 |
| Gini index | 0.4417 |
| Vacancy rate | 9.67 |
| White | 59489 |
| Black | 2988 |
| Asian | 1000 |
| Native | 186 |
| Hispanic/Latino | 1947 |
| Bachelor's or higher | 17778 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 61% (state house)
- [IL House District 118](/us/states/il/districts/house/118.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
