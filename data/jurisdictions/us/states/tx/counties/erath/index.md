---
type: Jurisdiction
title: "Erath County, TX"
classification: county
fips: "48143"
state: "TX"
demographics:
  population: 43794
  population_under_18: 9073
  population_18_64: 28224
  population_65_plus: 6497
  median_household_income: 65115
  poverty_rate: 16.56
  homeownership_rate: 63.15
  unemployment_rate: 5.69
  median_home_value: 269100
  gini_index: 0.4649
  vacancy_rate: 10.05
  race_white: 34730
  race_black: 835
  race_asian: 441
  race_native: 335
  hispanic: 9757
  bachelors_plus: 11350
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/59"
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

# Erath County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43794 |
| Under 18 | 9073 |
| 18–64 | 28224 |
| 65+ | 6497 |
| Median household income | 65115 |
| Poverty rate | 16.56 |
| Homeownership rate | 63.15 |
| Unemployment rate | 5.69 |
| Median home value | 269100 |
| Gini index | 0.4649 |
| Vacancy rate | 10.05 |
| White | 34730 |
| Black | 835 |
| Asian | 441 |
| Native | 335 |
| Hispanic/Latino | 9757 |
| Bachelor's or higher | 11350 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 59](/us/states/tx/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
