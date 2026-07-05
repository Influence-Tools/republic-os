---
type: Jurisdiction
title: "Fannin County, GA"
classification: county
fips: "13111"
state: "GA"
demographics:
  population: 25742
  population_under_18: 3989
  population_18_64: 13788
  population_65_plus: 7965
  median_household_income: 57073
  poverty_rate: 13.7
  homeownership_rate: 78.57
  unemployment_rate: 3.69
  median_home_value: 306600
  gini_index: 0.5017
  vacancy_rate: 35.69
  race_white: 24004
  race_black: 92
  race_asian: 194
  race_native: 36
  hispanic: 848
  bachelors_plus: 6816
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ga/districts/senate/51"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/7"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Fannin County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25742 |
| Under 18 | 3989 |
| 18–64 | 13788 |
| 65+ | 7965 |
| Median household income | 57073 |
| Poverty rate | 13.7 |
| Homeownership rate | 78.57 |
| Unemployment rate | 3.69 |
| Median home value | 306600 |
| Gini index | 0.5017 |
| Vacancy rate | 35.69 |
| White | 24004 |
| Black | 92 |
| Asian | 194 |
| Native | 36 |
| Hispanic/Latino | 848 |
| Bachelor's or higher | 6816 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 51](/us/states/ga/districts/senate/51.md) — 100% (state senate)
- [GA House District 7](/us/states/ga/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
