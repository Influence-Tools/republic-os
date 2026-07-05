---
type: Jurisdiction
title: "Powder River County, MT"
classification: county
fips: "30075"
state: "MT"
demographics:
  population: 1815
  population_under_18: 364
  population_18_64: 906
  population_65_plus: 545
  median_household_income: 67045
  poverty_rate: 8.12
  homeownership_rate: 78.81
  unemployment_rate: 0.71
  median_home_value: 192100
  gini_index: 0.4717
  vacancy_rate: 27.16
  race_white: 1642
  race_black: 0
  race_asian: 17
  race_native: 40
  hispanic: 26
  bachelors_plus: 488
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Powder River County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1815 |
| Under 18 | 364 |
| 18–64 | 906 |
| 65+ | 545 |
| Median household income | 67045 |
| Poverty rate | 8.12 |
| Homeownership rate | 78.81 |
| Unemployment rate | 0.71 |
| Median home value | 192100 |
| Gini index | 0.4717 |
| Vacancy rate | 27.16 |
| White | 1642 |
| Black | 0 |
| Asian | 17 |
| Native | 40 |
| Hispanic/Latino | 26 |
| Bachelor's or higher | 488 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
