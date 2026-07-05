---
type: Jurisdiction
title: "Vilas County, WI"
classification: county
fips: "55125"
state: "WI"
demographics:
  population: 23647
  population_under_18: 3827
  population_18_64: 12307
  population_65_plus: 7513
  median_household_income: 68431
  poverty_rate: 11.06
  homeownership_rate: 84.03
  unemployment_rate: 3.97
  median_home_value: 300000
  gini_index: 0.4358
  vacancy_rate: 55.19
  race_white: 20150
  race_black: 65
  race_asian: 91
  race_native: 2015
  hispanic: 541
  bachelors_plus: 7739
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/34"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Vilas County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23647 |
| Under 18 | 3827 |
| 18–64 | 12307 |
| 65+ | 7513 |
| Median household income | 68431 |
| Poverty rate | 11.06 |
| Homeownership rate | 84.03 |
| Unemployment rate | 3.97 |
| Median home value | 300000 |
| Gini index | 0.4358 |
| Vacancy rate | 55.19 |
| White | 20150 |
| Black | 65 |
| Asian | 91 |
| Native | 2015 |
| Hispanic/Latino | 541 |
| Bachelor's or higher | 7739 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 100% (state senate)
- [WI House District 34](/us/states/wi/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
