---
type: Jurisdiction
title: "Nantucket County, MA"
classification: county
fips: "25019"
state: "MA"
demographics:
  population: 14483
  population_under_18: 2975
  population_18_64: 9181
  population_65_plus: 2327
  median_household_income: 139688
  poverty_rate: 3.16
  homeownership_rate: 71.78
  unemployment_rate: 4.32
  median_home_value: 1593800
  gini_index: 0.4719
  vacancy_rate: 58.3
  race_white: 10090
  race_black: 1372
  race_asian: 251
  race_native: 8
  hispanic: 2467
  bachelors_plus: 8240
districts:
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.1959
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Nantucket County, MA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14483 |
| Under 18 | 2975 |
| 18–64 | 9181 |
| 65+ | 2327 |
| Median household income | 139688 |
| Poverty rate | 3.16 |
| Homeownership rate | 71.78 |
| Unemployment rate | 4.32 |
| Median home value | 1593800 |
| Gini index | 0.4719 |
| Vacancy rate | 58.3 |
| White | 10090 |
| Black | 1372 |
| Asian | 251 |
| Native | 8 |
| Hispanic/Latino | 2467 |
| Bachelor's or higher | 8240 |

## Districts

- [MA-09](/us/states/ma/districts/09.md) — 20% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
