---
type: Jurisdiction
title: "Whiteside County, IL"
classification: county
fips: "17195"
state: "IL"
demographics:
  population: 54947
  population_under_18: 12065
  population_18_64: 30915
  population_65_plus: 11967
  median_household_income: 67500
  poverty_rate: 11.98
  homeownership_rate: 76.93
  unemployment_rate: 4.35
  median_home_value: 127100
  gini_index: 0.4389
  vacancy_rate: 10.52
  race_white: 46769
  race_black: 691
  race_asian: 291
  race_native: 206
  hispanic: 7319
  bachelors_plus: 10881
districts:
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.6734
  - to: "us/states/il/districts/house/74"
    rel: in-district
    area_weight: 0.3265
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Whiteside County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54947 |
| Under 18 | 12065 |
| 18–64 | 30915 |
| 65+ | 11967 |
| Median household income | 67500 |
| Poverty rate | 11.98 |
| Homeownership rate | 76.93 |
| Unemployment rate | 4.35 |
| Median home value | 127100 |
| Gini index | 0.4389 |
| Vacancy rate | 10.52 |
| White | 46769 |
| Black | 691 |
| Asian | 291 |
| Native | 206 |
| Hispanic/Latino | 7319 |
| Bachelor's or higher | 10881 |

## Districts

- [IL-17](/us/states/il/districts/17.md) — 100% (congressional)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 100% (state senate)
- [IL House District 73](/us/states/il/districts/house/73.md) — 67% (state house)
- [IL House District 74](/us/states/il/districts/house/74.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
