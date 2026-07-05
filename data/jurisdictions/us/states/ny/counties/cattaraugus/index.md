---
type: Jurisdiction
title: "Cattaraugus County, NY"
classification: county
fips: "36009"
state: "NY"
demographics:
  population: 76145
  population_under_18: 16645
  population_18_64: 43657
  population_65_plus: 15843
  median_household_income: 59540
  poverty_rate: 19.1
  homeownership_rate: 75.23
  unemployment_rate: 4.98
  median_home_value: 113100
  gini_index: 0.4407
  vacancy_rate: 20.97
  race_white: 67496
  race_black: 1138
  race_asian: 665
  race_native: 1866
  hispanic: 1817
  bachelors_plus: 16305
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/senate/57"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/148"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Cattaraugus County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 76145 |
| Under 18 | 16645 |
| 18–64 | 43657 |
| 65+ | 15843 |
| Median household income | 59540 |
| Poverty rate | 19.1 |
| Homeownership rate | 75.23 |
| Unemployment rate | 4.98 |
| Median home value | 113100 |
| Gini index | 0.4407 |
| Vacancy rate | 20.97 |
| White | 67496 |
| Black | 1138 |
| Asian | 665 |
| Native | 1866 |
| Hispanic/Latino | 1817 |
| Bachelor's or higher | 16305 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 100% (congressional)
- [NY Senate District 57](/us/states/ny/districts/senate/57.md) — 100% (state senate)
- [NY House District 148](/us/states/ny/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
