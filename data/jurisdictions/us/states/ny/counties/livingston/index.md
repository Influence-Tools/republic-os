---
type: Jurisdiction
title: "Livingston County, NY"
classification: county
fips: "36051"
state: "NY"
demographics:
  population: 61498
  population_under_18: 10966
  population_18_64: 38148
  population_65_plus: 12384
  median_household_income: 74001
  poverty_rate: 11.09
  homeownership_rate: 76.35
  unemployment_rate: 5.16
  median_home_value: 174600
  gini_index: 0.4236
  vacancy_rate: 10.45
  race_white: 54973
  race_black: 1223
  race_asian: 732
  race_native: 42
  hispanic: 2857
  bachelors_plus: 18558
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/senate/54"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/133"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Livingston County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61498 |
| Under 18 | 10966 |
| 18–64 | 38148 |
| 65+ | 12384 |
| Median household income | 74001 |
| Poverty rate | 11.09 |
| Homeownership rate | 76.35 |
| Unemployment rate | 5.16 |
| Median home value | 174600 |
| Gini index | 0.4236 |
| Vacancy rate | 10.45 |
| White | 54973 |
| Black | 1223 |
| Asian | 732 |
| Native | 42 |
| Hispanic/Latino | 2857 |
| Bachelor's or higher | 18558 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 100% (congressional)
- [NY Senate District 54](/us/states/ny/districts/senate/54.md) — 100% (state senate)
- [NY House District 133](/us/states/ny/districts/house/133.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
