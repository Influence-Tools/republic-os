---
type: Jurisdiction
title: "Glascock County, GA"
classification: county
fips: "13125"
state: "GA"
demographics:
  population: 2932
  population_under_18: 659
  population_18_64: 1731
  population_65_plus: 542
  median_household_income: 54934
  poverty_rate: 12.56
  homeownership_rate: 67.57
  unemployment_rate: 1.57
  median_home_value: 123800
  gini_index: 0.3826
  vacancy_rate: 26.52
  race_white: 2537
  race_black: 211
  race_asian: 0
  race_native: 0
  hispanic: 93
  bachelors_plus: 452
districts:
  - to: "us/states/ga/districts/12"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/23"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/128"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Glascock County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2932 |
| Under 18 | 659 |
| 18–64 | 1731 |
| 65+ | 542 |
| Median household income | 54934 |
| Poverty rate | 12.56 |
| Homeownership rate | 67.57 |
| Unemployment rate | 1.57 |
| Median home value | 123800 |
| Gini index | 0.3826 |
| Vacancy rate | 26.52 |
| White | 2537 |
| Black | 211 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 93 |
| Bachelor's or higher | 452 |

## Districts

- [GA-12](/us/states/ga/districts/12.md) — 100% (congressional)
- [GA Senate District 23](/us/states/ga/districts/senate/23.md) — 100% (state senate)
- [GA House District 128](/us/states/ga/districts/house/128.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
