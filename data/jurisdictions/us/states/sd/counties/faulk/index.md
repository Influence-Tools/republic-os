---
type: Jurisdiction
title: "Faulk County, SD"
classification: county
fips: "46049"
state: "SD"
demographics:
  population: 2126
  population_under_18: 531
  population_18_64: 1083
  population_65_plus: 512
  median_household_income: 57750
  poverty_rate: 28.35
  homeownership_rate: 79.58
  unemployment_rate: 5.27
  median_home_value: 147500
  gini_index: 0.5029
  vacancy_rate: 20.55
  race_white: 2021
  race_black: 0
  race_asian: 5
  race_native: 5
  hispanic: 28
  bachelors_plus: 418
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/23"
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

# Faulk County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2126 |
| Under 18 | 531 |
| 18–64 | 1083 |
| 65+ | 512 |
| Median household income | 57750 |
| Poverty rate | 28.35 |
| Homeownership rate | 79.58 |
| Unemployment rate | 5.27 |
| Median home value | 147500 |
| Gini index | 0.5029 |
| Vacancy rate | 20.55 |
| White | 2021 |
| Black | 0 |
| Asian | 5 |
| Native | 5 |
| Hispanic/Latino | 28 |
| Bachelor's or higher | 418 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 23](/us/states/sd/districts/senate/23.md) — 100% (state senate)
- [SD House District 23](/us/states/sd/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
