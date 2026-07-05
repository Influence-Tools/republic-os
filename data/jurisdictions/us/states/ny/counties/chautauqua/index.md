---
type: Jurisdiction
title: "Chautauqua County, NY"
classification: county
fips: "36013"
state: "NY"
demographics:
  population: 125544
  population_under_18: 25803
  population_18_64: 72824
  population_65_plus: 26917
  median_household_income: 58351
  poverty_rate: 17.43
  homeownership_rate: 68.85
  unemployment_rate: 5.92
  median_home_value: 127900
  gini_index: 0.4442
  vacancy_rate: 19.68
  race_white: 108193
  race_black: 3286
  race_asian: 876
  race_native: 411
  hispanic: 12039
  bachelors_plus: 32141
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.7216
  - to: "us/states/ny/districts/senate/57"
    rel: in-district
    area_weight: 0.722
  - to: "us/states/ny/districts/house/150"
    rel: in-district
    area_weight: 0.722
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Chautauqua County, NY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 125544 |
| Under 18 | 25803 |
| 18–64 | 72824 |
| 65+ | 26917 |
| Median household income | 58351 |
| Poverty rate | 17.43 |
| Homeownership rate | 68.85 |
| Unemployment rate | 5.92 |
| Median home value | 127900 |
| Gini index | 0.4442 |
| Vacancy rate | 19.68 |
| White | 108193 |
| Black | 3286 |
| Asian | 876 |
| Native | 411 |
| Hispanic/Latino | 12039 |
| Bachelor's or higher | 32141 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 72% (congressional)
- [NY Senate District 57](/us/states/ny/districts/senate/57.md) — 72% (state senate)
- [NY House District 150](/us/states/ny/districts/house/150.md) — 72% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
