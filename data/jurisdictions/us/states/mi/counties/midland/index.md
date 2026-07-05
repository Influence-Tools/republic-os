---
type: Jurisdiction
title: "Midland County, MI"
classification: county
fips: "26111"
state: "MI"
demographics:
  population: 83757
  population_under_18: 17545
  population_18_64: 49289
  population_65_plus: 16923
  median_household_income: 77705
  poverty_rate: 10.74
  homeownership_rate: 78.08
  unemployment_rate: 4.37
  median_home_value: 195400
  gini_index: 0.4624
  vacancy_rate: 5.83
  race_white: 75567
  race_black: 1022
  race_asian: 1804
  race_native: 159
  hispanic: 2882
  bachelors_plus: 30699
districts:
  - to: "us/states/mi/districts/08"
    rel: in-district
    area_weight: 0.6582
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.3418
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.6575
  - to: "us/states/mi/districts/senate/35"
    rel: in-district
    area_weight: 0.3425
  - to: "us/states/mi/districts/house/95"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Midland County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83757 |
| Under 18 | 17545 |
| 18–64 | 49289 |
| 65+ | 16923 |
| Median household income | 77705 |
| Poverty rate | 10.74 |
| Homeownership rate | 78.08 |
| Unemployment rate | 4.37 |
| Median home value | 195400 |
| Gini index | 0.4624 |
| Vacancy rate | 5.83 |
| White | 75567 |
| Black | 1022 |
| Asian | 1804 |
| Native | 159 |
| Hispanic/Latino | 2882 |
| Bachelor's or higher | 30699 |

## Districts

- [MI-08](/us/states/mi/districts/08.md) — 66% (congressional)
- [MI-02](/us/states/mi/districts/02.md) — 34% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 66% (state senate)
- [MI Senate District 35](/us/states/mi/districts/senate/35.md) — 34% (state senate)
- [MI House District 95](/us/states/mi/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
