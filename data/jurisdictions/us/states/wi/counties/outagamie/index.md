---
type: Jurisdiction
title: "Outagamie County, WI"
classification: county
fips: "55087"
state: "WI"
demographics:
  population: 192826
  population_under_18: 44257
  population_18_64: 116586
  population_65_plus: 31983
  median_household_income: 85069
  poverty_rate: 6.29
  homeownership_rate: 71.48
  unemployment_rate: 2.74
  median_home_value: 267300
  gini_index: 0.4468
  vacancy_rate: 3.13
  race_white: 165450
  race_black: 3138
  race_asian: 7230
  race_native: 2225
  hispanic: 10177
  bachelors_plus: 55703
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.5868
  - to: "us/states/wi/districts/senate/2"
    rel: in-district
    area_weight: 0.3398
  - to: "us/states/wi/districts/senate/1"
    rel: in-district
    area_weight: 0.0373
  - to: "us/states/wi/districts/senate/18"
    rel: in-district
    area_weight: 0.0361
  - to: "us/states/wi/districts/house/56"
    rel: in-district
    area_weight: 0.5333
  - to: "us/states/wi/districts/house/5"
    rel: in-district
    area_weight: 0.3397
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.0471
  - to: "us/states/wi/districts/house/2"
    rel: in-district
    area_weight: 0.0373
  - to: "us/states/wi/districts/house/52"
    rel: in-district
    area_weight: 0.034
  - to: "us/states/wi/districts/house/55"
    rel: in-district
    area_weight: 0.0064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Outagamie County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 192826 |
| Under 18 | 44257 |
| 18–64 | 116586 |
| 65+ | 31983 |
| Median household income | 85069 |
| Poverty rate | 6.29 |
| Homeownership rate | 71.48 |
| Unemployment rate | 2.74 |
| Median home value | 267300 |
| Gini index | 0.4468 |
| Vacancy rate | 3.13 |
| White | 165450 |
| Black | 3138 |
| Asian | 7230 |
| Native | 2225 |
| Hispanic/Latino | 10177 |
| Bachelor's or higher | 55703 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 100% (congressional)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 59% (state senate)
- [WI Senate District 2](/us/states/wi/districts/senate/2.md) — 34% (state senate)
- [WI Senate District 1](/us/states/wi/districts/senate/1.md) — 4% (state senate)
- [WI Senate District 18](/us/states/wi/districts/senate/18.md) — 4% (state senate)
- [WI House District 56](/us/states/wi/districts/house/56.md) — 53% (state house)
- [WI House District 5](/us/states/wi/districts/house/5.md) — 34% (state house)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 5% (state house)
- [WI House District 2](/us/states/wi/districts/house/2.md) — 4% (state house)
- [WI House District 52](/us/states/wi/districts/house/52.md) — 3% (state house)
- [WI House District 55](/us/states/wi/districts/house/55.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
