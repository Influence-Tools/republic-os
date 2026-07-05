---
type: Jurisdiction
title: "Aroostook County, ME"
classification: county
fips: "23003"
state: "ME"
demographics:
  population: 67058
  population_under_18: 12509
  population_18_64: 37337
  population_65_plus: 17212
  median_household_income: 56700
  poverty_rate: 14.4
  homeownership_rate: 74.52
  unemployment_rate: 5.26
  median_home_value: 149700
  gini_index: 0.4646
  vacancy_rate: 22.15
  race_white: 62391
  race_black: 508
  race_asian: 239
  race_native: 847
  hispanic: 1148
  bachelors_plus: 15466
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/me/districts/senate/1"
    rel: in-district
    area_weight: 0.6809
  - to: "us/states/me/districts/senate/2"
    rel: in-district
    area_weight: 0.3189
  - to: "us/states/me/districts/house/1"
    rel: in-district
    area_weight: 0.4885
  - to: "us/states/me/districts/house/6"
    rel: in-district
    area_weight: 0.1677
  - to: "us/states/me/districts/house/8"
    rel: in-district
    area_weight: 0.127
  - to: "us/states/me/districts/house/2"
    rel: in-district
    area_weight: 0.0947
  - to: "us/states/me/districts/house/3"
    rel: in-district
    area_weight: 0.065
  - to: "us/states/me/districts/house/7"
    rel: in-district
    area_weight: 0.0231
  - to: "us/states/me/districts/house/4"
    rel: in-district
    area_weight: 0.0222
  - to: "us/states/me/districts/house/5"
    rel: in-district
    area_weight: 0.0114
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Aroostook County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67058 |
| Under 18 | 12509 |
| 18–64 | 37337 |
| 65+ | 17212 |
| Median household income | 56700 |
| Poverty rate | 14.4 |
| Homeownership rate | 74.52 |
| Unemployment rate | 5.26 |
| Median home value | 149700 |
| Gini index | 0.4646 |
| Vacancy rate | 22.15 |
| White | 62391 |
| Black | 508 |
| Asian | 239 |
| Native | 847 |
| Hispanic/Latino | 1148 |
| Bachelor's or higher | 15466 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 100% (congressional)
- [ME Senate District 1](/us/states/me/districts/senate/1.md) — 68% (state senate)
- [ME Senate District 2](/us/states/me/districts/senate/2.md) — 32% (state senate)
- [ME House District 1](/us/states/me/districts/house/1.md) — 49% (state house)
- [ME House District 6](/us/states/me/districts/house/6.md) — 17% (state house)
- [ME House District 8](/us/states/me/districts/house/8.md) — 13% (state house)
- [ME House District 2](/us/states/me/districts/house/2.md) — 9% (state house)
- [ME House District 3](/us/states/me/districts/house/3.md) — 6% (state house)
- [ME House District 7](/us/states/me/districts/house/7.md) — 2% (state house)
- [ME House District 4](/us/states/me/districts/house/4.md) — 2% (state house)
- [ME House District 5](/us/states/me/districts/house/5.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
