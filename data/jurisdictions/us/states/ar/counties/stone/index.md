---
type: Jurisdiction
title: "Stone County, AR"
classification: county
fips: "05137"
state: "AR"
demographics:
  population: 12568
  population_under_18: 2471
  population_18_64: 6550
  population_65_plus: 3547
  median_household_income: 40943
  poverty_rate: 19.35
  homeownership_rate: 75.94
  unemployment_rate: 3.23
  median_home_value: 171600
  gini_index: 0.4545
  vacancy_rate: 22.9
  race_white: 11302
  race_black: 11
  race_asian: 8
  race_native: 107
  hispanic: 281
  bachelors_plus: 2027
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/senate/24"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/41"
    rel: in-district
    area_weight: 0.4722
  - to: "us/states/ar/districts/house/27"
    rel: in-district
    area_weight: 0.2895
  - to: "us/states/ar/districts/house/28"
    rel: in-district
    area_weight: 0.2383
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Stone County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12568 |
| Under 18 | 2471 |
| 18–64 | 6550 |
| 65+ | 3547 |
| Median household income | 40943 |
| Poverty rate | 19.35 |
| Homeownership rate | 75.94 |
| Unemployment rate | 3.23 |
| Median home value | 171600 |
| Gini index | 0.4545 |
| Vacancy rate | 22.9 |
| White | 11302 |
| Black | 11 |
| Asian | 8 |
| Native | 107 |
| Hispanic/Latino | 281 |
| Bachelor's or higher | 2027 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 24](/us/states/ar/districts/senate/24.md) — 100% (state senate)
- [AR House District 41](/us/states/ar/districts/house/41.md) — 47% (state house)
- [AR House District 27](/us/states/ar/districts/house/27.md) — 29% (state house)
- [AR House District 28](/us/states/ar/districts/house/28.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
