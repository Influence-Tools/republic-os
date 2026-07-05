---
type: Jurisdiction
title: "Traill County, ND"
classification: county
fips: "38097"
state: "ND"
demographics:
  population: 7970
  population_under_18: 1821
  population_18_64: 4532
  population_65_plus: 1617
  median_household_income: 87004
  poverty_rate: 9.06
  homeownership_rate: 74.35
  unemployment_rate: 2.23
  median_home_value: 200700
  gini_index: 0.4386
  vacancy_rate: 9.03
  race_white: 7208
  race_black: 77
  race_asian: 45
  race_native: 63
  hispanic: 315
  bachelors_plus: 2126
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/nd/districts/senate/20"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nd/districts/house/20"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Traill County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7970 |
| Under 18 | 1821 |
| 18–64 | 4532 |
| 65+ | 1617 |
| Median household income | 87004 |
| Poverty rate | 9.06 |
| Homeownership rate | 74.35 |
| Unemployment rate | 2.23 |
| Median home value | 200700 |
| Gini index | 0.4386 |
| Vacancy rate | 9.03 |
| White | 7208 |
| Black | 77 |
| Asian | 45 |
| Native | 63 |
| Hispanic/Latino | 315 |
| Bachelor's or higher | 2126 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 20](/us/states/nd/districts/senate/20.md) — 100% (state senate)
- [ND House District 20](/us/states/nd/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
