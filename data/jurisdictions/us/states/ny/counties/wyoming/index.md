---
type: Jurisdiction
title: "Wyoming County, NY"
classification: county
fips: "36121"
state: "NY"
demographics:
  population: 39753
  population_under_18: 7339
  population_18_64: 24302
  population_65_plus: 8112
  median_household_income: 69110
  poverty_rate: 11.13
  homeownership_rate: 75.94
  unemployment_rate: 3.65
  median_home_value: 162300
  gini_index: 0.4148
  vacancy_rate: 9.91
  race_white: 35674
  race_black: 1544
  race_asian: 180
  race_native: 64
  hispanic: 1492
  bachelors_plus: 7637
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ny/districts/senate/57"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/147"
    rel: in-district
    area_weight: 0.8298
  - to: "us/states/ny/districts/house/133"
    rel: in-district
    area_weight: 0.1701
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Wyoming County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39753 |
| Under 18 | 7339 |
| 18–64 | 24302 |
| 65+ | 8112 |
| Median household income | 69110 |
| Poverty rate | 11.13 |
| Homeownership rate | 75.94 |
| Unemployment rate | 3.65 |
| Median home value | 162300 |
| Gini index | 0.4148 |
| Vacancy rate | 9.91 |
| White | 35674 |
| Black | 1544 |
| Asian | 180 |
| Native | 64 |
| Hispanic/Latino | 1492 |
| Bachelor's or higher | 7637 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 100% (congressional)
- [NY Senate District 57](/us/states/ny/districts/senate/57.md) — 100% (state senate)
- [NY House District 147](/us/states/ny/districts/house/147.md) — 83% (state house)
- [NY House District 133](/us/states/ny/districts/house/133.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
