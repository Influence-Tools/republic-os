---
type: Jurisdiction
title: "McDuffie County, GA"
classification: county
fips: "13189"
state: "GA"
demographics:
  population: 21718
  population_under_18: 5367
  population_18_64: 12233
  population_65_plus: 4118
  median_household_income: 56733
  poverty_rate: 20.32
  homeownership_rate: 65.03
  unemployment_rate: 1.95
  median_home_value: 170200
  gini_index: 0.4717
  vacancy_rate: 14.31
  race_white: 12021
  race_black: 8712
  race_asian: 68
  race_native: 0
  hispanic: 800
  bachelors_plus: 3692
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/125"
    rel: in-district
    area_weight: 0.5074
  - to: "us/states/ga/districts/house/128"
    rel: in-district
    area_weight: 0.4924
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# McDuffie County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21718 |
| Under 18 | 5367 |
| 18–64 | 12233 |
| 65+ | 4118 |
| Median household income | 56733 |
| Poverty rate | 20.32 |
| Homeownership rate | 65.03 |
| Unemployment rate | 1.95 |
| Median home value | 170200 |
| Gini index | 0.4717 |
| Vacancy rate | 14.31 |
| White | 12021 |
| Black | 8712 |
| Asian | 68 |
| Native | 0 |
| Hispanic/Latino | 800 |
| Bachelor's or higher | 3692 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 125](/us/states/ga/districts/house/125.md) — 51% (state house)
- [GA House District 128](/us/states/ga/districts/house/128.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
