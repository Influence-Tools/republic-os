---
type: Jurisdiction
title: "Manistee County, MI"
classification: county
fips: "26101"
state: "MI"
demographics:
  population: 25350
  population_under_18: 4218
  population_18_64: 14037
  population_65_plus: 7095
  median_household_income: 63516
  poverty_rate: 12.65
  homeownership_rate: 85.76
  unemployment_rate: 6.36
  median_home_value: 182200
  gini_index: 0.4465
  vacancy_rate: 32.79
  race_white: 22442
  race_black: 859
  race_asian: 104
  race_native: 324
  hispanic: 904
  bachelors_plus: 6473
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.4353
  - to: "us/states/mi/districts/senate/32"
    rel: in-district
    area_weight: 0.239
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.1963
  - to: "us/states/mi/districts/house/104"
    rel: in-district
    area_weight: 0.3119
  - to: "us/states/mi/districts/house/102"
    rel: in-district
    area_weight: 0.1234
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Manistee County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25350 |
| Under 18 | 4218 |
| 18–64 | 14037 |
| 65+ | 7095 |
| Median household income | 63516 |
| Poverty rate | 12.65 |
| Homeownership rate | 85.76 |
| Unemployment rate | 6.36 |
| Median home value | 182200 |
| Gini index | 0.4465 |
| Vacancy rate | 32.79 |
| White | 22442 |
| Black | 859 |
| Asian | 104 |
| Native | 324 |
| Hispanic/Latino | 904 |
| Bachelor's or higher | 6473 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 44% (congressional)
- [MI Senate District 32](/us/states/mi/districts/senate/32.md) — 24% (state senate)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 20% (state senate)
- [MI House District 104](/us/states/mi/districts/house/104.md) — 31% (state house)
- [MI House District 102](/us/states/mi/districts/house/102.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
