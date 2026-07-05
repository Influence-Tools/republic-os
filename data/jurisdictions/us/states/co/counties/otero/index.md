---
type: Jurisdiction
title: "Otero County, CO"
classification: county
fips: "08089"
state: "CO"
demographics:
  population: 18321
  population_under_18: 4232
  population_18_64: 10195
  population_65_plus: 3894
  median_household_income: 54037
  poverty_rate: 22.09
  homeownership_rate: 68.95
  unemployment_rate: 6.73
  median_home_value: 168900
  gini_index: 0.424
  vacancy_rate: 13.29
  race_white: 12315
  race_black: 213
  race_asian: 137
  race_native: 390
  hispanic: 7695
  bachelors_plus: 3158
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Otero County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18321 |
| Under 18 | 4232 |
| 18–64 | 10195 |
| 65+ | 3894 |
| Median household income | 54037 |
| Poverty rate | 22.09 |
| Homeownership rate | 68.95 |
| Unemployment rate | 6.73 |
| Median home value | 168900 |
| Gini index | 0.424 |
| Vacancy rate | 13.29 |
| White | 12315 |
| Black | 213 |
| Asian | 137 |
| Native | 390 |
| Hispanic/Latino | 7695 |
| Bachelor's or higher | 3158 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
