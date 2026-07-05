---
type: Jurisdiction
title: "Clark County, WI"
classification: county
fips: "55019"
state: "WI"
demographics:
  population: 34739
  population_under_18: 10305
  population_18_64: 18450
  population_65_plus: 5984
  median_household_income: 67400
  poverty_rate: 12.07
  homeownership_rate: 78.53
  unemployment_rate: 3.73
  median_home_value: 172800
  gini_index: 0.4261
  vacancy_rate: 14.18
  race_white: 31688
  race_black: 299
  race_asian: 136
  race_native: 69
  hispanic: 2232
  bachelors_plus: 3609
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/69"
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

# Clark County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 34739 |
| Under 18 | 10305 |
| 18–64 | 18450 |
| 65+ | 5984 |
| Median household income | 67400 |
| Poverty rate | 12.07 |
| Homeownership rate | 78.53 |
| Unemployment rate | 3.73 |
| Median home value | 172800 |
| Gini index | 0.4261 |
| Vacancy rate | 14.18 |
| White | 31688 |
| Black | 299 |
| Asian | 136 |
| Native | 69 |
| Hispanic/Latino | 2232 |
| Bachelor's or higher | 3609 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 100% (state senate)
- [WI House District 69](/us/states/wi/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
