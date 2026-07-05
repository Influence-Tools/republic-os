---
type: Jurisdiction
title: "Wilkinson County, GA"
classification: county
fips: "13319"
state: "GA"
demographics:
  population: 8747
  population_under_18: 1915
  population_18_64: 5034
  population_65_plus: 1798
  median_household_income: 45465
  poverty_rate: 21.6
  homeownership_rate: 80.51
  unemployment_rate: 4.81
  median_home_value: 86300
  gini_index: 0.4603
  vacancy_rate: 19.31
  race_white: 4908
  race_black: 3298
  race_asian: 47
  race_native: 1
  hispanic: 290
  bachelors_plus: 1017
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ga/districts/senate/26"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/133"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Wilkinson County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8747 |
| Under 18 | 1915 |
| 18–64 | 5034 |
| 65+ | 1798 |
| Median household income | 45465 |
| Poverty rate | 21.6 |
| Homeownership rate | 80.51 |
| Unemployment rate | 4.81 |
| Median home value | 86300 |
| Gini index | 0.4603 |
| Vacancy rate | 19.31 |
| White | 4908 |
| Black | 3298 |
| Asian | 47 |
| Native | 1 |
| Hispanic/Latino | 290 |
| Bachelor's or higher | 1017 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 26](/us/states/ga/districts/senate/26.md) — 100% (state senate)
- [GA House District 133](/us/states/ga/districts/house/133.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
