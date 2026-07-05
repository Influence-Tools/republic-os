---
type: Jurisdiction
title: "Allegany County, NY"
classification: county
fips: "36003"
state: "NY"
demographics:
  population: 47159
  population_under_18: 9242
  population_18_64: 28461
  population_65_plus: 9456
  median_household_income: 62869
  poverty_rate: 16.18
  homeownership_rate: 79.27
  unemployment_rate: 7.11
  median_home_value: 101700
  gini_index: 0.4263
  vacancy_rate: 24.77
  race_white: 44015
  race_black: 776
  race_asian: 653
  race_native: 84
  hispanic: 1037
  bachelors_plus: 10942
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ny/districts/senate/57"
    rel: in-district
    area_weight: 0.5935
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.4062
  - to: "us/states/ny/districts/house/148"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Allegany County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47159 |
| Under 18 | 9242 |
| 18–64 | 28461 |
| 65+ | 9456 |
| Median household income | 62869 |
| Poverty rate | 16.18 |
| Homeownership rate | 79.27 |
| Unemployment rate | 7.11 |
| Median home value | 101700 |
| Gini index | 0.4263 |
| Vacancy rate | 24.77 |
| White | 44015 |
| Black | 776 |
| Asian | 653 |
| Native | 84 |
| Hispanic/Latino | 1037 |
| Bachelor's or higher | 10942 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 100% (congressional)
- [NY Senate District 57](/us/states/ny/districts/senate/57.md) — 59% (state senate)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 41% (state senate)
- [NY House District 148](/us/states/ny/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
