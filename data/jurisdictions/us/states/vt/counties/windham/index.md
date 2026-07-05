---
type: Jurisdiction
title: "Windham County, VT"
classification: county
fips: "50025"
state: "VT"
demographics:
  population: 45923
  population_under_18: 7729
  population_18_64: 26447
  population_65_plus: 11747
  median_household_income: 72217
  poverty_rate: 11.58
  homeownership_rate: 73.94
  unemployment_rate: 4.76
  median_home_value: 279600
  gini_index: 0.4718
  vacancy_rate: 34.45
  race_white: 41871
  race_black: 394
  race_asian: 548
  race_native: 75
  hispanic: 1423
  bachelors_plus: 22380
districts:
  - to: "us/states/vt/districts/00"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, vt]
timestamp: "2026-07-03"
---

# Windham County, VT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45923 |
| Under 18 | 7729 |
| 18–64 | 26447 |
| 65+ | 11747 |
| Median household income | 72217 |
| Poverty rate | 11.58 |
| Homeownership rate | 73.94 |
| Unemployment rate | 4.76 |
| Median home value | 279600 |
| Gini index | 0.4718 |
| Vacancy rate | 34.45 |
| White | 41871 |
| Black | 394 |
| Asian | 548 |
| Native | 75 |
| Hispanic/Latino | 1423 |
| Bachelor's or higher | 22380 |

## Districts

- [VT-00](/us/states/vt/districts/00.md) — 100% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
