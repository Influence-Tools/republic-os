---
type: Jurisdiction
title: "Rock County, WI"
classification: county
fips: "55105"
state: "WI"
demographics:
  population: 164350
  population_under_18: 36803
  population_18_64: 98279
  population_65_plus: 29268
  median_household_income: 75673
  poverty_rate: 9.26
  homeownership_rate: 71.16
  unemployment_rate: 3.76
  median_home_value: 231600
  gini_index: 0.4077
  vacancy_rate: 5.5
  race_white: 134161
  race_black: 7727
  race_asian: 1779
  race_native: 564
  hispanic: 16646
  bachelors_plus: 38594
districts:
  - to: "us/states/wi/districts/02"
    rel: in-district
    area_weight: 0.5485
  - to: "us/states/wi/districts/01"
    rel: in-district
    area_weight: 0.4514
  - to: "us/states/wi/districts/senate/15"
    rel: in-district
    area_weight: 0.8994
  - to: "us/states/wi/districts/senate/11"
    rel: in-district
    area_weight: 0.1002
  - to: "us/states/wi/districts/house/45"
    rel: in-district
    area_weight: 0.3494
  - to: "us/states/wi/districts/house/44"
    rel: in-district
    area_weight: 0.3079
  - to: "us/states/wi/districts/house/43"
    rel: in-district
    area_weight: 0.2422
  - to: "us/states/wi/districts/house/31"
    rel: in-district
    area_weight: 0.1002
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Rock County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 164350 |
| Under 18 | 36803 |
| 18–64 | 98279 |
| 65+ | 29268 |
| Median household income | 75673 |
| Poverty rate | 9.26 |
| Homeownership rate | 71.16 |
| Unemployment rate | 3.76 |
| Median home value | 231600 |
| Gini index | 0.4077 |
| Vacancy rate | 5.5 |
| White | 134161 |
| Black | 7727 |
| Asian | 1779 |
| Native | 564 |
| Hispanic/Latino | 16646 |
| Bachelor's or higher | 38594 |

## Districts

- [WI-02](/us/states/wi/districts/02.md) — 55% (congressional)
- [WI-01](/us/states/wi/districts/01.md) — 45% (congressional)
- [WI Senate District 15](/us/states/wi/districts/senate/15.md) — 90% (state senate)
- [WI Senate District 11](/us/states/wi/districts/senate/11.md) — 10% (state senate)
- [WI House District 45](/us/states/wi/districts/house/45.md) — 35% (state house)
- [WI House District 44](/us/states/wi/districts/house/44.md) — 31% (state house)
- [WI House District 43](/us/states/wi/districts/house/43.md) — 24% (state house)
- [WI House District 31](/us/states/wi/districts/house/31.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
