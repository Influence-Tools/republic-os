---
type: Jurisdiction
title: "Union County, TN"
classification: county
fips: "47173"
state: "TN"
demographics:
  population: 20431
  population_under_18: 4352
  population_18_64: 12230
  population_65_plus: 3849
  median_household_income: 62727
  poverty_rate: 13.8
  homeownership_rate: 80.19
  unemployment_rate: 2.63
  median_home_value: 204000
  gini_index: 0.4246
  vacancy_rate: 19.33
  race_white: 19327
  race_black: 70
  race_asian: 11
  race_native: 0
  hispanic: 485
  bachelors_plus: 2801
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/36"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Union County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20431 |
| Under 18 | 4352 |
| 18–64 | 12230 |
| 65+ | 3849 |
| Median household income | 62727 |
| Poverty rate | 13.8 |
| Homeownership rate | 80.19 |
| Unemployment rate | 2.63 |
| Median home value | 204000 |
| Gini index | 0.4246 |
| Vacancy rate | 19.33 |
| White | 19327 |
| Black | 70 |
| Asian | 11 |
| Native | 0 |
| Hispanic/Latino | 485 |
| Bachelor's or higher | 2801 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 100% (congressional)
- [TN Senate District 8](/us/states/tn/districts/senate/8.md) — 100% (state senate)
- [TN House District 36](/us/states/tn/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
