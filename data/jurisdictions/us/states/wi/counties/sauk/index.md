---
type: Jurisdiction
title: "Sauk County, WI"
classification: county
fips: "55111"
state: "WI"
demographics:
  population: 66009
  population_under_18: 14752
  population_18_64: 38117
  population_65_plus: 13140
  median_household_income: 79541
  poverty_rate: 8.06
  homeownership_rate: 72.36
  unemployment_rate: 2.32
  median_home_value: 258600
  gini_index: 0.4099
  vacancy_rate: 11.14
  race_white: 57628
  race_black: 517
  race_asian: 296
  race_native: 381
  hispanic: 4488
  bachelors_plus: 16555
districts:
  - to: "us/states/wi/districts/02"
    rel: in-district
    area_weight: 0.8765
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.1225
  - to: "us/states/wi/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/40"
    rel: in-district
    area_weight: 0.5322
  - to: "us/states/wi/districts/house/41"
    rel: in-district
    area_weight: 0.4677
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Sauk County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66009 |
| Under 18 | 14752 |
| 18–64 | 38117 |
| 65+ | 13140 |
| Median household income | 79541 |
| Poverty rate | 8.06 |
| Homeownership rate | 72.36 |
| Unemployment rate | 2.32 |
| Median home value | 258600 |
| Gini index | 0.4099 |
| Vacancy rate | 11.14 |
| White | 57628 |
| Black | 517 |
| Asian | 296 |
| Native | 381 |
| Hispanic/Latino | 4488 |
| Bachelor's or higher | 16555 |

## Districts

- [WI-02](/us/states/wi/districts/02.md) — 88% (congressional)
- [WI-03](/us/states/wi/districts/03.md) — 12% (congressional)
- [WI Senate District 14](/us/states/wi/districts/senate/14.md) — 100% (state senate)
- [WI House District 40](/us/states/wi/districts/house/40.md) — 53% (state house)
- [WI House District 41](/us/states/wi/districts/house/41.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
