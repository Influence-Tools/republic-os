---
type: Jurisdiction
title: "Ida County, IA"
classification: county
fips: "19093"
state: "IA"
demographics:
  population: 6911
  population_under_18: 1680
  population_18_64: 3698
  population_65_plus: 1533
  median_household_income: 63073
  poverty_rate: 11.3
  homeownership_rate: 72.92
  unemployment_rate: 2.4
  median_home_value: 108900
  gini_index: 0.4365
  vacancy_rate: 9.47
  race_white: 6395
  race_black: 23
  race_asian: 46
  race_native: 32
  hispanic: 286
  bachelors_plus: 1255
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/12"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Ida County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6911 |
| Under 18 | 1680 |
| 18–64 | 3698 |
| 65+ | 1533 |
| Median household income | 63073 |
| Poverty rate | 11.3 |
| Homeownership rate | 72.92 |
| Unemployment rate | 2.4 |
| Median home value | 108900 |
| Gini index | 0.4365 |
| Vacancy rate | 9.47 |
| White | 6395 |
| Black | 23 |
| Asian | 46 |
| Native | 32 |
| Hispanic/Latino | 286 |
| Bachelor's or higher | 1255 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 6](/us/states/ia/districts/senate/6.md) — 100% (state senate)
- [IA House District 12](/us/states/ia/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
