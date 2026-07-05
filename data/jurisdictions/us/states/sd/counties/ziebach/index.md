---
type: Jurisdiction
title: "Ziebach County, SD"
classification: county
fips: "46137"
state: "SD"
demographics:
  population: 2377
  population_under_18: 657
  population_18_64: 777
  population_65_plus: 943
  median_household_income: 53958
  poverty_rate: 33.49
  homeownership_rate: 57.14
  unemployment_rate: 23.49
  median_home_value: 99600
  gini_index: 0.5235
  vacancy_rate: 16.95
  race_white: 647
  race_black: 0
  race_asian: 0
  race_native: 1659
  hispanic: 35
  bachelors_plus: 259
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/28a"
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

# Ziebach County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2377 |
| Under 18 | 657 |
| 18–64 | 777 |
| 65+ | 943 |
| Median household income | 53958 |
| Poverty rate | 33.49 |
| Homeownership rate | 57.14 |
| Unemployment rate | 23.49 |
| Median home value | 99600 |
| Gini index | 0.5235 |
| Vacancy rate | 16.95 |
| White | 647 |
| Black | 0 |
| Asian | 0 |
| Native | 1659 |
| Hispanic/Latino | 35 |
| Bachelor's or higher | 259 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 28](/us/states/sd/districts/senate/28.md) — 100% (state senate)
- [SD House District 28A](/us/states/sd/districts/house/28a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
