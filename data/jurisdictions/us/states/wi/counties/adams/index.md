---
type: Jurisdiction
title: "Adams County, WI"
classification: county
fips: "55001"
state: "WI"
demographics:
  population: 21123
  population_under_18: 2847
  population_18_64: 11473
  population_65_plus: 6803
  median_household_income: 59442
  poverty_rate: 14.13
  homeownership_rate: 86.24
  unemployment_rate: 4.52
  median_home_value: 200800
  gini_index: 0.4207
  vacancy_rate: 44.04
  race_white: 18788
  race_black: 429
  race_asian: 135
  race_native: 153
  hispanic: 933
  bachelors_plus: 3768
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.5352
  - to: "us/states/wi/districts/senate/14"
    rel: in-district
    area_weight: 0.2107
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.1498
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.1042
  - to: "us/states/wi/districts/house/72"
    rel: in-district
    area_weight: 0.4808
  - to: "us/states/wi/districts/house/41"
    rel: in-district
    area_weight: 0.2107
  - to: "us/states/wi/districts/house/39"
    rel: in-district
    area_weight: 0.1498
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.1042
  - to: "us/states/wi/districts/house/71"
    rel: in-district
    area_weight: 0.0544
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Adams County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21123 |
| Under 18 | 2847 |
| 18–64 | 11473 |
| 65+ | 6803 |
| Median household income | 59442 |
| Poverty rate | 14.13 |
| Homeownership rate | 86.24 |
| Unemployment rate | 4.52 |
| Median home value | 200800 |
| Gini index | 0.4207 |
| Vacancy rate | 44.04 |
| White | 18788 |
| Black | 429 |
| Asian | 135 |
| Native | 153 |
| Hispanic/Latino | 933 |
| Bachelor's or higher | 3768 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 54% (state senate)
- [WI Senate District 14](/us/states/wi/districts/senate/14.md) — 21% (state senate)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 15% (state senate)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 10% (state senate)
- [WI House District 72](/us/states/wi/districts/house/72.md) — 48% (state house)
- [WI House District 41](/us/states/wi/districts/house/41.md) — 21% (state house)
- [WI House District 39](/us/states/wi/districts/house/39.md) — 15% (state house)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 10% (state house)
- [WI House District 71](/us/states/wi/districts/house/71.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
