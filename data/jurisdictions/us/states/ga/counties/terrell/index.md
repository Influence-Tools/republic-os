---
type: Jurisdiction
title: "Terrell County, GA"
classification: county
fips: "13273"
state: "GA"
demographics:
  population: 8850
  population_under_18: 1975
  population_18_64: 5025
  population_65_plus: 1850
  median_household_income: 46171
  poverty_rate: 33.27
  homeownership_rate: 61.6
  unemployment_rate: 4.1
  median_home_value: 118400
  gini_index: 0.4805
  vacancy_rate: 20.44
  race_white: 3246
  race_black: 5311
  race_asian: 13
  race_native: 0
  hispanic: 234
  bachelors_plus: 1227
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Terrell County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8850 |
| Under 18 | 1975 |
| 18–64 | 5025 |
| 65+ | 1850 |
| Median household income | 46171 |
| Poverty rate | 33.27 |
| Homeownership rate | 61.6 |
| Unemployment rate | 4.1 |
| Median home value | 118400 |
| Gini index | 0.4805 |
| Vacancy rate | 20.44 |
| White | 3246 |
| Black | 5311 |
| Asian | 13 |
| Native | 0 |
| Hispanic/Latino | 234 |
| Bachelor's or higher | 1227 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
