---
type: Jurisdiction
title: "Pepin County, WI"
classification: county
fips: "55091"
state: "WI"
demographics:
  population: 7431
  population_under_18: 1660
  population_18_64: 3949
  population_65_plus: 1822
  median_household_income: 75256
  poverty_rate: 10.21
  homeownership_rate: 82.96
  unemployment_rate: 3.11
  median_home_value: 214800
  gini_index: 0.4133
  vacancy_rate: 15.53
  race_white: 7046
  race_black: 31
  race_asian: 48
  race_native: 11
  hispanic: 198
  bachelors_plus: 1566
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/house/29"
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

# Pepin County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7431 |
| Under 18 | 1660 |
| 18–64 | 3949 |
| 65+ | 1822 |
| Median household income | 75256 |
| Poverty rate | 10.21 |
| Homeownership rate | 82.96 |
| Unemployment rate | 3.11 |
| Median home value | 214800 |
| Gini index | 0.4133 |
| Vacancy rate | 15.53 |
| White | 7046 |
| Black | 31 |
| Asian | 48 |
| Native | 11 |
| Hispanic/Latino | 198 |
| Bachelor's or higher | 1566 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 100% (state senate)
- [WI House District 29](/us/states/wi/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
