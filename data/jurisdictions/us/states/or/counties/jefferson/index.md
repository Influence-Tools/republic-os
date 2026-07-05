---
type: Jurisdiction
title: "Jefferson County, OR"
classification: county
fips: "41031"
state: "OR"
demographics:
  population: 25203
  population_under_18: 5719
  population_18_64: 14468
  population_65_plus: 5016
  median_household_income: 76260
  poverty_rate: 13.4
  homeownership_rate: 72.01
  unemployment_rate: 8.06
  median_home_value: 374200
  gini_index: 0.4256
  vacancy_rate: 16.86
  race_white: 15628
  race_black: 142
  race_asian: 118
  race_native: 3439
  hispanic: 5372
  bachelors_plus: 4896
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9904
  - to: "us/states/or/districts/05"
    rel: in-district
    area_weight: 0.0096
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.7182
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.2817
  - to: "us/states/or/districts/house/59"
    rel: in-district
    area_weight: 0.7182
  - to: "us/states/or/districts/house/57"
    rel: in-district
    area_weight: 0.2817
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Jefferson County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25203 |
| Under 18 | 5719 |
| 18–64 | 14468 |
| 65+ | 5016 |
| Median household income | 76260 |
| Poverty rate | 13.4 |
| Homeownership rate | 72.01 |
| Unemployment rate | 8.06 |
| Median home value | 374200 |
| Gini index | 0.4256 |
| Vacancy rate | 16.86 |
| White | 15628 |
| Black | 142 |
| Asian | 118 |
| Native | 3439 |
| Hispanic/Latino | 5372 |
| Bachelor's or higher | 4896 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 99% (congressional)
- [OR-05](/us/states/or/districts/05.md) — 1% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 72% (state senate)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 28% (state senate)
- [OR House District 59](/us/states/or/districts/house/59.md) — 72% (state house)
- [OR House District 57](/us/states/or/districts/house/57.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
