---
type: Jurisdiction
title: "Columbia County, WI"
classification: county
fips: "55021"
state: "WI"
demographics:
  population: 58272
  population_under_18: 11972
  population_18_64: 34878
  population_65_plus: 11422
  median_household_income: 85351
  poverty_rate: 7.75
  homeownership_rate: 76.66
  unemployment_rate: 3.06
  median_home_value: 283200
  gini_index: 0.4002
  vacancy_rate: 10.13
  race_white: 53053
  race_black: 1062
  race_asian: 466
  race_native: 313
  hispanic: 2385
  bachelors_plus: 14338
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/wi/districts/senate/14"
    rel: in-district
    area_weight: 0.8631
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.1368
  - to: "us/states/wi/districts/house/42"
    rel: in-district
    area_weight: 0.5055
  - to: "us/states/wi/districts/house/40"
    rel: in-district
    area_weight: 0.3269
  - to: "us/states/wi/districts/house/39"
    rel: in-district
    area_weight: 0.1364
  - to: "us/states/wi/districts/house/41"
    rel: in-district
    area_weight: 0.0307
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Columbia County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 58272 |
| Under 18 | 11972 |
| 18–64 | 34878 |
| 65+ | 11422 |
| Median household income | 85351 |
| Poverty rate | 7.75 |
| Homeownership rate | 76.66 |
| Unemployment rate | 3.06 |
| Median home value | 283200 |
| Gini index | 0.4002 |
| Vacancy rate | 10.13 |
| White | 53053 |
| Black | 1062 |
| Asian | 466 |
| Native | 313 |
| Hispanic/Latino | 2385 |
| Bachelor's or higher | 14338 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 100% (congressional)
- [WI Senate District 14](/us/states/wi/districts/senate/14.md) — 86% (state senate)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 14% (state senate)
- [WI House District 42](/us/states/wi/districts/house/42.md) — 51% (state house)
- [WI House District 40](/us/states/wi/districts/house/40.md) — 33% (state house)
- [WI House District 39](/us/states/wi/districts/house/39.md) — 14% (state house)
- [WI House District 41](/us/states/wi/districts/house/41.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
