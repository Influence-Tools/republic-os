---
type: Jurisdiction
title: "Dewey County, SD"
classification: county
fips: "46041"
state: "SD"
demographics:
  population: 5205
  population_under_18: 1996
  population_18_64: 2691
  population_65_plus: 518
  median_household_income: 54104
  poverty_rate: 33.04
  homeownership_rate: 61.23
  unemployment_rate: 13.91
  median_home_value: 69600
  gini_index: 0.4507
  vacancy_rate: 12.38
  race_white: 1094
  race_black: 27
  race_asian: 3
  race_native: 3862
  hispanic: 54
  bachelors_plus: 680
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/house/28a"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Dewey County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5205 |
| Under 18 | 1996 |
| 18–64 | 2691 |
| 65+ | 518 |
| Median household income | 54104 |
| Poverty rate | 33.04 |
| Homeownership rate | 61.23 |
| Unemployment rate | 13.91 |
| Median home value | 69600 |
| Gini index | 0.4507 |
| Vacancy rate | 12.38 |
| White | 1094 |
| Black | 27 |
| Asian | 3 |
| Native | 3862 |
| Hispanic/Latino | 54 |
| Bachelor's or higher | 680 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 28](/us/states/sd/districts/senate/28.md) — 100% (state senate)
- [SD House District 28A](/us/states/sd/districts/house/28a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
