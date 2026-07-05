---
type: Jurisdiction
title: "Collingsworth County, TX"
classification: county
fips: "48087"
state: "TX"
demographics:
  population: 2588
  population_under_18: 721
  population_18_64: 1239
  population_65_plus: 628
  median_household_income: 61280
  poverty_rate: 21.76
  homeownership_rate: 73.85
  unemployment_rate: 1.11
  median_home_value: 104000
  gini_index: 0.4069
  vacancy_rate: 34.43
  race_white: 1482
  race_black: 115
  race_asian: 0
  race_native: 49
  hispanic: 844
  bachelors_plus: 581
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Collingsworth County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2588 |
| Under 18 | 721 |
| 18–64 | 1239 |
| 65+ | 628 |
| Median household income | 61280 |
| Poverty rate | 21.76 |
| Homeownership rate | 73.85 |
| Unemployment rate | 1.11 |
| Median home value | 104000 |
| Gini index | 0.4069 |
| Vacancy rate | 34.43 |
| White | 1482 |
| Black | 115 |
| Asian | 0 |
| Native | 49 |
| Hispanic/Latino | 844 |
| Bachelor's or higher | 581 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
