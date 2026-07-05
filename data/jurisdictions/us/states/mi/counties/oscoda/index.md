---
type: Jurisdiction
title: "Oscoda County, MI"
classification: county
fips: "26135"
state: "MI"
demographics:
  population: 8425
  population_under_18: 1654
  population_18_64: 4297
  population_65_plus: 2474
  median_household_income: 49515
  poverty_rate: 17.21
  homeownership_rate: 87.25
  unemployment_rate: 8.05
  median_home_value: 125500
  gini_index: 0.4183
  vacancy_rate: 50.93
  race_white: 7906
  race_black: 36
  race_asian: 38
  race_native: 32
  hispanic: 177
  bachelors_plus: 1267
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/house/106"
    rel: in-district
    area_weight: 0.5009
  - to: "us/states/mi/districts/house/105"
    rel: in-district
    area_weight: 0.4989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Oscoda County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8425 |
| Under 18 | 1654 |
| 18–64 | 4297 |
| 65+ | 2474 |
| Median household income | 49515 |
| Poverty rate | 17.21 |
| Homeownership rate | 87.25 |
| Unemployment rate | 8.05 |
| Median home value | 125500 |
| Gini index | 0.4183 |
| Vacancy rate | 50.93 |
| White | 7906 |
| Black | 36 |
| Asian | 38 |
| Native | 32 |
| Hispanic/Latino | 177 |
| Bachelor's or higher | 1267 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 100% (congressional)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 100% (state senate)
- [MI House District 106](/us/states/mi/districts/house/106.md) — 50% (state house)
- [MI House District 105](/us/states/mi/districts/house/105.md) — 50% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
