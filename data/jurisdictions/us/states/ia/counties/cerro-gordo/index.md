---
type: Jurisdiction
title: "Cerro Gordo County, IA"
classification: county
fips: "19033"
state: "IA"
demographics:
  population: 42632
  population_under_18: 8861
  population_18_64: 23735
  population_65_plus: 10036
  median_household_income: 68189
  poverty_rate: 10.56
  homeownership_rate: 70.35
  unemployment_rate: 2.61
  median_home_value: 166400
  gini_index: 0.4561
  vacancy_rate: 14.25
  race_white: 38231
  race_black: 987
  race_asian: 499
  race_native: 77
  hispanic: 2397
  bachelors_plus: 9788
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/59"
    rel: in-district
    area_weight: 0.6282
  - to: "us/states/ia/districts/house/60"
    rel: in-district
    area_weight: 0.3717
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Cerro Gordo County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42632 |
| Under 18 | 8861 |
| 18–64 | 23735 |
| 65+ | 10036 |
| Median household income | 68189 |
| Poverty rate | 10.56 |
| Homeownership rate | 70.35 |
| Unemployment rate | 2.61 |
| Median home value | 166400 |
| Gini index | 0.4561 |
| Vacancy rate | 14.25 |
| White | 38231 |
| Black | 987 |
| Asian | 499 |
| Native | 77 |
| Hispanic/Latino | 2397 |
| Bachelor's or higher | 9788 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 30](/us/states/ia/districts/senate/30.md) — 100% (state senate)
- [IA House District 59](/us/states/ia/districts/house/59.md) — 63% (state house)
- [IA House District 60](/us/states/ia/districts/house/60.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
