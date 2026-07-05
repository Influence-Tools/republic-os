---
type: Jurisdiction
title: "Fond du Lac County, WI"
classification: county
fips: "55039"
state: "WI"
demographics:
  population: 104137
  population_under_18: 21999
  population_18_64: 61524
  population_65_plus: 20614
  median_household_income: 74275
  poverty_rate: 9.24
  homeownership_rate: 70.71
  unemployment_rate: 3.17
  median_home_value: 222800
  gini_index: 0.4064
  vacancy_rate: 6.19
  race_white: 91257
  race_black: 1770
  race_asian: 1976
  race_native: 444
  hispanic: 7129
  bachelors_plus: 21529
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.4752
  - to: "us/states/wi/districts/senate/20"
    rel: in-district
    area_weight: 0.3478
  - to: "us/states/wi/districts/senate/9"
    rel: in-district
    area_weight: 0.1262
  - to: "us/states/wi/districts/house/39"
    rel: in-district
    area_weight: 0.3318
  - to: "us/states/wi/districts/house/59"
    rel: in-district
    area_weight: 0.237
  - to: "us/states/wi/districts/house/37"
    rel: in-district
    area_weight: 0.1433
  - to: "us/states/wi/districts/house/27"
    rel: in-district
    area_weight: 0.1262
  - to: "us/states/wi/districts/house/60"
    rel: in-district
    area_weight: 0.1108
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Fond du Lac County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104137 |
| Under 18 | 21999 |
| 18–64 | 61524 |
| 65+ | 20614 |
| Median household income | 74275 |
| Poverty rate | 9.24 |
| Homeownership rate | 70.71 |
| Unemployment rate | 3.17 |
| Median home value | 222800 |
| Gini index | 0.4064 |
| Vacancy rate | 6.19 |
| White | 91257 |
| Black | 1770 |
| Asian | 1976 |
| Native | 444 |
| Hispanic/Latino | 7129 |
| Bachelor's or higher | 21529 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 100% (congressional)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 48% (state senate)
- [WI Senate District 20](/us/states/wi/districts/senate/20.md) — 35% (state senate)
- [WI Senate District 9](/us/states/wi/districts/senate/9.md) — 13% (state senate)
- [WI House District 39](/us/states/wi/districts/house/39.md) — 33% (state house)
- [WI House District 59](/us/states/wi/districts/house/59.md) — 24% (state house)
- [WI House District 37](/us/states/wi/districts/house/37.md) — 14% (state house)
- [WI House District 27](/us/states/wi/districts/house/27.md) — 13% (state house)
- [WI House District 60](/us/states/wi/districts/house/60.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
