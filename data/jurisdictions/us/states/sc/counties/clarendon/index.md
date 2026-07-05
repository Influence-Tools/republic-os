---
type: Jurisdiction
title: "Clarendon County, SC"
classification: county
fips: "45027"
state: "SC"
demographics:
  population: 30986
  population_under_18: 5642
  population_18_64: 17617
  population_65_plus: 7727
  median_household_income: 52401
  poverty_rate: 15.43
  homeownership_rate: 72.94
  unemployment_rate: 6.85
  median_home_value: 158000
  gini_index: 0.4714
  vacancy_rate: 23.2
  race_white: 15667
  race_black: 13687
  race_asian: 260
  race_native: 121
  hispanic: 1005
  bachelors_plus: 5524
districts:
  - to: "us/states/sc/districts/06"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/sc/districts/senate/36"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sc/districts/house/64"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Clarendon County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30986 |
| Under 18 | 5642 |
| 18–64 | 17617 |
| 65+ | 7727 |
| Median household income | 52401 |
| Poverty rate | 15.43 |
| Homeownership rate | 72.94 |
| Unemployment rate | 6.85 |
| Median home value | 158000 |
| Gini index | 0.4714 |
| Vacancy rate | 23.2 |
| White | 15667 |
| Black | 13687 |
| Asian | 260 |
| Native | 121 |
| Hispanic/Latino | 1005 |
| Bachelor's or higher | 5524 |

## Districts

- [SC-06](/us/states/sc/districts/06.md) — 100% (congressional)
- [SC Senate District 36](/us/states/sc/districts/senate/36.md) — 100% (state senate)
- [SC House District 64](/us/states/sc/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
