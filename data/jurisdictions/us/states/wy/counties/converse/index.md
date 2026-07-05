---
type: Jurisdiction
title: "Converse County, WY"
classification: county
fips: "56009"
state: "WY"
demographics:
  population: 13762
  population_under_18: 3298
  population_18_64: 7929
  population_65_plus: 2535
  median_household_income: 81558
  poverty_rate: 10.56
  homeownership_rate: 77.3
  unemployment_rate: 4.18
  median_home_value: 292700
  gini_index: 0.4133
  vacancy_rate: 13.15
  race_white: 12631
  race_black: 78
  race_asian: 28
  race_native: 4
  hispanic: 1127
  bachelors_plus: 3299
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/2"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wy/districts/house/6"
    rel: in-district
    area_weight: 0.6587
  - to: "us/states/wy/districts/house/62"
    rel: in-district
    area_weight: 0.3409
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Converse County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13762 |
| Under 18 | 3298 |
| 18–64 | 7929 |
| 65+ | 2535 |
| Median household income | 81558 |
| Poverty rate | 10.56 |
| Homeownership rate | 77.3 |
| Unemployment rate | 4.18 |
| Median home value | 292700 |
| Gini index | 0.4133 |
| Vacancy rate | 13.15 |
| White | 12631 |
| Black | 78 |
| Asian | 28 |
| Native | 4 |
| Hispanic/Latino | 1127 |
| Bachelor's or higher | 3299 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 2](/us/states/wy/districts/senate/2.md) — 100% (state senate)
- [WY House District 6](/us/states/wy/districts/house/6.md) — 66% (state house)
- [WY House District 62](/us/states/wy/districts/house/62.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
