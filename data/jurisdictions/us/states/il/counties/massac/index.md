---
type: Jurisdiction
title: "Massac County, IL"
classification: county
fips: "17127"
state: "IL"
demographics:
  population: 13865
  population_under_18: 2955
  population_18_64: 7861
  population_65_plus: 3049
  median_household_income: 65116
  poverty_rate: 16.27
  homeownership_rate: 76.36
  unemployment_rate: 3.85
  median_home_value: 121900
  gini_index: 0.4213
  vacancy_rate: 20.01
  race_white: 11970
  race_black: 934
  race_asian: 39
  race_native: 17
  hispanic: 397
  bachelors_plus: 2159
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Massac County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13865 |
| Under 18 | 2955 |
| 18–64 | 7861 |
| 65+ | 3049 |
| Median household income | 65116 |
| Poverty rate | 16.27 |
| Homeownership rate | 76.36 |
| Unemployment rate | 3.85 |
| Median home value | 121900 |
| Gini index | 0.4213 |
| Vacancy rate | 20.01 |
| White | 11970 |
| Black | 934 |
| Asian | 39 |
| Native | 17 |
| Hispanic/Latino | 397 |
| Bachelor's or higher | 2159 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 117](/us/states/il/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
