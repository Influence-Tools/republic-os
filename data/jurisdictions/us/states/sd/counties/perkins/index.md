---
type: Jurisdiction
title: "Perkins County, SD"
classification: county
fips: "46105"
state: "SD"
demographics:
  population: 3001
  population_under_18: 722
  population_18_64: 799
  population_65_plus: 1480
  median_household_income: 66908
  poverty_rate: 13.73
  homeownership_rate: 78.38
  unemployment_rate: 4.86
  median_home_value: 114600
  gini_index: 0.5201
  vacancy_rate: 24.94
  race_white: 2787
  race_black: 0
  race_asian: 20
  race_native: 35
  hispanic: 32
  bachelors_plus: 726
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/28a"
    rel: in-district
    area_weight: 0.6729
  - to: "us/states/sd/districts/house/28b"
    rel: in-district
    area_weight: 0.327
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Perkins County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3001 |
| Under 18 | 722 |
| 18–64 | 799 |
| 65+ | 1480 |
| Median household income | 66908 |
| Poverty rate | 13.73 |
| Homeownership rate | 78.38 |
| Unemployment rate | 4.86 |
| Median home value | 114600 |
| Gini index | 0.5201 |
| Vacancy rate | 24.94 |
| White | 2787 |
| Black | 0 |
| Asian | 20 |
| Native | 35 |
| Hispanic/Latino | 32 |
| Bachelor's or higher | 726 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 28](/us/states/sd/districts/senate/28.md) — 100% (state senate)
- [SD House District 28A](/us/states/sd/districts/house/28a.md) — 67% (state house)
- [SD House District 28B](/us/states/sd/districts/house/28b.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
