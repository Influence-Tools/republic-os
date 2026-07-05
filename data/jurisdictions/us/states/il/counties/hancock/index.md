---
type: Jurisdiction
title: "Hancock County, IL"
classification: county
fips: "17067"
state: "IL"
demographics:
  population: 17281
  population_under_18: 3635
  population_18_64: 9390
  population_65_plus: 4256
  median_household_income: 65865
  poverty_rate: 12.27
  homeownership_rate: 81.32
  unemployment_rate: 4.23
  median_home_value: 113800
  gini_index: 0.4426
  vacancy_rate: 14.82
  race_white: 16283
  race_black: 128
  race_asian: 62
  race_native: 23
  hispanic: 397
  bachelors_plus: 4084
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Hancock County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17281 |
| Under 18 | 3635 |
| 18–64 | 9390 |
| 65+ | 4256 |
| Median household income | 65865 |
| Poverty rate | 12.27 |
| Homeownership rate | 81.32 |
| Unemployment rate | 4.23 |
| Median home value | 113800 |
| Gini index | 0.4426 |
| Vacancy rate | 14.82 |
| White | 16283 |
| Black | 128 |
| Asian | 62 |
| Native | 23 |
| Hispanic/Latino | 397 |
| Bachelor's or higher | 4084 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 100% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
