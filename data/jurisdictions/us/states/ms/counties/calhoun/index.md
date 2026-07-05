---
type: Jurisdiction
title: "Calhoun County, MS"
classification: county
fips: "28013"
state: "MS"
demographics:
  population: 12922
  population_under_18: 2859
  population_18_64: 7375
  population_65_plus: 2688
  median_household_income: 43125
  poverty_rate: 20.41
  homeownership_rate: 71.98
  unemployment_rate: 4.69
  median_home_value: 90300
  gini_index: 0.4597
  vacancy_rate: 16.87
  race_white: 8230
  race_black: 3439
  race_asian: 11
  race_native: 0
  hispanic: 814
  bachelors_plus: 1471
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ms/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ms/districts/house/23"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Calhoun County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12922 |
| Under 18 | 2859 |
| 18–64 | 7375 |
| 65+ | 2688 |
| Median household income | 43125 |
| Poverty rate | 20.41 |
| Homeownership rate | 71.98 |
| Unemployment rate | 4.69 |
| Median home value | 90300 |
| Gini index | 0.4597 |
| Vacancy rate | 16.87 |
| White | 8230 |
| Black | 3439 |
| Asian | 11 |
| Native | 0 |
| Hispanic/Latino | 814 |
| Bachelor's or higher | 1471 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 8](/us/states/ms/districts/senate/8.md) — 100% (state senate)
- [MS House District 23](/us/states/ms/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
