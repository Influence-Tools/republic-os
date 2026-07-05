---
type: Jurisdiction
title: "Glasscock County, TX"
classification: county
fips: "48173"
state: "TX"
demographics:
  population: 1068
  population_under_18: 251
  population_18_64: 658
  population_65_plus: 159
  median_household_income: 101250
  poverty_rate: 8.9
  homeownership_rate: 68.48
  unemployment_rate: 0.78
  median_home_value: 245200
  gini_index: 0.4681
  vacancy_rate: 10.33
  race_white: 756
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 288
  bachelors_plus: 276
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/31"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Glasscock County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1068 |
| Under 18 | 251 |
| 18–64 | 658 |
| 65+ | 159 |
| Median household income | 101250 |
| Poverty rate | 8.9 |
| Homeownership rate | 68.48 |
| Unemployment rate | 0.78 |
| Median home value | 245200 |
| Gini index | 0.4681 |
| Vacancy rate | 10.33 |
| White | 756 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 288 |
| Bachelor's or higher | 276 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 31](/us/states/tx/districts/senate/31.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
