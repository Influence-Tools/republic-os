---
type: Jurisdiction
title: "Donley County, TX"
classification: county
fips: "48129"
state: "TX"
demographics:
  population: 3257
  population_under_18: 573
  population_18_64: 1866
  population_65_plus: 818
  median_household_income: 58750
  poverty_rate: 7.87
  homeownership_rate: 74.83
  unemployment_rate: 1.68
  median_home_value: 96400
  gini_index: 0.4252
  vacancy_rate: 39.52
  race_white: 2742
  race_black: 168
  race_asian: 83
  race_native: 6
  hispanic: 410
  bachelors_plus: 486
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Donley County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3257 |
| Under 18 | 573 |
| 18–64 | 1866 |
| 65+ | 818 |
| Median household income | 58750 |
| Poverty rate | 7.87 |
| Homeownership rate | 74.83 |
| Unemployment rate | 1.68 |
| Median home value | 96400 |
| Gini index | 0.4252 |
| Vacancy rate | 39.52 |
| White | 2742 |
| Black | 168 |
| Asian | 83 |
| Native | 6 |
| Hispanic/Latino | 410 |
| Bachelor's or higher | 486 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
