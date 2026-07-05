---
type: Jurisdiction
title: "Schley County, GA"
classification: county
fips: "13249"
state: "GA"
demographics:
  population: 4513
  population_under_18: 1112
  population_18_64: 2741
  population_65_plus: 660
  median_household_income: 56875
  poverty_rate: 13.89
  homeownership_rate: 80.05
  unemployment_rate: 7.61
  median_home_value: 143900
  gini_index: 0.4898
  vacancy_rate: 13.1
  race_white: 3734
  race_black: 657
  race_asian: 0
  race_native: 4
  hispanic: 65
  bachelors_plus: 998
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Schley County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4513 |
| Under 18 | 1112 |
| 18–64 | 2741 |
| 65+ | 660 |
| Median household income | 56875 |
| Poverty rate | 13.89 |
| Homeownership rate | 80.05 |
| Unemployment rate | 7.61 |
| Median home value | 143900 |
| Gini index | 0.4898 |
| Vacancy rate | 13.1 |
| White | 3734 |
| Black | 657 |
| Asian | 0 |
| Native | 4 |
| Hispanic/Latino | 65 |
| Bachelor's or higher | 998 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 100% (state senate)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
