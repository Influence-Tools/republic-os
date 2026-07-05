---
type: Jurisdiction
title: "Grant County, AR"
classification: county
fips: "05053"
state: "AR"
demographics:
  population: 18242
  population_under_18: 3847
  population_18_64: 11026
  population_65_plus: 3369
  median_household_income: 71549
  poverty_rate: 13.09
  homeownership_rate: 80.74
  unemployment_rate: 4.54
  median_home_value: 161700
  gini_index: 0.4502
  vacancy_rate: 12.3
  race_white: 16660
  race_black: 490
  race_asian: 89
  race_native: 26
  hispanic: 522
  bachelors_plus: 3431
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ar/districts/senate/2"
    rel: in-district
    area_weight: 0.4705
  - to: "us/states/ar/districts/senate/1"
    rel: in-district
    area_weight: 0.2694
  - to: "us/states/ar/districts/senate/7"
    rel: in-district
    area_weight: 0.2601
  - to: "us/states/ar/districts/house/92"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Grant County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18242 |
| Under 18 | 3847 |
| 18–64 | 11026 |
| 65+ | 3369 |
| Median household income | 71549 |
| Poverty rate | 13.09 |
| Homeownership rate | 80.74 |
| Unemployment rate | 4.54 |
| Median home value | 161700 |
| Gini index | 0.4502 |
| Vacancy rate | 12.3 |
| White | 16660 |
| Black | 490 |
| Asian | 89 |
| Native | 26 |
| Hispanic/Latino | 522 |
| Bachelor's or higher | 3431 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 2](/us/states/ar/districts/senate/2.md) — 47% (state senate)
- [AR Senate District 1](/us/states/ar/districts/senate/1.md) — 27% (state senate)
- [AR Senate District 7](/us/states/ar/districts/senate/7.md) — 26% (state senate)
- [AR House District 92](/us/states/ar/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
