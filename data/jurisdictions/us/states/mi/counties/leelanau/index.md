---
type: Jurisdiction
title: "Leelanau County, MI"
classification: county
fips: "26089"
state: "MI"
demographics:
  population: 22734
  population_under_18: 3500
  population_18_64: 11561
  population_65_plus: 7673
  median_household_income: 99422
  poverty_rate: 6.53
  homeownership_rate: 91.62
  unemployment_rate: 3.43
  median_home_value: 458400
  gini_index: 0.4688
  vacancy_rate: 38.8
  race_white: 20420
  race_black: 162
  race_asian: 106
  race_native: 596
  hispanic: 982
  bachelors_plus: 13202
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.148
  - to: "us/states/mi/districts/senate/37"
    rel: in-district
    area_weight: 0.148
  - to: "us/states/mi/districts/house/103"
    rel: in-district
    area_weight: 0.148
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Leelanau County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22734 |
| Under 18 | 3500 |
| 18–64 | 11561 |
| 65+ | 7673 |
| Median household income | 99422 |
| Poverty rate | 6.53 |
| Homeownership rate | 91.62 |
| Unemployment rate | 3.43 |
| Median home value | 458400 |
| Gini index | 0.4688 |
| Vacancy rate | 38.8 |
| White | 20420 |
| Black | 162 |
| Asian | 106 |
| Native | 596 |
| Hispanic/Latino | 982 |
| Bachelor's or higher | 13202 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 15% (congressional)
- [MI Senate District 37](/us/states/mi/districts/senate/37.md) — 15% (state senate)
- [MI House District 103](/us/states/mi/districts/house/103.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
