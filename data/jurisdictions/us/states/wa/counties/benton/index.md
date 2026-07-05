---
type: Jurisdiction
title: "Benton County, WA"
classification: county
fips: "53005"
state: "WA"
demographics:
  population: 212905
  population_under_18: 55579
  population_18_64: 123530
  population_65_plus: 33796
  median_household_income: 89874
  poverty_rate: 10.99
  homeownership_rate: 67.63
  unemployment_rate: 5.32
  median_home_value: 407800
  gini_index: 0.4378
  vacancy_rate: 6.08
  race_white: 148319
  race_black: 3542
  race_asian: 6663
  race_native: 2237
  hispanic: 54546
  bachelors_plus: 64110
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/wa/districts/senate/16"
    rel: in-district
    area_weight: 0.3543
  - to: "us/states/wa/districts/senate/8"
    rel: in-district
    area_weight: 0.2886
  - to: "us/states/wa/districts/senate/14"
    rel: in-district
    area_weight: 0.2461
  - to: "us/states/wa/districts/senate/15"
    rel: in-district
    area_weight: 0.111
  - to: "us/states/wa/districts/house/16"
    rel: in-district
    area_weight: 0.3543
  - to: "us/states/wa/districts/house/8"
    rel: in-district
    area_weight: 0.2886
  - to: "us/states/wa/districts/house/14"
    rel: in-district
    area_weight: 0.2461
  - to: "us/states/wa/districts/house/15"
    rel: in-district
    area_weight: 0.111
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Benton County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 212905 |
| Under 18 | 55579 |
| 18–64 | 123530 |
| 65+ | 33796 |
| Median household income | 89874 |
| Poverty rate | 10.99 |
| Homeownership rate | 67.63 |
| Unemployment rate | 5.32 |
| Median home value | 407800 |
| Gini index | 0.4378 |
| Vacancy rate | 6.08 |
| White | 148319 |
| Black | 3542 |
| Asian | 6663 |
| Native | 2237 |
| Hispanic/Latino | 54546 |
| Bachelor's or higher | 64110 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 16](/us/states/wa/districts/senate/16.md) — 35% (state senate)
- [WA Senate District 8](/us/states/wa/districts/senate/8.md) — 29% (state senate)
- [WA Senate District 14](/us/states/wa/districts/senate/14.md) — 25% (state senate)
- [WA Senate District 15](/us/states/wa/districts/senate/15.md) — 11% (state senate)
- [WA House District 16](/us/states/wa/districts/house/16.md) — 35% (state house)
- [WA House District 8](/us/states/wa/districts/house/8.md) — 29% (state house)
- [WA House District 14](/us/states/wa/districts/house/14.md) — 25% (state house)
- [WA House District 15](/us/states/wa/districts/house/15.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
