---
type: Jurisdiction
title: "Bennington County, VT"
classification: county
fips: "50003"
state: "VT"
demographics:
  population: 37269
  population_under_18: 6953
  population_18_64: 21228
  population_65_plus: 9088
  median_household_income: 73325
  poverty_rate: 11.33
  homeownership_rate: 73.68
  unemployment_rate: 4.41
  median_home_value: 279900
  gini_index: 0.5174
  vacancy_rate: 28.3
  race_white: 34230
  race_black: 435
  race_asian: 317
  race_native: 36
  hispanic: 1047
  bachelors_plus: 16644
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Bennington County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37269 |
| Under 18 | 6953 |
| 18–64 | 21228 |
| 65+ | 9088 |
| Median household income | 73325 |
| Poverty rate | 11.33 |
| Homeownership rate | 73.68 |
| Unemployment rate | 4.41 |
| Median home value | 279900 |
| Gini index | 0.5174 |
| Vacancy rate | 28.3 |
| White | 34230 |
| Black | 435 |
| Asian | 317 |
| Native | 36 |
| Hispanic/Latino | 1047 |
| Bachelor's or higher | 16644 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
