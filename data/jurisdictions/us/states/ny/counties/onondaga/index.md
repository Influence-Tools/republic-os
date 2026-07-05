---
type: Jurisdiction
title: "Onondaga County, NY"
classification: county
fips: "36067"
state: "NY"
demographics:
  population: 471129
  population_under_18: 98554
  population_18_64: 284589
  population_65_plus: 87986
  median_household_income: 76945
  poverty_rate: 13.8
  homeownership_rate: 65.93
  unemployment_rate: 5.19
  median_home_value: 200200
  gini_index: 0.4644
  vacancy_rate: 6.72
  race_white: 352626
  race_black: 50904
  race_asian: 19457
  race_native: 2263
  hispanic: 27930
  bachelors_plus: 184654
districts:
  - to: "us/states/ny/districts/22"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/ny/districts/senate/48"
    rel: in-district
    area_weight: 0.6981
  - to: "us/states/ny/districts/senate/50"
    rel: in-district
    area_weight: 0.3018
  - to: "us/states/ny/districts/house/126"
    rel: in-district
    area_weight: 0.5808
  - to: "us/states/ny/districts/house/127"
    rel: in-district
    area_weight: 0.1832
  - to: "us/states/ny/districts/house/128"
    rel: in-district
    area_weight: 0.1539
  - to: "us/states/ny/districts/house/129"
    rel: in-district
    area_weight: 0.0818
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Onondaga County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 471129 |
| Under 18 | 98554 |
| 18–64 | 284589 |
| 65+ | 87986 |
| Median household income | 76945 |
| Poverty rate | 13.8 |
| Homeownership rate | 65.93 |
| Unemployment rate | 5.19 |
| Median home value | 200200 |
| Gini index | 0.4644 |
| Vacancy rate | 6.72 |
| White | 352626 |
| Black | 50904 |
| Asian | 19457 |
| Native | 2263 |
| Hispanic/Latino | 27930 |
| Bachelor's or higher | 184654 |

## Districts

- [NY-22](/us/states/ny/districts/22.md) — 100% (congressional)
- [NY Senate District 48](/us/states/ny/districts/senate/48.md) — 70% (state senate)
- [NY Senate District 50](/us/states/ny/districts/senate/50.md) — 30% (state senate)
- [NY House District 126](/us/states/ny/districts/house/126.md) — 58% (state house)
- [NY House District 127](/us/states/ny/districts/house/127.md) — 18% (state house)
- [NY House District 128](/us/states/ny/districts/house/128.md) — 15% (state house)
- [NY House District 129](/us/states/ny/districts/house/129.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
