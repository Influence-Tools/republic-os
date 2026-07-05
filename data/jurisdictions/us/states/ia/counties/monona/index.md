---
type: Jurisdiction
title: "Monona County, IA"
classification: county
fips: "19133"
state: "IA"
demographics:
  population: 8557
  population_under_18: 1935
  population_18_64: 4538
  population_65_plus: 2084
  median_household_income: 68377
  poverty_rate: 10.64
  homeownership_rate: 75.68
  unemployment_rate: 1.62
  median_home_value: 142900
  gini_index: 0.4132
  vacancy_rate: 11.3
  race_white: 7994
  race_black: 21
  race_asian: 0
  race_native: 40
  hispanic: 233
  bachelors_plus: 1570
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ia/districts/senate/7"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ia/districts/house/13"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Monona County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8557 |
| Under 18 | 1935 |
| 18–64 | 4538 |
| 65+ | 2084 |
| Median household income | 68377 |
| Poverty rate | 10.64 |
| Homeownership rate | 75.68 |
| Unemployment rate | 1.62 |
| Median home value | 142900 |
| Gini index | 0.4132 |
| Vacancy rate | 11.3 |
| White | 7994 |
| Black | 21 |
| Asian | 0 |
| Native | 40 |
| Hispanic/Latino | 233 |
| Bachelor's or higher | 1570 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 7](/us/states/ia/districts/senate/7.md) — 100% (state senate)
- [IA House District 13](/us/states/ia/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
