---
type: Jurisdiction
title: "Schuyler County, NY"
classification: county
fips: "36097"
state: "NY"
demographics:
  population: 17562
  population_under_18: 3299
  population_18_64: 10218
  population_65_plus: 4045
  median_household_income: 67663
  poverty_rate: 14.84
  homeownership_rate: 79.17
  unemployment_rate: 6.53
  median_home_value: 171800
  gini_index: 0.4459
  vacancy_rate: 24.58
  race_white: 16345
  race_black: 225
  race_asian: 85
  race_native: 39
  hispanic: 366
  bachelors_plus: 5304
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.5245
  - to: "us/states/ny/districts/23"
    rel: in-district
    area_weight: 0.4751
  - to: "us/states/ny/districts/senate/58"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/132"
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

# Schuyler County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17562 |
| Under 18 | 3299 |
| 18–64 | 10218 |
| 65+ | 4045 |
| Median household income | 67663 |
| Poverty rate | 14.84 |
| Homeownership rate | 79.17 |
| Unemployment rate | 6.53 |
| Median home value | 171800 |
| Gini index | 0.4459 |
| Vacancy rate | 24.58 |
| White | 16345 |
| Black | 225 |
| Asian | 85 |
| Native | 39 |
| Hispanic/Latino | 366 |
| Bachelor's or higher | 5304 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 52% (congressional)
- [NY-23](/us/states/ny/districts/23.md) — 48% (congressional)
- [NY Senate District 58](/us/states/ny/districts/senate/58.md) — 100% (state senate)
- [NY House District 132](/us/states/ny/districts/house/132.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
