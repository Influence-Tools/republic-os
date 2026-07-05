---
type: Jurisdiction
title: "Jackson County, AR"
classification: county
fips: "05067"
state: "AR"
demographics:
  population: 16712
  population_under_18: 3336
  population_18_64: 10378
  population_65_plus: 2998
  median_household_income: 44218
  poverty_rate: 21.66
  homeownership_rate: 65.47
  unemployment_rate: 9.78
  median_home_value: 98300
  gini_index: 0.4974
  vacancy_rate: 14.36
  race_white: 12571
  race_black: 2541
  race_asian: 59
  race_native: 78
  hispanic: 544
  bachelors_plus: 2369
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ar/districts/house/39"
    rel: in-district
    area_weight: 0.4544
  - to: "us/states/ar/districts/house/61"
    rel: in-district
    area_weight: 0.2997
  - to: "us/states/ar/districts/house/38"
    rel: in-district
    area_weight: 0.2457
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Jackson County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16712 |
| Under 18 | 3336 |
| 18–64 | 10378 |
| 65+ | 2998 |
| Median household income | 44218 |
| Poverty rate | 21.66 |
| Homeownership rate | 65.47 |
| Unemployment rate | 9.78 |
| Median home value | 98300 |
| Gini index | 0.4974 |
| Vacancy rate | 14.36 |
| White | 12571 |
| Black | 2541 |
| Asian | 59 |
| Native | 78 |
| Hispanic/Latino | 544 |
| Bachelor's or higher | 2369 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 100% (state senate)
- [AR House District 39](/us/states/ar/districts/house/39.md) — 45% (state house)
- [AR House District 61](/us/states/ar/districts/house/61.md) — 30% (state house)
- [AR House District 38](/us/states/ar/districts/house/38.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
