---
type: Jurisdiction
title: "La Crosse County, WI"
classification: county
fips: "55063"
state: "WI"
demographics:
  population: 120488
  population_under_18: 23330
  population_18_64: 75374
  population_65_plus: 21784
  median_household_income: 73013
  poverty_rate: 12.39
  homeownership_rate: 62.16
  unemployment_rate: 3.14
  median_home_value: 257000
  gini_index: 0.4472
  vacancy_rate: 4.65
  race_white: 106232
  race_black: 1819
  race_asian: 5423
  race_native: 426
  hispanic: 3269
  bachelors_plus: 39972
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/house/94"
    rel: in-district
    area_weight: 0.4964
  - to: "us/states/wi/districts/house/95"
    rel: in-district
    area_weight: 0.3672
  - to: "us/states/wi/districts/house/96"
    rel: in-district
    area_weight: 0.1363
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# La Crosse County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 120488 |
| Under 18 | 23330 |
| 18–64 | 75374 |
| 65+ | 21784 |
| Median household income | 73013 |
| Poverty rate | 12.39 |
| Homeownership rate | 62.16 |
| Unemployment rate | 3.14 |
| Median home value | 257000 |
| Gini index | 0.4472 |
| Vacancy rate | 4.65 |
| White | 106232 |
| Black | 1819 |
| Asian | 5423 |
| Native | 426 |
| Hispanic/Latino | 3269 |
| Bachelor's or higher | 39972 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 32](/us/states/wi/districts/senate/32.md) — 100% (state senate)
- [WI House District 94](/us/states/wi/districts/house/94.md) — 50% (state house)
- [WI House District 95](/us/states/wi/districts/house/95.md) — 37% (state house)
- [WI House District 96](/us/states/wi/districts/house/96.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
