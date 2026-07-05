---
type: Jurisdiction
title: "Oneida County, WI"
classification: county
fips: "55085"
state: "WI"
demographics:
  population: 38167
  population_under_18: 6376
  population_18_64: 20991
  population_65_plus: 10800
  median_household_income: 69371
  poverty_rate: 8.55
  homeownership_rate: 82.3
  unemployment_rate: 1.96
  median_home_value: 238400
  gini_index: 0.4464
  vacancy_rate: 43.23
  race_white: 35797
  race_black: 196
  race_asian: 178
  race_native: 302
  hispanic: 654
  bachelors_plus: 11614
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/34"
    rel: in-district
    area_weight: 0.97
  - to: "us/states/wi/districts/house/35"
    rel: in-district
    area_weight: 0.0299
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Oneida County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38167 |
| Under 18 | 6376 |
| 18–64 | 20991 |
| 65+ | 10800 |
| Median household income | 69371 |
| Poverty rate | 8.55 |
| Homeownership rate | 82.3 |
| Unemployment rate | 1.96 |
| Median home value | 238400 |
| Gini index | 0.4464 |
| Vacancy rate | 43.23 |
| White | 35797 |
| Black | 196 |
| Asian | 178 |
| Native | 302 |
| Hispanic/Latino | 654 |
| Bachelor's or higher | 11614 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 100% (state senate)
- [WI House District 34](/us/states/wi/districts/house/34.md) — 97% (state house)
- [WI House District 35](/us/states/wi/districts/house/35.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
