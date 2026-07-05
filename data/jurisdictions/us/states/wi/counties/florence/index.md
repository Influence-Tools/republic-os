---
type: Jurisdiction
title: "Florence County, WI"
classification: county
fips: "55037"
state: "WI"
demographics:
  population: 4646
  population_under_18: 721
  population_18_64: 2564
  population_65_plus: 1361
  median_household_income: 61086
  poverty_rate: 7.3
  homeownership_rate: 90.85
  unemployment_rate: 4.79
  median_home_value: 173200
  gini_index: 0.4228
  vacancy_rate: 52.63
  race_white: 4411
  race_black: 12
  race_asian: 0
  race_native: 74
  hispanic: 21
  bachelors_plus: 1160
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9961
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wi/districts/house/36"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Florence County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4646 |
| Under 18 | 721 |
| 18–64 | 2564 |
| 65+ | 1361 |
| Median household income | 61086 |
| Poverty rate | 7.3 |
| Homeownership rate | 90.85 |
| Unemployment rate | 4.79 |
| Median home value | 173200 |
| Gini index | 0.4228 |
| Vacancy rate | 52.63 |
| White | 4411 |
| Black | 12 |
| Asian | 0 |
| Native | 74 |
| Hispanic/Latino | 21 |
| Bachelor's or higher | 1160 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 100% (state senate)
- [WI House District 36](/us/states/wi/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
