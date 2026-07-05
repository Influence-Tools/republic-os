---
type: Jurisdiction
title: "Randolph County, GA"
classification: county
fips: "13243"
state: "GA"
demographics:
  population: 6196
  population_under_18: 1675
  population_18_64: 3147
  population_65_plus: 1374
  median_household_income: 28380
  poverty_rate: 30.04
  homeownership_rate: 51.53
  unemployment_rate: 10.94
  median_home_value: 90200
  gini_index: 0.5296
  vacancy_rate: 23.46
  race_white: 1672
  race_black: 4174
  race_asian: 5
  race_native: 0
  hispanic: 261
  bachelors_plus: 924
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Randolph County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6196 |
| Under 18 | 1675 |
| 18–64 | 3147 |
| 65+ | 1374 |
| Median household income | 28380 |
| Poverty rate | 30.04 |
| Homeownership rate | 51.53 |
| Unemployment rate | 10.94 |
| Median home value | 90200 |
| Gini index | 0.5296 |
| Vacancy rate | 23.46 |
| White | 1672 |
| Black | 4174 |
| Asian | 5 |
| Native | 0 |
| Hispanic/Latino | 261 |
| Bachelor's or higher | 924 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
