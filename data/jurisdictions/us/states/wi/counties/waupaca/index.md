---
type: Jurisdiction
title: "Waupaca County, WI"
classification: county
fips: "55135"
state: "WI"
demographics:
  population: 51569
  population_under_18: 10369
  population_18_64: 30233
  population_65_plus: 10967
  median_household_income: 72830
  poverty_rate: 10.4
  homeownership_rate: 75.32
  unemployment_rate: 2.78
  median_home_value: 211400
  gini_index: 0.4518
  vacancy_rate: 12.48
  race_white: 48037
  race_black: 285
  race_asian: 139
  race_native: 109
  hispanic: 2006
  bachelors_plus: 9852
districts:
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.5664
  - to: "us/states/wi/districts/senate/29"
    rel: in-district
    area_weight: 0.3336
  - to: "us/states/wi/districts/senate/2"
    rel: in-district
    area_weight: 0.1
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.424
  - to: "us/states/wi/districts/house/87"
    rel: in-district
    area_weight: 0.3336
  - to: "us/states/wi/districts/house/56"
    rel: in-district
    area_weight: 0.1425
  - to: "us/states/wi/districts/house/6"
    rel: in-district
    area_weight: 0.1
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Waupaca County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51569 |
| Under 18 | 10369 |
| 18–64 | 30233 |
| 65+ | 10967 |
| Median household income | 72830 |
| Poverty rate | 10.4 |
| Homeownership rate | 75.32 |
| Unemployment rate | 2.78 |
| Median home value | 211400 |
| Gini index | 0.4518 |
| Vacancy rate | 12.48 |
| White | 48037 |
| Black | 285 |
| Asian | 139 |
| Native | 109 |
| Hispanic/Latino | 2006 |
| Bachelor's or higher | 9852 |

## Districts

- [WI-08](/us/states/wi/districts/08.md) — 100% (congressional)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 57% (state senate)
- [WI Senate District 29](/us/states/wi/districts/senate/29.md) — 33% (state senate)
- [WI Senate District 2](/us/states/wi/districts/senate/2.md) — 10% (state senate)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 42% (state house)
- [WI House District 87](/us/states/wi/districts/house/87.md) — 33% (state house)
- [WI House District 56](/us/states/wi/districts/house/56.md) — 14% (state house)
- [WI House District 6](/us/states/wi/districts/house/6.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
