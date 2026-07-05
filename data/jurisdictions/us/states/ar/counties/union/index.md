---
type: Jurisdiction
title: "Union County, AR"
classification: county
fips: "05139"
state: "AR"
demographics:
  population: 37900
  population_under_18: 8984
  population_18_64: 21628
  population_65_plus: 7288
  median_household_income: 55259
  poverty_rate: 19.55
  homeownership_rate: 72.69
  unemployment_rate: 5.48
  median_home_value: 120900
  gini_index: 0.4796
  vacancy_rate: 19.56
  race_white: 23334
  race_black: 12235
  race_asian: 325
  race_native: 73
  hispanic: 1793
  bachelors_plus: 6718
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/97"
    rel: in-district
    area_weight: 0.5866
  - to: "us/states/ar/districts/house/96"
    rel: in-district
    area_weight: 0.4133
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Union County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37900 |
| Under 18 | 8984 |
| 18–64 | 21628 |
| 65+ | 7288 |
| Median household income | 55259 |
| Poverty rate | 19.55 |
| Homeownership rate | 72.69 |
| Unemployment rate | 5.48 |
| Median home value | 120900 |
| Gini index | 0.4796 |
| Vacancy rate | 19.56 |
| White | 23334 |
| Black | 12235 |
| Asian | 325 |
| Native | 73 |
| Hispanic/Latino | 1793 |
| Bachelor's or higher | 6718 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 2](/us/states/ar/districts/senate/2.md) — 100% (state senate)
- [AR House District 97](/us/states/ar/districts/house/97.md) — 59% (state house)
- [AR House District 96](/us/states/ar/districts/house/96.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
