---
type: Jurisdiction
title: "Trousdale County, TN"
classification: county
fips: "47169"
state: "TN"
demographics:
  population: 11957
  population_under_18: 1988
  population_18_64: 8494
  population_65_plus: 1475
  median_household_income: 72747
  poverty_rate: 11.87
  homeownership_rate: 74.46
  unemployment_rate: 0.64
  median_home_value: 337600
  gini_index: 0.3855
  vacancy_rate: 6.89
  race_white: 9517
  race_black: 1319
  race_asian: 9
  race_native: 25
  hispanic: 485
  bachelors_plus: 1851
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/35"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Trousdale County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11957 |
| Under 18 | 1988 |
| 18–64 | 8494 |
| 65+ | 1475 |
| Median household income | 72747 |
| Poverty rate | 11.87 |
| Homeownership rate | 74.46 |
| Unemployment rate | 0.64 |
| Median home value | 337600 |
| Gini index | 0.3855 |
| Vacancy rate | 6.89 |
| White | 9517 |
| Black | 1319 |
| Asian | 9 |
| Native | 25 |
| Hispanic/Latino | 485 |
| Bachelor's or higher | 1851 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 18](/us/states/tn/districts/senate/18.md) — 100% (state senate)
- [TN House District 35](/us/states/tn/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
