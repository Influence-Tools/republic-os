---
type: Jurisdiction
title: "LaMoure County, ND"
classification: county
fips: "38045"
state: "ND"
demographics:
  population: 4118
  population_under_18: 944
  population_18_64: 2072
  population_65_plus: 1102
  median_household_income: 80664
  poverty_rate: 8.7
  homeownership_rate: 83.55
  unemployment_rate: 2.45
  median_home_value: 117200
  gini_index: 0.429
  vacancy_rate: 15.54
  race_white: 3952
  race_black: 6
  race_asian: 5
  race_native: 20
  hispanic: 79
  bachelors_plus: 890
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/28"
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

# LaMoure County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4118 |
| Under 18 | 944 |
| 18–64 | 2072 |
| 65+ | 1102 |
| Median household income | 80664 |
| Poverty rate | 8.7 |
| Homeownership rate | 83.55 |
| Unemployment rate | 2.45 |
| Median home value | 117200 |
| Gini index | 0.429 |
| Vacancy rate | 15.54 |
| White | 3952 |
| Black | 6 |
| Asian | 5 |
| Native | 20 |
| Hispanic/Latino | 79 |
| Bachelor's or higher | 890 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 28](/us/states/nd/districts/senate/28.md) — 100% (state senate)
- [ND House District 28](/us/states/nd/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
