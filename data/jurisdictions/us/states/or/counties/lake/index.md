---
type: Jurisdiction
title: "Lake County, OR"
classification: county
fips: "41037"
state: "OR"
demographics:
  population: 8267
  population_under_18: 1481
  population_18_64: 4700
  population_65_plus: 2086
  median_household_income: 62787
  poverty_rate: 14.86
  homeownership_rate: 67.33
  unemployment_rate: 4.14
  median_home_value: 219500
  gini_index: 0.4313
  vacancy_rate: 17.81
  race_white: 6633
  race_black: 40
  race_asian: 12
  race_native: 175
  hispanic: 896
  bachelors_plus: 1694
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9999
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

# Lake County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8267 |
| Under 18 | 1481 |
| 18–64 | 4700 |
| 65+ | 2086 |
| Median household income | 62787 |
| Poverty rate | 14.86 |
| Homeownership rate | 67.33 |
| Unemployment rate | 4.14 |
| Median home value | 219500 |
| Gini index | 0.4313 |
| Vacancy rate | 17.81 |
| White | 6633 |
| Black | 40 |
| Asian | 12 |
| Native | 175 |
| Hispanic/Latino | 896 |
| Bachelor's or higher | 1694 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 60](/us/states/or/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
