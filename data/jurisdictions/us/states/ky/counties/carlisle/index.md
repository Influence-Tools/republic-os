---
type: Jurisdiction
title: "Carlisle County, KY"
classification: county
fips: "21039"
state: "KY"
demographics:
  population: 4762
  population_under_18: 1117
  population_18_64: 2687
  population_65_plus: 958
  median_household_income: 62439
  poverty_rate: 15.08
  homeownership_rate: 80.38
  unemployment_rate: 3.7
  median_home_value: 120400
  gini_index: 0.45
  vacancy_rate: 19.16
  race_white: 4332
  race_black: 71
  race_asian: 13
  race_native: 6
  hispanic: 153
  bachelors_plus: 700
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/senate/2"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/house/1"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Carlisle County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4762 |
| Under 18 | 1117 |
| 18–64 | 2687 |
| 65+ | 958 |
| Median household income | 62439 |
| Poverty rate | 15.08 |
| Homeownership rate | 80.38 |
| Unemployment rate | 3.7 |
| Median home value | 120400 |
| Gini index | 0.45 |
| Vacancy rate | 19.16 |
| White | 4332 |
| Black | 71 |
| Asian | 13 |
| Native | 6 |
| Hispanic/Latino | 153 |
| Bachelor's or higher | 700 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 2](/us/states/ky/districts/senate/2.md) — 100% (state senate)
- [KY House District 1](/us/states/ky/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
