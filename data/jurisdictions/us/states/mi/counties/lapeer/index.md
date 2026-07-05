---
type: Jurisdiction
title: "Lapeer County, MI"
classification: county
fips: "26087"
state: "MI"
demographics:
  population: 88837
  population_under_18: 17667
  population_18_64: 53254
  population_65_plus: 17916
  median_household_income: 77306
  poverty_rate: 9.71
  homeownership_rate: 86.04
  unemployment_rate: 5.06
  median_home_value: 239000
  gini_index: 0.4218
  vacancy_rate: 6.22
  race_white: 80733
  race_black: 920
  race_asian: 259
  race_native: 330
  hispanic: 4476
  bachelors_plus: 17419
districts:
  - to: "us/states/mi/districts/09"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/senate/26"
    rel: in-district
    area_weight: 0.7824
  - to: "us/states/mi/districts/senate/24"
    rel: in-district
    area_weight: 0.2174
  - to: "us/states/mi/districts/house/67"
    rel: in-district
    area_weight: 0.4283
  - to: "us/states/mi/districts/house/65"
    rel: in-district
    area_weight: 0.4094
  - to: "us/states/mi/districts/house/98"
    rel: in-district
    area_weight: 0.1623
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Lapeer County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 88837 |
| Under 18 | 17667 |
| 18–64 | 53254 |
| 65+ | 17916 |
| Median household income | 77306 |
| Poverty rate | 9.71 |
| Homeownership rate | 86.04 |
| Unemployment rate | 5.06 |
| Median home value | 239000 |
| Gini index | 0.4218 |
| Vacancy rate | 6.22 |
| White | 80733 |
| Black | 920 |
| Asian | 259 |
| Native | 330 |
| Hispanic/Latino | 4476 |
| Bachelor's or higher | 17419 |

## Districts

- [MI-09](/us/states/mi/districts/09.md) — 100% (congressional)
- [MI Senate District 26](/us/states/mi/districts/senate/26.md) — 78% (state senate)
- [MI Senate District 24](/us/states/mi/districts/senate/24.md) — 22% (state senate)
- [MI House District 67](/us/states/mi/districts/house/67.md) — 43% (state house)
- [MI House District 65](/us/states/mi/districts/house/65.md) — 41% (state house)
- [MI House District 98](/us/states/mi/districts/house/98.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
