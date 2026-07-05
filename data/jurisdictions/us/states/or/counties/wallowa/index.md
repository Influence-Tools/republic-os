---
type: Jurisdiction
title: "Wallowa County, OR"
classification: county
fips: "41063"
state: "OR"
demographics:
  population: 7553
  population_under_18: 1517
  population_18_64: 3817
  population_65_plus: 2219
  median_household_income: 67112
  poverty_rate: 7.8
  homeownership_rate: 72.45
  unemployment_rate: 3.83
  median_home_value: 394800
  gini_index: 0.4265
  vacancy_rate: 22.12
  race_white: 6793
  race_black: 99
  race_asian: 22
  race_native: 11
  hispanic: 315
  bachelors_plus: 2994
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/58"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Wallowa County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7553 |
| Under 18 | 1517 |
| 18–64 | 3817 |
| 65+ | 2219 |
| Median household income | 67112 |
| Poverty rate | 7.8 |
| Homeownership rate | 72.45 |
| Unemployment rate | 3.83 |
| Median home value | 394800 |
| Gini index | 0.4265 |
| Vacancy rate | 22.12 |
| White | 6793 |
| Black | 99 |
| Asian | 22 |
| Native | 11 |
| Hispanic/Latino | 315 |
| Bachelor's or higher | 2994 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 58](/us/states/or/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
