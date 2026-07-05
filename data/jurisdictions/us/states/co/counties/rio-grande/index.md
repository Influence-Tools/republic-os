---
type: Jurisdiction
title: "Rio Grande County, CO"
classification: county
fips: "08105"
state: "CO"
demographics:
  population: 11321
  population_under_18: 2281
  population_18_64: 6462
  population_65_plus: 2578
  median_household_income: 64411
  poverty_rate: 18.01
  homeownership_rate: 67.1
  unemployment_rate: 10.15
  median_home_value: 239500
  gini_index: 0.4691
  vacancy_rate: 22.42
  race_white: 8268
  race_black: 63
  race_asian: 11
  race_native: 395
  hispanic: 4607
  bachelors_plus: 3817
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/62"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Rio Grande County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11321 |
| Under 18 | 2281 |
| 18–64 | 6462 |
| 65+ | 2578 |
| Median household income | 64411 |
| Poverty rate | 18.01 |
| Homeownership rate | 67.1 |
| Unemployment rate | 10.15 |
| Median home value | 239500 |
| Gini index | 0.4691 |
| Vacancy rate | 22.42 |
| White | 8268 |
| Black | 63 |
| Asian | 11 |
| Native | 395 |
| Hispanic/Latino | 4607 |
| Bachelor's or higher | 3817 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 62](/us/states/co/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
