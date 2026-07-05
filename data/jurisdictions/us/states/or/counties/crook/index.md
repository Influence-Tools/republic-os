---
type: Jurisdiction
title: "Crook County, OR"
classification: county
fips: "41013"
state: "OR"
demographics:
  population: 26277
  population_under_18: 5121
  population_18_64: 14518
  population_65_plus: 6638
  median_household_income: 81965
  poverty_rate: 11.28
  homeownership_rate: 74.08
  unemployment_rate: 5.95
  median_home_value: 467000
  gini_index: 0.4131
  vacancy_rate: 8.63
  race_white: 23003
  race_black: 138
  race_asian: 82
  race_native: 234
  hispanic: 2071
  bachelors_plus: 5513
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/59"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Crook County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26277 |
| Under 18 | 5121 |
| 18–64 | 14518 |
| 65+ | 6638 |
| Median household income | 81965 |
| Poverty rate | 11.28 |
| Homeownership rate | 74.08 |
| Unemployment rate | 5.95 |
| Median home value | 467000 |
| Gini index | 0.4131 |
| Vacancy rate | 8.63 |
| White | 23003 |
| Black | 138 |
| Asian | 82 |
| Native | 234 |
| Hispanic/Latino | 2071 |
| Bachelor's or higher | 5513 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 59](/us/states/or/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
