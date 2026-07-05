---
type: Jurisdiction
title: "Swift County, MN"
classification: county
fips: "27151"
state: "MN"
demographics:
  population: 9748
  population_under_18: 2197
  population_18_64: 5263
  population_65_plus: 2288
  median_household_income: 60412
  poverty_rate: 12.03
  homeownership_rate: 72.39
  unemployment_rate: 4.43
  median_home_value: 161400
  gini_index: 0.438
  vacancy_rate: 12.43
  race_white: 8621
  race_black: 69
  race_asian: 0
  race_native: 212
  hispanic: 701
  bachelors_plus: 1958
districts:
  - to: "us/states/mn/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mn/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mn/districts/house/12a"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Swift County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9748 |
| Under 18 | 2197 |
| 18–64 | 5263 |
| 65+ | 2288 |
| Median household income | 60412 |
| Poverty rate | 12.03 |
| Homeownership rate | 72.39 |
| Unemployment rate | 4.43 |
| Median home value | 161400 |
| Gini index | 0.438 |
| Vacancy rate | 12.43 |
| White | 8621 |
| Black | 69 |
| Asian | 0 |
| Native | 212 |
| Hispanic/Latino | 701 |
| Bachelor's or higher | 1958 |

## Districts

- [MN-07](/us/states/mn/districts/07.md) — 100% (congressional)
- [MN Senate District 12](/us/states/mn/districts/senate/12.md) — 100% (state senate)
- [MN House District 12A](/us/states/mn/districts/house/12a.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
