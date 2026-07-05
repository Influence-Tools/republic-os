---
type: Jurisdiction
title: "Bee County, TX"
classification: county
fips: "48025"
state: "TX"
demographics:
  population: 31083
  population_under_18: 6213
  population_18_64: 20920
  population_65_plus: 3950
  median_household_income: 57673
  poverty_rate: 17.6
  homeownership_rate: 70.82
  unemployment_rate: 5.21
  median_home_value: 111300
  gini_index: 0.4841
  vacancy_rate: 17.31
  race_white: 13725
  race_black: 2262
  race_asian: 156
  race_native: 218
  hispanic: 19208
  bachelors_plus: 3926
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/43"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Bee County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31083 |
| Under 18 | 6213 |
| 18–64 | 20920 |
| 65+ | 3950 |
| Median household income | 57673 |
| Poverty rate | 17.6 |
| Homeownership rate | 70.82 |
| Unemployment rate | 5.21 |
| Median home value | 111300 |
| Gini index | 0.4841 |
| Vacancy rate | 17.31 |
| White | 13725 |
| Black | 2262 |
| Asian | 156 |
| Native | 218 |
| Hispanic/Latino | 19208 |
| Bachelor's or higher | 3926 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 100% (state senate)
- [TX House District 43](/us/states/tx/districts/house/43.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
