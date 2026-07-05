---
type: Jurisdiction
title: "Tioga County, NY"
classification: county
fips: "36107"
state: "NY"
demographics:
  population: 47864
  population_under_18: 9728
  population_18_64: 27697
  population_65_plus: 10439
  median_household_income: 72739
  poverty_rate: 13.36
  homeownership_rate: 79.08
  unemployment_rate: 5.48
  median_home_value: 160800
  gini_index: 0.462
  vacancy_rate: 7.95
  race_white: 44735
  race_black: 624
  race_asian: 454
  race_native: 11
  hispanic: 1149
  bachelors_plus: 12223
districts:
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ny/districts/house/124"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Tioga County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47864 |
| Under 18 | 9728 |
| 18–64 | 27697 |
| 65+ | 10439 |
| Median household income | 72739 |
| Poverty rate | 13.36 |
| Homeownership rate | 79.08 |
| Unemployment rate | 5.48 |
| Median home value | 160800 |
| Gini index | 0.462 |
| Vacancy rate | 7.95 |
| White | 44735 |
| Black | 624 |
| Asian | 454 |
| Native | 11 |
| Hispanic/Latino | 1149 |
| Bachelor's or higher | 12223 |

## Districts

- [NY-23](/us/states/ny/districts/23.md) — 100% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 124](/us/states/ny/districts/house/124.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
