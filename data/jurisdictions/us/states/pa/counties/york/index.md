---
type: Jurisdiction
title: "York County, PA"
classification: county
fips: "42133"
state: "PA"
demographics:
  population: 462924
  population_under_18: 101294
  population_18_64: 274517
  population_65_plus: 87113
  median_household_income: 84829
  poverty_rate: 8.36
  homeownership_rate: 76.34
  unemployment_rate: 4.49
  median_home_value: 248600
  gini_index: 0.4122
  vacancy_rate: 4.36
  race_white: 375793
  race_black: 29054
  race_asian: 6866
  race_native: 644
  hispanic: 44412
  bachelors_plus: 123557
districts:
  - to: "us/states/pa/districts/11"
    rel: in-district
    area_weight: 0.6137
  - to: "us/states/pa/districts/10"
    rel: in-district
    area_weight: 0.384
  - to: "us/states/pa/districts/senate/28"
    rel: in-district
    area_weight: 0.662
  - to: "us/states/pa/districts/senate/31"
    rel: in-district
    area_weight: 0.3377
  - to: "us/states/pa/districts/house/92"
    rel: in-district
    area_weight: 0.2241
  - to: "us/states/pa/districts/house/94"
    rel: in-district
    area_weight: 0.1982
  - to: "us/states/pa/districts/house/93"
    rel: in-district
    area_weight: 0.172
  - to: "us/states/pa/districts/house/196"
    rel: in-district
    area_weight: 0.1434
  - to: "us/states/pa/districts/house/169"
    rel: in-district
    area_weight: 0.1381
  - to: "us/states/pa/districts/house/47"
    rel: in-district
    area_weight: 0.1096
  - to: "us/states/pa/districts/house/95"
    rel: in-district
    area_weight: 0.0142
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# York County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 462924 |
| Under 18 | 101294 |
| 18–64 | 274517 |
| 65+ | 87113 |
| Median household income | 84829 |
| Poverty rate | 8.36 |
| Homeownership rate | 76.34 |
| Unemployment rate | 4.49 |
| Median home value | 248600 |
| Gini index | 0.4122 |
| Vacancy rate | 4.36 |
| White | 375793 |
| Black | 29054 |
| Asian | 6866 |
| Native | 644 |
| Hispanic/Latino | 44412 |
| Bachelor's or higher | 123557 |

## Districts

- [PA-11](/us/states/pa/districts/11.md) — 61% (congressional)
- [PA-10](/us/states/pa/districts/10.md) — 38% (congressional)
- [PA Senate District 28](/us/states/pa/districts/senate/28.md) — 66% (state senate)
- [PA Senate District 31](/us/states/pa/districts/senate/31.md) — 34% (state senate)
- [PA House District 92](/us/states/pa/districts/house/92.md) — 22% (state house)
- [PA House District 94](/us/states/pa/districts/house/94.md) — 20% (state house)
- [PA House District 93](/us/states/pa/districts/house/93.md) — 17% (state house)
- [PA House District 196](/us/states/pa/districts/house/196.md) — 14% (state house)
- [PA House District 169](/us/states/pa/districts/house/169.md) — 14% (state house)
- [PA House District 47](/us/states/pa/districts/house/47.md) — 11% (state house)
- [PA House District 95](/us/states/pa/districts/house/95.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
