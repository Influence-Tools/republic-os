---
type: Jurisdiction
title: "Ripley County, MO"
classification: county
fips: "29181"
state: "MO"
demographics:
  population: 10708
  population_under_18: 2585
  population_18_64: 5989
  population_65_plus: 2134
  median_household_income: 42037
  poverty_rate: 24.79
  homeownership_rate: 79.11
  unemployment_rate: 3.7
  median_home_value: 119600
  gini_index: 0.4411
  vacancy_rate: 22.56
  race_white: 9921
  race_black: 34
  race_asian: 30
  race_native: 12
  hispanic: 157
  bachelors_plus: 1276
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Ripley County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10708 |
| Under 18 | 2585 |
| 18–64 | 5989 |
| 65+ | 2134 |
| Median household income | 42037 |
| Poverty rate | 24.79 |
| Homeownership rate | 79.11 |
| Unemployment rate | 3.7 |
| Median home value | 119600 |
| Gini index | 0.4411 |
| Vacancy rate | 22.56 |
| White | 9921 |
| Black | 34 |
| Asian | 30 |
| Native | 12 |
| Hispanic/Latino | 157 |
| Bachelor's or higher | 1276 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 25](/us/states/mo/districts/senate/25.md) — 100% (state senate)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
