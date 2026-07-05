---
type: Jurisdiction
title: "Dallas County, AR"
classification: county
fips: "05039"
state: "AR"
demographics:
  population: 6242
  population_under_18: 1256
  population_18_64: 3396
  population_65_plus: 1590
  median_household_income: 42500
  poverty_rate: 13.92
  homeownership_rate: 72.63
  unemployment_rate: 8.25
  median_home_value: 97300
  gini_index: 0.4576
  vacancy_rate: 26.28
  race_white: 3289
  race_black: 2657
  race_asian: 8
  race_native: 0
  hispanic: 71
  bachelors_plus: 715
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/2"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Dallas County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6242 |
| Under 18 | 1256 |
| 18–64 | 3396 |
| 65+ | 1590 |
| Median household income | 42500 |
| Poverty rate | 13.92 |
| Homeownership rate | 72.63 |
| Unemployment rate | 8.25 |
| Median home value | 97300 |
| Gini index | 0.4576 |
| Vacancy rate | 26.28 |
| White | 3289 |
| Black | 2657 |
| Asian | 8 |
| Native | 0 |
| Hispanic/Latino | 71 |
| Bachelor's or higher | 715 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 2](/us/states/ar/districts/senate/2.md) — 100% (state senate)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
