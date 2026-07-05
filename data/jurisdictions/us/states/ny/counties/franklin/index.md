---
type: Jurisdiction
title: "Franklin County, NY"
classification: county
fips: "36033"
state: "NY"
demographics:
  population: 46696
  population_under_18: 9302
  population_18_64: 28274
  population_65_plus: 9120
  median_household_income: 65151
  poverty_rate: 18.25
  homeownership_rate: 72.52
  unemployment_rate: 3.93
  median_home_value: 145400
  gini_index: 0.4253
  vacancy_rate: 23.46
  race_white: 39221
  race_black: 1659
  race_asian: 314
  race_native: 3293
  hispanic: 1350
  bachelors_plus: 11854
districts:
  - to: "us/states/ny/districts/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/senate/45"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ny/districts/house/115"
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

# Franklin County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46696 |
| Under 18 | 9302 |
| 18–64 | 28274 |
| 65+ | 9120 |
| Median household income | 65151 |
| Poverty rate | 18.25 |
| Homeownership rate | 72.52 |
| Unemployment rate | 3.93 |
| Median home value | 145400 |
| Gini index | 0.4253 |
| Vacancy rate | 23.46 |
| White | 39221 |
| Black | 1659 |
| Asian | 314 |
| Native | 3293 |
| Hispanic/Latino | 1350 |
| Bachelor's or higher | 11854 |

## Districts

- [NY-21](/us/states/ny/districts/21.md) — 100% (congressional)
- [NY Senate District 45](/us/states/ny/districts/senate/45.md) — 100% (state senate)
- [NY House District 115](/us/states/ny/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
