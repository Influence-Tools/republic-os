---
type: Jurisdiction
title: "Saline County, AR"
classification: county
fips: "05125"
state: "AR"
demographics:
  population: 127479
  population_under_18: 29643
  population_18_64: 74392
  population_65_plus: 23444
  median_household_income: 79046
  poverty_rate: 8.82
  homeownership_rate: 78.22
  unemployment_rate: 3.9
  median_home_value: 221200
  gini_index: 0.4067
  vacancy_rate: 5.16
  race_white: 102429
  race_black: 12001
  race_asian: 1326
  race_native: 286
  hispanic: 9282
  bachelors_plus: 34108
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ar/districts/senate/7"
    rel: in-district
    area_weight: 0.4807
  - to: "us/states/ar/districts/senate/6"
    rel: in-district
    area_weight: 0.3422
  - to: "us/states/ar/districts/senate/16"
    rel: in-district
    area_weight: 0.1769
  - to: "us/states/ar/districts/house/54"
    rel: in-district
    area_weight: 0.4084
  - to: "us/states/ar/districts/house/83"
    rel: in-district
    area_weight: 0.182
  - to: "us/states/ar/districts/house/92"
    rel: in-district
    area_weight: 0.1151
  - to: "us/states/ar/districts/house/29"
    rel: in-district
    area_weight: 0.0855
  - to: "us/states/ar/districts/house/78"
    rel: in-district
    area_weight: 0.0796
  - to: "us/states/ar/districts/house/82"
    rel: in-district
    area_weight: 0.0752
  - to: "us/states/ar/districts/house/81"
    rel: in-district
    area_weight: 0.0541
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Saline County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 127479 |
| Under 18 | 29643 |
| 18–64 | 74392 |
| 65+ | 23444 |
| Median household income | 79046 |
| Poverty rate | 8.82 |
| Homeownership rate | 78.22 |
| Unemployment rate | 3.9 |
| Median home value | 221200 |
| Gini index | 0.4067 |
| Vacancy rate | 5.16 |
| White | 102429 |
| Black | 12001 |
| Asian | 1326 |
| Native | 286 |
| Hispanic/Latino | 9282 |
| Bachelor's or higher | 34108 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 7](/us/states/ar/districts/senate/7.md) — 48% (state senate)
- [AR Senate District 6](/us/states/ar/districts/senate/6.md) — 34% (state senate)
- [AR Senate District 16](/us/states/ar/districts/senate/16.md) — 18% (state senate)
- [AR House District 54](/us/states/ar/districts/house/54.md) — 41% (state house)
- [AR House District 83](/us/states/ar/districts/house/83.md) — 18% (state house)
- [AR House District 92](/us/states/ar/districts/house/92.md) — 12% (state house)
- [AR House District 29](/us/states/ar/districts/house/29.md) — 9% (state house)
- [AR House District 78](/us/states/ar/districts/house/78.md) — 8% (state house)
- [AR House District 82](/us/states/ar/districts/house/82.md) — 8% (state house)
- [AR House District 81](/us/states/ar/districts/house/81.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
