---
type: Jurisdiction
title: "Palo Alto County, IA"
classification: county
fips: "19147"
state: "IA"
demographics:
  population: 8863
  population_under_18: 2044
  population_18_64: 4849
  population_65_plus: 1970
  median_household_income: 72781
  poverty_rate: 11.61
  homeownership_rate: 77.08
  unemployment_rate: 2.2
  median_home_value: 123200
  gini_index: 0.4157
  vacancy_rate: 16.6
  race_white: 8117
  race_black: 145
  race_asian: 57
  race_native: 21
  hispanic: 311
  bachelors_plus: 1423
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/10"
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

# Palo Alto County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8863 |
| Under 18 | 2044 |
| 18–64 | 4849 |
| 65+ | 1970 |
| Median household income | 72781 |
| Poverty rate | 11.61 |
| Homeownership rate | 77.08 |
| Unemployment rate | 2.2 |
| Median home value | 123200 |
| Gini index | 0.4157 |
| Vacancy rate | 16.6 |
| White | 8117 |
| Black | 145 |
| Asian | 57 |
| Native | 21 |
| Hispanic/Latino | 311 |
| Bachelor's or higher | 1423 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 5](/us/states/ia/districts/senate/5.md) — 100% (state senate)
- [IA House District 10](/us/states/ia/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
