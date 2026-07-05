---
type: Jurisdiction
title: "Tehama County, CA"
classification: county
fips: "06103"
state: "CA"
demographics:
  population: 65167
  population_under_18: 15696
  population_18_64: 36386
  population_65_plus: 13085
  median_household_income: 63784
  poverty_rate: 15.56
  homeownership_rate: 67.13
  unemployment_rate: 5.85
  median_home_value: 339600
  gini_index: 0.5001
  vacancy_rate: 9.95
  race_white: 43477
  race_black: 558
  race_asian: 1275
  race_native: 1285
  hispanic: 18941
  bachelors_plus: 10965
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Tehama County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65167 |
| Under 18 | 15696 |
| 18–64 | 36386 |
| 65+ | 13085 |
| Median household income | 63784 |
| Poverty rate | 15.56 |
| Homeownership rate | 67.13 |
| Unemployment rate | 5.85 |
| Median home value | 339600 |
| Gini index | 0.5001 |
| Vacancy rate | 9.95 |
| White | 43477 |
| Black | 558 |
| Asian | 1275 |
| Native | 1285 |
| Hispanic/Latino | 18941 |
| Bachelor's or higher | 10965 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
