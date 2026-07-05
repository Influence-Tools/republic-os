---
type: Jurisdiction
title: "Lancaster County, PA"
classification: county
fips: "42071"
state: "PA"
demographics:
  population: 557931
  population_under_18: 128950
  population_18_64: 319547
  population_65_plus: 109434
  median_household_income: 86959
  poverty_rate: 8.19
  homeownership_rate: 69.82
  unemployment_rate: 3.37
  median_home_value: 301100
  gini_index: 0.4301
  vacancy_rate: 2.95
  race_white: 455405
  race_black: 22388
  race_asian: 13540
  race_native: 1162
  hispanic: 64326
  bachelors_plus: 168247
districts:
  - to: "us/states/pa/districts/11"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/pa/districts/senate/13"
    rel: in-district
    area_weight: 0.5488
  - to: "us/states/pa/districts/senate/36"
    rel: in-district
    area_weight: 0.3506
  - to: "us/states/pa/districts/senate/48"
    rel: in-district
    area_weight: 0.1003
  - to: "us/states/pa/districts/house/100"
    rel: in-district
    area_weight: 0.314
  - to: "us/states/pa/districts/house/37"
    rel: in-district
    area_weight: 0.1441
  - to: "us/states/pa/districts/house/99"
    rel: in-district
    area_weight: 0.1396
  - to: "us/states/pa/districts/house/97"
    rel: in-district
    area_weight: 0.1215
  - to: "us/states/pa/districts/house/43"
    rel: in-district
    area_weight: 0.1038
  - to: "us/states/pa/districts/house/98"
    rel: in-district
    area_weight: 0.0934
  - to: "us/states/pa/districts/house/41"
    rel: in-district
    area_weight: 0.0498
  - to: "us/states/pa/districts/house/96"
    rel: in-district
    area_weight: 0.0219
  - to: "us/states/pa/districts/house/49"
    rel: in-district
    area_weight: 0.0116
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Lancaster County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 557931 |
| Under 18 | 128950 |
| 18–64 | 319547 |
| 65+ | 109434 |
| Median household income | 86959 |
| Poverty rate | 8.19 |
| Homeownership rate | 69.82 |
| Unemployment rate | 3.37 |
| Median home value | 301100 |
| Gini index | 0.4301 |
| Vacancy rate | 2.95 |
| White | 455405 |
| Black | 22388 |
| Asian | 13540 |
| Native | 1162 |
| Hispanic/Latino | 64326 |
| Bachelor's or higher | 168247 |

## Districts

- [PA-11](/us/states/pa/districts/11.md) — 100% (congressional)
- [PA Senate District 13](/us/states/pa/districts/senate/13.md) — 55% (state senate)
- [PA Senate District 36](/us/states/pa/districts/senate/36.md) — 35% (state senate)
- [PA Senate District 48](/us/states/pa/districts/senate/48.md) — 10% (state senate)
- [PA House District 100](/us/states/pa/districts/house/100.md) — 31% (state house)
- [PA House District 37](/us/states/pa/districts/house/37.md) — 14% (state house)
- [PA House District 99](/us/states/pa/districts/house/99.md) — 14% (state house)
- [PA House District 97](/us/states/pa/districts/house/97.md) — 12% (state house)
- [PA House District 43](/us/states/pa/districts/house/43.md) — 10% (state house)
- [PA House District 98](/us/states/pa/districts/house/98.md) — 9% (state house)
- [PA House District 41](/us/states/pa/districts/house/41.md) — 5% (state house)
- [PA House District 96](/us/states/pa/districts/house/96.md) — 2% (state house)
- [PA House District 49](/us/states/pa/districts/house/49.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
