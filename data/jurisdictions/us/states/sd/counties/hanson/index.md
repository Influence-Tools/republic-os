---
type: Jurisdiction
title: "Hanson County, SD"
classification: county
fips: "46061"
state: "SD"
demographics:
  population: 3472
  population_under_18: 996
  population_18_64: 1910
  population_65_plus: 566
  median_household_income: 81071
  poverty_rate: 7.03
  homeownership_rate: 89.4
  unemployment_rate: 1.8
  median_home_value: 191200
  gini_index: 0.4057
  vacancy_rate: 12.32
  race_white: 3195
  race_black: 12
  race_asian: 0
  race_native: 0
  hispanic: 48
  bachelors_plus: 628
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/19"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/sd/districts/house/19"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Hanson County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3472 |
| Under 18 | 996 |
| 18–64 | 1910 |
| 65+ | 566 |
| Median household income | 81071 |
| Poverty rate | 7.03 |
| Homeownership rate | 89.4 |
| Unemployment rate | 1.8 |
| Median home value | 191200 |
| Gini index | 0.4057 |
| Vacancy rate | 12.32 |
| White | 3195 |
| Black | 12 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 48 |
| Bachelor's or higher | 628 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 19](/us/states/sd/districts/senate/19.md) — 100% (state senate)
- [SD House District 19](/us/states/sd/districts/house/19.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
