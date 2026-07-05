---
type: Jurisdiction
title: "Mifflin County, PA"
classification: county
fips: "42087"
state: "PA"
demographics:
  population: 46041
  population_under_18: 10428
  population_18_64: 25483
  population_65_plus: 10130
  median_household_income: 63953
  poverty_rate: 16.23
  homeownership_rate: 71.13
  unemployment_rate: 2.66
  median_home_value: 156700
  gini_index: 0.3982
  vacancy_rate: 13.78
  race_white: 43044
  race_black: 449
  race_asian: 146
  race_native: 41
  hispanic: 1050
  bachelors_plus: 6637
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/171"
    rel: in-district
    area_weight: 0.8135
  - to: "us/states/pa/districts/house/85"
    rel: in-district
    area_weight: 0.1863
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Mifflin County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46041 |
| Under 18 | 10428 |
| 18–64 | 25483 |
| 65+ | 10130 |
| Median household income | 63953 |
| Poverty rate | 16.23 |
| Homeownership rate | 71.13 |
| Unemployment rate | 2.66 |
| Median home value | 156700 |
| Gini index | 0.3982 |
| Vacancy rate | 13.78 |
| White | 43044 |
| Black | 449 |
| Asian | 146 |
| Native | 41 |
| Hispanic/Latino | 1050 |
| Bachelor's or higher | 6637 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 30](/us/states/pa/districts/senate/30.md) — 100% (state senate)
- [PA House District 171](/us/states/pa/districts/house/171.md) — 81% (state house)
- [PA House District 85](/us/states/pa/districts/house/85.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
