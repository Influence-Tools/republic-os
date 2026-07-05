---
type: Jurisdiction
title: "Audubon County, IA"
classification: county
fips: "19009"
state: "IA"
demographics:
  population: 5599
  population_under_18: 1210
  population_18_64: 2964
  population_65_plus: 1425
  median_household_income: 58229
  poverty_rate: 11.76
  homeownership_rate: 76.16
  unemployment_rate: 1.3
  median_home_value: 121900
  gini_index: 0.4576
  vacancy_rate: 6.95
  race_white: 5293
  race_black: 28
  race_asian: 3
  race_native: 10
  hispanic: 140
  bachelors_plus: 995
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ia/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/11"
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

# Audubon County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5599 |
| Under 18 | 1210 |
| 18–64 | 2964 |
| 65+ | 1425 |
| Median household income | 58229 |
| Poverty rate | 11.76 |
| Homeownership rate | 76.16 |
| Unemployment rate | 1.3 |
| Median home value | 121900 |
| Gini index | 0.4576 |
| Vacancy rate | 6.95 |
| White | 5293 |
| Black | 28 |
| Asian | 3 |
| Native | 10 |
| Hispanic/Latino | 140 |
| Bachelor's or higher | 995 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 6](/us/states/ia/districts/senate/6.md) — 100% (state senate)
- [IA House District 11](/us/states/ia/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
