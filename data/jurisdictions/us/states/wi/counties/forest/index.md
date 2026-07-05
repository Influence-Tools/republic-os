---
type: Jurisdiction
title: "Forest County, WI"
classification: county
fips: "55041"
state: "WI"
demographics:
  population: 9369
  population_under_18: 1804
  population_18_64: 5189
  population_65_plus: 2376
  median_household_income: 61071
  poverty_rate: 15.23
  homeownership_rate: 81.98
  unemployment_rate: 2.89
  median_home_value: 185000
  gini_index: 0.4304
  vacancy_rate: 54.03
  race_white: 7314
  race_black: 39
  race_asian: 8
  race_native: 1061
  hispanic: 206
  bachelors_plus: 1402
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/house/36"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Forest County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9369 |
| Under 18 | 1804 |
| 18–64 | 5189 |
| 65+ | 2376 |
| Median household income | 61071 |
| Poverty rate | 15.23 |
| Homeownership rate | 81.98 |
| Unemployment rate | 2.89 |
| Median home value | 185000 |
| Gini index | 0.4304 |
| Vacancy rate | 54.03 |
| White | 7314 |
| Black | 39 |
| Asian | 8 |
| Native | 1061 |
| Hispanic/Latino | 206 |
| Bachelor's or higher | 1402 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 100% (state senate)
- [WI House District 36](/us/states/wi/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
