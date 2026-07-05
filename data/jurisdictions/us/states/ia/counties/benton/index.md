---
type: Jurisdiction
title: "Benton County, IA"
classification: county
fips: "19011"
state: "IA"
demographics:
  population: 25724
  population_under_18: 5881
  population_18_64: 14750
  population_65_plus: 5093
  median_household_income: 86962
  poverty_rate: 7.38
  homeownership_rate: 84.99
  unemployment_rate: 2.01
  median_home_value: 208200
  gini_index: 0.3972
  vacancy_rate: 8.21
  race_white: 24375
  race_black: 107
  race_asian: 60
  race_native: 26
  hispanic: 507
  bachelors_plus: 6074
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/42"
    rel: in-district
    area_weight: 0.8388
  - to: "us/states/ia/districts/senate/38"
    rel: in-district
    area_weight: 0.1611
  - to: "us/states/ia/districts/house/84"
    rel: in-district
    area_weight: 0.8388
  - to: "us/states/ia/districts/house/76"
    rel: in-district
    area_weight: 0.1611
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Benton County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25724 |
| Under 18 | 5881 |
| 18–64 | 14750 |
| 65+ | 5093 |
| Median household income | 86962 |
| Poverty rate | 7.38 |
| Homeownership rate | 84.99 |
| Unemployment rate | 2.01 |
| Median home value | 208200 |
| Gini index | 0.3972 |
| Vacancy rate | 8.21 |
| White | 24375 |
| Black | 107 |
| Asian | 60 |
| Native | 26 |
| Hispanic/Latino | 507 |
| Bachelor's or higher | 6074 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 42](/us/states/ia/districts/senate/42.md) — 84% (state senate)
- [IA Senate District 38](/us/states/ia/districts/senate/38.md) — 16% (state senate)
- [IA House District 84](/us/states/ia/districts/house/84.md) — 84% (state house)
- [IA House District 76](/us/states/ia/districts/house/76.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
