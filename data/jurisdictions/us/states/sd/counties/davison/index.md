---
type: Jurisdiction
title: "Davison County, SD"
classification: county
fips: "46035"
state: "SD"
demographics:
  population: 19952
  population_under_18: 4708
  population_18_64: 11088
  population_65_plus: 4156
  median_household_income: 66208
  poverty_rate: 11.17
  homeownership_rate: 61.47
  unemployment_rate: 0.86
  median_home_value: 205800
  gini_index: 0.4416
  vacancy_rate: 7.1
  race_white: 17917
  race_black: 133
  race_asian: 99
  race_native: 824
  hispanic: 1017
  bachelors_plus: 3832
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/20"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Davison County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19952 |
| Under 18 | 4708 |
| 18–64 | 11088 |
| 65+ | 4156 |
| Median household income | 66208 |
| Poverty rate | 11.17 |
| Homeownership rate | 61.47 |
| Unemployment rate | 0.86 |
| Median home value | 205800 |
| Gini index | 0.4416 |
| Vacancy rate | 7.1 |
| White | 17917 |
| Black | 133 |
| Asian | 99 |
| Native | 824 |
| Hispanic/Latino | 1017 |
| Bachelor's or higher | 3832 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 20](/us/states/sd/districts/senate/20.md) — 100% (state senate)
- [SD House District 20](/us/states/sd/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
