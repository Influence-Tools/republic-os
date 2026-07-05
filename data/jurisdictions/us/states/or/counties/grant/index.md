---
type: Jurisdiction
title: "Grant County, OR"
classification: county
fips: "41023"
state: "OR"
demographics:
  population: 7209
  population_under_18: 1243
  population_18_64: 3635
  population_65_plus: 2331
  median_household_income: 59450
  poverty_rate: 12.82
  homeownership_rate: 76.74
  unemployment_rate: 5.21
  median_home_value: 229700
  gini_index: 0.409
  vacancy_rate: 17.15
  race_white: 6311
  race_black: 9
  race_asian: 57
  race_native: 53
  hispanic: 306
  bachelors_plus: 1269
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/60"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Grant County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7209 |
| Under 18 | 1243 |
| 18–64 | 3635 |
| 65+ | 2331 |
| Median household income | 59450 |
| Poverty rate | 12.82 |
| Homeownership rate | 76.74 |
| Unemployment rate | 5.21 |
| Median home value | 229700 |
| Gini index | 0.409 |
| Vacancy rate | 17.15 |
| White | 6311 |
| Black | 9 |
| Asian | 57 |
| Native | 53 |
| Hispanic/Latino | 306 |
| Bachelor's or higher | 1269 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 60](/us/states/or/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
