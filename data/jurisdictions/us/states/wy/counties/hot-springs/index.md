---
type: Jurisdiction
title: "Hot Springs County, WY"
classification: county
fips: "56017"
state: "WY"
demographics:
  population: 4620
  population_under_18: 1042
  population_18_64: 2367
  population_65_plus: 1211
  median_household_income: 61250
  poverty_rate: 14.73
  homeownership_rate: 72.66
  unemployment_rate: 2.95
  median_home_value: 227500
  gini_index: 0.4196
  vacancy_rate: 13.04
  race_white: 4205
  race_black: 0
  race_asian: 14
  race_native: 25
  hispanic: 183
  bachelors_plus: 1194
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/house/28"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Hot Springs County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4620 |
| Under 18 | 1042 |
| 18–64 | 2367 |
| 65+ | 1211 |
| Median household income | 61250 |
| Poverty rate | 14.73 |
| Homeownership rate | 72.66 |
| Unemployment rate | 2.95 |
| Median home value | 227500 |
| Gini index | 0.4196 |
| Vacancy rate | 13.04 |
| White | 4205 |
| Black | 0 |
| Asian | 14 |
| Native | 25 |
| Hispanic/Latino | 183 |
| Bachelor's or higher | 1194 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 20](/us/states/wy/districts/senate/20.md) — 100% (state senate)
- [WY House District 28](/us/states/wy/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
