---
type: Jurisdiction
title: "Oswego County, NY"
classification: county
fips: "36075"
state: "NY"
demographics:
  population: 117953
  population_under_18: 24276
  population_18_64: 72494
  population_65_plus: 21183
  median_household_income: 69183
  poverty_rate: 16.32
  homeownership_rate: 73.41
  unemployment_rate: 7.01
  median_home_value: 151700
  gini_index: 0.4437
  vacancy_rate: 13.87
  race_white: 108555
  race_black: 1190
  race_asian: 923
  race_native: 156
  hispanic: 3925
  bachelors_plus: 24137
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.7737
  - to: "us/states/ny/districts/senate/49"
    rel: in-district
    area_weight: 0.3987
  - to: "us/states/ny/districts/senate/50"
    rel: in-district
    area_weight: 0.3771
  - to: "us/states/ny/districts/house/120"
    rel: in-district
    area_weight: 0.7757
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Oswego County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 117953 |
| Under 18 | 24276 |
| 18–64 | 72494 |
| 65+ | 21183 |
| Median household income | 69183 |
| Poverty rate | 16.32 |
| Homeownership rate | 73.41 |
| Unemployment rate | 7.01 |
| Median home value | 151700 |
| Gini index | 0.4437 |
| Vacancy rate | 13.87 |
| White | 108555 |
| Black | 1190 |
| Asian | 923 |
| Native | 156 |
| Hispanic/Latino | 3925 |
| Bachelor's or higher | 24137 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 77% (congressional)
- [NY Senate District 49](/us/states/ny/districts/senate/49.md) — 40% (state senate)
- [NY Senate District 50](/us/states/ny/districts/senate/50.md) — 38% (state senate)
- [NY House District 120](/us/states/ny/districts/house/120.md) — 78% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
