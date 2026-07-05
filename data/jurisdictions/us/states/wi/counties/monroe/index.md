---
type: Jurisdiction
title: "Monroe County, WI"
classification: county
fips: "55081"
state: "WI"
demographics:
  population: 46208
  population_under_18: 11724
  population_18_64: 26164
  population_65_plus: 8320
  median_household_income: 69467
  poverty_rate: 11.73
  homeownership_rate: 72.76
  unemployment_rate: 3.19
  median_home_value: 210000
  gini_index: 0.4193
  vacancy_rate: 8.6
  race_white: 41596
  race_black: 701
  race_asian: 423
  race_native: 395
  hispanic: 2664
  bachelors_plus: 8719
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.8466
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.1534
  - to: "us/states/wi/districts/senate/24"
    rel: in-district
    area_weight: 0.6656
  - to: "us/states/wi/districts/senate/32"
    rel: in-district
    area_weight: 0.3344
  - to: "us/states/wi/districts/house/70"
    rel: in-district
    area_weight: 0.6655
  - to: "us/states/wi/districts/house/95"
    rel: in-district
    area_weight: 0.3344
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Monroe County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46208 |
| Under 18 | 11724 |
| 18–64 | 26164 |
| 65+ | 8320 |
| Median household income | 69467 |
| Poverty rate | 11.73 |
| Homeownership rate | 72.76 |
| Unemployment rate | 3.19 |
| Median home value | 210000 |
| Gini index | 0.4193 |
| Vacancy rate | 8.6 |
| White | 41596 |
| Black | 701 |
| Asian | 423 |
| Native | 395 |
| Hispanic/Latino | 2664 |
| Bachelor's or higher | 8719 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 85% (congressional)
- [WI-07](/us/states/wi/districts/07.md) — 15% (congressional)
- [WI Senate District 24](/us/states/wi/districts/senate/24.md) — 67% (state senate)
- [WI Senate District 32](/us/states/wi/districts/senate/32.md) — 33% (state senate)
- [WI House District 70](/us/states/wi/districts/house/70.md) — 67% (state house)
- [WI House District 95](/us/states/wi/districts/house/95.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
