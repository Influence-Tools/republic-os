---
type: Jurisdiction
title: "Hamilton County, NY"
classification: county
fips: "36041"
state: "NY"
demographics:
  population: 5089
  population_under_18: 615
  population_18_64: 2756
  population_65_plus: 1718
  median_household_income: 68835
  poverty_rate: 10.58
  homeownership_rate: 82.42
  unemployment_rate: 4.45
  median_home_value: 260200
  gini_index: 0.4303
  vacancy_rate: 69.37
  race_white: 4664
  race_black: 81
  race_asian: 17
  race_native: 1
  hispanic: 106
  bachelors_plus: 2054
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/118"
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

# Hamilton County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5089 |
| Under 18 | 615 |
| 18–64 | 2756 |
| 65+ | 1718 |
| Median household income | 68835 |
| Poverty rate | 10.58 |
| Homeownership rate | 82.42 |
| Unemployment rate | 4.45 |
| Median home value | 260200 |
| Gini index | 0.4303 |
| Vacancy rate | 69.37 |
| White | 4664 |
| Black | 81 |
| Asian | 17 |
| Native | 1 |
| Hispanic/Latino | 106 |
| Bachelor's or higher | 2054 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 100% (state senate)
- [NY House District 118](/us/states/ny/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
