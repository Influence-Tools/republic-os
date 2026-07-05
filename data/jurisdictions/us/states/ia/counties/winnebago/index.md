---
type: Jurisdiction
title: "Winnebago County, IA"
classification: county
fips: "19189"
state: "IA"
demographics:
  population: 10583
  population_under_18: 2229
  population_18_64: 6013
  population_65_plus: 2341
  median_household_income: 67642
  poverty_rate: 11.18
  homeownership_rate: 70.61
  unemployment_rate: 3.01
  median_home_value: 135000
  gini_index: 0.4418
  vacancy_rate: 8.59
  race_white: 9463
  race_black: 237
  race_asian: 140
  race_native: 22
  hispanic: 619
  bachelors_plus: 2434
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ia/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/9"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Winnebago County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10583 |
| Under 18 | 2229 |
| 18–64 | 6013 |
| 65+ | 2341 |
| Median household income | 67642 |
| Poverty rate | 11.18 |
| Homeownership rate | 70.61 |
| Unemployment rate | 3.01 |
| Median home value | 135000 |
| Gini index | 0.4418 |
| Vacancy rate | 8.59 |
| White | 9463 |
| Black | 237 |
| Asian | 140 |
| Native | 22 |
| Hispanic/Latino | 619 |
| Bachelor's or higher | 2434 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 5](/us/states/ia/districts/senate/5.md) — 100% (state senate)
- [IA House District 9](/us/states/ia/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
