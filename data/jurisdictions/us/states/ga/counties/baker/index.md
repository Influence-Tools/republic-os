---
type: Jurisdiction
title: "Baker County, GA"
classification: county
fips: "13007"
state: "GA"
demographics:
  population: 2790
  population_under_18: 447
  population_18_64: 1584
  population_65_plus: 759
  median_household_income: 46012
  poverty_rate: 26.27
  homeownership_rate: 76.71
  unemployment_rate: 6.72
  median_home_value: 119500
  gini_index: 0.5266
  vacancy_rate: 19.71
  race_white: 1434
  race_black: 1028
  race_asian: 168
  race_native: 14
  hispanic: 118
  bachelors_plus: 512
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Baker County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2790 |
| Under 18 | 447 |
| 18–64 | 1584 |
| 65+ | 759 |
| Median household income | 46012 |
| Poverty rate | 26.27 |
| Homeownership rate | 76.71 |
| Unemployment rate | 6.72 |
| Median home value | 119500 |
| Gini index | 0.5266 |
| Vacancy rate | 19.71 |
| White | 1434 |
| Black | 1028 |
| Asian | 168 |
| Native | 14 |
| Hispanic/Latino | 118 |
| Bachelor's or higher | 512 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
