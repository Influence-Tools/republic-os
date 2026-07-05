---
type: Jurisdiction
title: "Sanborn County, SD"
classification: county
fips: "46111"
state: "SD"
demographics:
  population: 2384
  population_under_18: 670
  population_18_64: 682
  population_65_plus: 1032
  median_household_income: 78750
  poverty_rate: 8.54
  homeownership_rate: 78.65
  unemployment_rate: 0.57
  median_home_value: 135600
  gini_index: 0.3992
  vacancy_rate: 19.01
  race_white: 2214
  race_black: 0
  race_asian: 0
  race_native: 56
  hispanic: 123
  bachelors_plus: 449
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

# Sanborn County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2384 |
| Under 18 | 670 |
| 18–64 | 682 |
| 65+ | 1032 |
| Median household income | 78750 |
| Poverty rate | 8.54 |
| Homeownership rate | 78.65 |
| Unemployment rate | 0.57 |
| Median home value | 135600 |
| Gini index | 0.3992 |
| Vacancy rate | 19.01 |
| White | 2214 |
| Black | 0 |
| Asian | 0 |
| Native | 56 |
| Hispanic/Latino | 123 |
| Bachelor's or higher | 449 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 20](/us/states/sd/districts/senate/20.md) — 100% (state senate)
- [SD House District 20](/us/states/sd/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
