---
type: Jurisdiction
title: "Prairie County, MT"
classification: county
fips: "30079"
state: "MT"
demographics:
  population: 1250
  population_under_18: 212
  population_18_64: 511
  population_65_plus: 527
  median_household_income: 51250
  poverty_rate: 20.61
  homeownership_rate: 83.85
  unemployment_rate: 0.92
  median_home_value: 165700
  gini_index: 0.5137
  vacancy_rate: 20.67
  race_white: 1108
  race_black: 0
  race_asian: 34
  race_native: 1
  hispanic: 7
  bachelors_plus: 385
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/house/34"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Prairie County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1250 |
| Under 18 | 212 |
| 18–64 | 511 |
| 65+ | 527 |
| Median household income | 51250 |
| Poverty rate | 20.61 |
| Homeownership rate | 83.85 |
| Unemployment rate | 0.92 |
| Median home value | 165700 |
| Gini index | 0.5137 |
| Vacancy rate | 20.67 |
| White | 1108 |
| Black | 0 |
| Asian | 34 |
| Native | 1 |
| Hispanic/Latino | 7 |
| Bachelor's or higher | 385 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 100% (state senate)
- [MT House District 34](/us/states/mt/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
