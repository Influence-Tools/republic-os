---
type: Jurisdiction
title: "Brooke County, WV"
classification: county
fips: "54009"
state: "WV"
demographics:
  population: 21805
  population_under_18: 3741
  population_18_64: 12571
  population_65_plus: 5493
  median_household_income: 54316
  poverty_rate: 13.08
  homeownership_rate: 74.63
  unemployment_rate: 6.26
  median_home_value: 141500
  gini_index: 0.4369
  vacancy_rate: 9.5
  race_white: 20236
  race_black: 327
  race_asian: 144
  race_native: 7
  hispanic: 310
  bachelors_plus: 5155
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/senate/1"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/3"
    rel: in-district
    area_weight: 0.6387
  - to: "us/states/wv/districts/house/2"
    rel: in-district
    area_weight: 0.2643
  - to: "us/states/wv/districts/house/1"
    rel: in-district
    area_weight: 0.0966
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Brooke County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21805 |
| Under 18 | 3741 |
| 18–64 | 12571 |
| 65+ | 5493 |
| Median household income | 54316 |
| Poverty rate | 13.08 |
| Homeownership rate | 74.63 |
| Unemployment rate | 6.26 |
| Median home value | 141500 |
| Gini index | 0.4369 |
| Vacancy rate | 9.5 |
| White | 20236 |
| Black | 327 |
| Asian | 144 |
| Native | 7 |
| Hispanic/Latino | 310 |
| Bachelor's or higher | 5155 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 1](/us/states/wv/districts/senate/1.md) — 100% (state senate)
- [WV House District 3](/us/states/wv/districts/house/3.md) — 64% (state house)
- [WV House District 2](/us/states/wv/districts/house/2.md) — 26% (state house)
- [WV House District 1](/us/states/wv/districts/house/1.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
