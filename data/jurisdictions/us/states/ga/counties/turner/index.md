---
type: Jurisdiction
title: "Turner County, GA"
classification: county
fips: "13287"
state: "GA"
demographics:
  population: 8939
  population_under_18: 2239
  population_18_64: 4971
  population_65_plus: 1729
  median_household_income: 36799
  poverty_rate: 20.27
  homeownership_rate: 63.79
  unemployment_rate: 12.21
  median_home_value: 97300
  gini_index: 0.4847
  vacancy_rate: 16.09
  race_white: 4837
  race_black: 3258
  race_asian: 0
  race_native: 96
  hispanic: 429
  bachelors_plus: 782
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/169"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Turner County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8939 |
| Under 18 | 2239 |
| 18–64 | 4971 |
| 65+ | 1729 |
| Median household income | 36799 |
| Poverty rate | 20.27 |
| Homeownership rate | 63.79 |
| Unemployment rate | 12.21 |
| Median home value | 97300 |
| Gini index | 0.4847 |
| Vacancy rate | 16.09 |
| White | 4837 |
| Black | 3258 |
| Asian | 0 |
| Native | 96 |
| Hispanic/Latino | 429 |
| Bachelor's or higher | 782 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 169](/us/states/ga/districts/house/169.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
