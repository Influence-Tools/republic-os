---
type: Jurisdiction
title: "Early County, GA"
classification: county
fips: "13099"
state: "GA"
demographics:
  population: 10603
  population_under_18: 2586
  population_18_64: 5907
  population_65_plus: 2110
  median_household_income: 54083
  poverty_rate: 23.62
  homeownership_rate: 66.63
  unemployment_rate: 6.74
  median_home_value: 131300
  gini_index: 0.4738
  vacancy_rate: 16.99
  race_white: 4357
  race_black: 5652
  race_asian: 45
  race_native: 4
  hispanic: 67
  bachelors_plus: 1483
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Early County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10603 |
| Under 18 | 2586 |
| 18–64 | 5907 |
| 65+ | 2110 |
| Median household income | 54083 |
| Poverty rate | 23.62 |
| Homeownership rate | 66.63 |
| Unemployment rate | 6.74 |
| Median home value | 131300 |
| Gini index | 0.4738 |
| Vacancy rate | 16.99 |
| White | 4357 |
| Black | 5652 |
| Asian | 45 |
| Native | 4 |
| Hispanic/Latino | 67 |
| Bachelor's or higher | 1483 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
