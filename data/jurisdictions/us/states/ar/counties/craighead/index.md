---
type: Jurisdiction
title: "Craighead County, AR"
classification: county
fips: "05031"
state: "AR"
demographics:
  population: 113249
  population_under_18: 28553
  population_18_64: 68973
  population_65_plus: 15723
  median_household_income: 59548
  poverty_rate: 20.12
  homeownership_rate: 60.11
  unemployment_rate: 5.57
  median_home_value: 210400
  gini_index: 0.4908
  vacancy_rate: 9.1
  race_white: 81397
  race_black: 18982
  race_asian: 1404
  race_native: 246
  hispanic: 7146
  bachelors_plus: 30104
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/19"
    rel: in-district
    area_weight: 0.7946
  - to: "us/states/ar/districts/senate/20"
    rel: in-district
    area_weight: 0.2051
  - to: "us/states/ar/districts/house/33"
    rel: in-district
    area_weight: 0.4455
  - to: "us/states/ar/districts/house/38"
    rel: in-district
    area_weight: 0.2973
  - to: "us/states/ar/districts/house/30"
    rel: in-district
    area_weight: 0.1347
  - to: "us/states/ar/districts/house/36"
    rel: in-district
    area_weight: 0.0891
  - to: "us/states/ar/districts/house/32"
    rel: in-district
    area_weight: 0.0333
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Craighead County, AR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 113249 |
| Under 18 | 28553 |
| 18–64 | 68973 |
| 65+ | 15723 |
| Median household income | 59548 |
| Poverty rate | 20.12 |
| Homeownership rate | 60.11 |
| Unemployment rate | 5.57 |
| Median home value | 210400 |
| Gini index | 0.4908 |
| Vacancy rate | 9.1 |
| White | 81397 |
| Black | 18982 |
| Asian | 1404 |
| Native | 246 |
| Hispanic/Latino | 7146 |
| Bachelor's or higher | 30104 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 19](/us/states/ar/districts/senate/19.md) — 79% (state senate)
- [AR Senate District 20](/us/states/ar/districts/senate/20.md) — 21% (state senate)
- [AR House District 33](/us/states/ar/districts/house/33.md) — 45% (state house)
- [AR House District 38](/us/states/ar/districts/house/38.md) — 30% (state house)
- [AR House District 30](/us/states/ar/districts/house/30.md) — 13% (state house)
- [AR House District 36](/us/states/ar/districts/house/36.md) — 9% (state house)
- [AR House District 32](/us/states/ar/districts/house/32.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
