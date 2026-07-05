---
type: Jurisdiction
title: "Jefferson County, IA"
classification: county
fips: "19101"
state: "IA"
demographics:
  population: 15705
  population_under_18: 2692
  population_18_64: 8821
  population_65_plus: 4192
  median_household_income: 61620
  poverty_rate: 15.19
  homeownership_rate: 67.69
  unemployment_rate: 7.95
  median_home_value: 163400
  gini_index: 0.4802
  vacancy_rate: 9.78
  race_white: 13253
  race_black: 399
  race_asian: 1285
  race_native: 123
  hispanic: 644
  bachelors_plus: 7293
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/44"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/88"
    rel: in-district
    area_weight: 0.5822
  - to: "us/states/ia/districts/house/87"
    rel: in-district
    area_weight: 0.4177
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Jefferson County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15705 |
| Under 18 | 2692 |
| 18–64 | 8821 |
| 65+ | 4192 |
| Median household income | 61620 |
| Poverty rate | 15.19 |
| Homeownership rate | 67.69 |
| Unemployment rate | 7.95 |
| Median home value | 163400 |
| Gini index | 0.4802 |
| Vacancy rate | 9.78 |
| White | 13253 |
| Black | 399 |
| Asian | 1285 |
| Native | 123 |
| Hispanic/Latino | 644 |
| Bachelor's or higher | 7293 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 44](/us/states/ia/districts/senate/44.md) — 100% (state senate)
- [IA House District 88](/us/states/ia/districts/house/88.md) — 58% (state house)
- [IA House District 87](/us/states/ia/districts/house/87.md) — 42% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
