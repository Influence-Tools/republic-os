---
type: Jurisdiction
title: "Ogle County, IL"
classification: county
fips: "17141"
state: "IL"
demographics:
  population: 51495
  population_under_18: 11430
  population_18_64: 29791
  population_65_plus: 10274
  median_household_income: 82132
  poverty_rate: 8.36
  homeownership_rate: 75.37
  unemployment_rate: 5.04
  median_home_value: 189200
  gini_index: 0.4113
  vacancy_rate: 8.2
  race_white: 44083
  race_black: 636
  race_asian: 294
  race_native: 264
  hispanic: 6144
  bachelors_plus: 11678
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/45"
    rel: in-district
    area_weight: 0.7433
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.2566
  - to: "us/states/il/districts/house/89"
    rel: in-district
    area_weight: 0.7433
  - to: "us/states/il/districts/house/74"
    rel: in-district
    area_weight: 0.2566
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Ogle County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51495 |
| Under 18 | 11430 |
| 18–64 | 29791 |
| 65+ | 10274 |
| Median household income | 82132 |
| Poverty rate | 8.36 |
| Homeownership rate | 75.37 |
| Unemployment rate | 5.04 |
| Median home value | 189200 |
| Gini index | 0.4113 |
| Vacancy rate | 8.2 |
| White | 44083 |
| Black | 636 |
| Asian | 294 |
| Native | 264 |
| Hispanic/Latino | 6144 |
| Bachelor's or higher | 11678 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 45](/us/states/il/districts/senate/45.md) — 74% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 26% (state senate)
- [IL House District 89](/us/states/il/districts/house/89.md) — 74% (state house)
- [IL House District 74](/us/states/il/districts/house/74.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
