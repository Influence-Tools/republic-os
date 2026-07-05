---
type: Jurisdiction
title: "Lewis County, NY"
classification: county
fips: "36049"
state: "NY"
demographics:
  population: 26607
  population_under_18: 6019
  population_18_64: 15122
  population_65_plus: 5466
  median_household_income: 68182
  poverty_rate: 12.34
  homeownership_rate: 80.22
  unemployment_rate: 5.18
  median_home_value: 166100
  gini_index: 0.3987
  vacancy_rate: 28.95
  race_white: 24983
  race_black: 282
  race_asian: 89
  race_native: 8
  hispanic: 480
  bachelors_plus: 4955
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/house/117"
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

# Lewis County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26607 |
| Under 18 | 6019 |
| 18–64 | 15122 |
| 65+ | 5466 |
| Median household income | 68182 |
| Poverty rate | 12.34 |
| Homeownership rate | 80.22 |
| Unemployment rate | 5.18 |
| Median home value | 166100 |
| Gini index | 0.3987 |
| Vacancy rate | 28.95 |
| White | 24983 |
| Black | 282 |
| Asian | 89 |
| Native | 8 |
| Hispanic/Latino | 480 |
| Bachelor's or higher | 4955 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 100% (state senate)
- [NY House District 117](/us/states/ny/districts/house/117.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
