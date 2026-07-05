---
type: Jurisdiction
title: "Cameron County, PA"
classification: county
fips: "42023"
state: "PA"
demographics:
  population: 4427
  population_under_18: 748
  population_18_64: 2375
  population_65_plus: 1304
  median_household_income: 50573
  poverty_rate: 13.51
  homeownership_rate: 72.43
  unemployment_rate: 7.8
  median_home_value: 88900
  gini_index: 0.419
  vacancy_rate: 43.47
  race_white: 4101
  race_black: 4
  race_asian: 20
  race_native: 13
  hispanic: 31
  bachelors_plus: 581
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/25"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/house/67"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Cameron County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4427 |
| Under 18 | 748 |
| 18–64 | 2375 |
| 65+ | 1304 |
| Median household income | 50573 |
| Poverty rate | 13.51 |
| Homeownership rate | 72.43 |
| Unemployment rate | 7.8 |
| Median home value | 88900 |
| Gini index | 0.419 |
| Vacancy rate | 43.47 |
| White | 4101 |
| Black | 4 |
| Asian | 20 |
| Native | 13 |
| Hispanic/Latino | 31 |
| Bachelor's or higher | 581 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 25](/us/states/pa/districts/senate/25.md) — 100% (state senate)
- [PA House District 67](/us/states/pa/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
