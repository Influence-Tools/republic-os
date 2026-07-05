---
type: Jurisdiction
title: "Jasper County, TX"
classification: county
fips: "48241"
state: "TX"
demographics:
  population: 32727
  population_under_18: 7617
  population_18_64: 18196
  population_65_plus: 6914
  median_household_income: 56723
  poverty_rate: 20.74
  homeownership_rate: 79.02
  unemployment_rate: 13.26
  median_home_value: 136400
  gini_index: 0.4665
  vacancy_rate: 17.23
  race_white: 24241
  race_black: 5001
  race_asian: 147
  race_native: 26
  hispanic: 2288
  bachelors_plus: 4245
districts:
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/21"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Jasper County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32727 |
| Under 18 | 7617 |
| 18–64 | 18196 |
| 65+ | 6914 |
| Median household income | 56723 |
| Poverty rate | 20.74 |
| Homeownership rate | 79.02 |
| Unemployment rate | 13.26 |
| Median home value | 136400 |
| Gini index | 0.4665 |
| Vacancy rate | 17.23 |
| White | 24241 |
| Black | 5001 |
| Asian | 147 |
| Native | 26 |
| Hispanic/Latino | 2288 |
| Bachelor's or higher | 4245 |

## Districts

- [TX-36](/us/states/tx/districts/36.md) — 100% (congressional)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 100% (state senate)
- [TX House District 21](/us/states/tx/districts/house/21.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
