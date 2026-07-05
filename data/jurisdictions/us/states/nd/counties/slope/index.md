---
type: Jurisdiction
title: "Slope County, ND"
classification: county
fips: "38087"
state: "ND"
demographics:
  population: 766
  population_under_18: 122
  population_18_64: 424
  population_65_plus: 220
  median_household_income: 71250
  poverty_rate: 4.96
  homeownership_rate: 80.75
  unemployment_rate: 2.68
  median_home_value: 170000
  gini_index: 0.4674
  vacancy_rate: 17.98
  race_white: 708
  race_black: 0
  race_asian: 0
  race_native: 0
  hispanic: 1
  bachelors_plus: 201
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/39"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/39"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Slope County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 766 |
| Under 18 | 122 |
| 18–64 | 424 |
| 65+ | 220 |
| Median household income | 71250 |
| Poverty rate | 4.96 |
| Homeownership rate | 80.75 |
| Unemployment rate | 2.68 |
| Median home value | 170000 |
| Gini index | 0.4674 |
| Vacancy rate | 17.98 |
| White | 708 |
| Black | 0 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 1 |
| Bachelor's or higher | 201 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 39](/us/states/nd/districts/senate/39.md) — 100% (state senate)
- [ND House District 39](/us/states/nd/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
