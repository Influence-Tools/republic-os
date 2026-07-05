---
type: Jurisdiction
title: "Harney County, OR"
classification: county
fips: "41025"
state: "OR"
demographics:
  population: 7499
  population_under_18: 1389
  population_18_64: 4132
  population_65_plus: 1978
  median_household_income: 55208
  poverty_rate: 13.72
  homeownership_rate: 67.4
  unemployment_rate: 3.72
  median_home_value: 242100
  gini_index: 0.4668
  vacancy_rate: 16.16
  race_white: 6503
  race_black: 140
  race_asian: 15
  race_native: 135
  hispanic: 421
  bachelors_plus: 1472
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/house/60"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Harney County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7499 |
| Under 18 | 1389 |
| 18–64 | 4132 |
| 65+ | 1978 |
| Median household income | 55208 |
| Poverty rate | 13.72 |
| Homeownership rate | 67.4 |
| Unemployment rate | 3.72 |
| Median home value | 242100 |
| Gini index | 0.4668 |
| Vacancy rate | 16.16 |
| White | 6503 |
| Black | 140 |
| Asian | 15 |
| Native | 135 |
| Hispanic/Latino | 421 |
| Bachelor's or higher | 1472 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 60](/us/states/or/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
