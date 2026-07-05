---
type: Jurisdiction
title: "Fulton County, PA"
classification: county
fips: "42057"
state: "PA"
demographics:
  population: 14531
  population_under_18: 2865
  population_18_64: 8351
  population_65_plus: 3315
  median_household_income: 65836
  poverty_rate: 11.18
  homeownership_rate: 77.61
  unemployment_rate: 2.91
  median_home_value: 208500
  gini_index: 0.4375
  vacancy_rate: 11.43
  race_white: 13601
  race_black: 187
  race_asian: 33
  race_native: 6
  hispanic: 188
  bachelors_plus: 2593
districts:
  - to: "us/states/pa/districts/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/pa/districts/house/78"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Fulton County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14531 |
| Under 18 | 2865 |
| 18–64 | 8351 |
| 65+ | 3315 |
| Median household income | 65836 |
| Poverty rate | 11.18 |
| Homeownership rate | 77.61 |
| Unemployment rate | 2.91 |
| Median home value | 208500 |
| Gini index | 0.4375 |
| Vacancy rate | 11.43 |
| White | 13601 |
| Black | 187 |
| Asian | 33 |
| Native | 6 |
| Hispanic/Latino | 188 |
| Bachelor's or higher | 2593 |

## Districts

- [PA-13](/us/states/pa/districts/13.md) — 100% (congressional)
- [PA Senate District 30](/us/states/pa/districts/senate/30.md) — 100% (state senate)
- [PA House District 78](/us/states/pa/districts/house/78.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
