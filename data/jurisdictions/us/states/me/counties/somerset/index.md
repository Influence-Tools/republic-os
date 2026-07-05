---
type: Jurisdiction
title: "Somerset County, ME"
classification: county
fips: "23025"
state: "ME"
demographics:
  population: 50959
  population_under_18: 9389
  population_18_64: 29847
  population_65_plus: 11723
  median_household_income: 58179
  poverty_rate: 14.19
  homeownership_rate: 77.42
  unemployment_rate: 3.5
  median_home_value: 166900
  gini_index: 0.4465
  vacancy_rate: 22.99
  race_white: 48140
  race_black: 249
  race_asian: 192
  race_native: 108
  hispanic: 787
  bachelors_plus: 10290
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/me/districts/senate/5"
    rel: in-district
    area_weight: 0.9096
  - to: "us/states/me/districts/senate/3"
    rel: in-district
    area_weight: 0.077
  - to: "us/states/me/districts/senate/16"
    rel: in-district
    area_weight: 0.0131
  - to: "us/states/me/districts/house/72"
    rel: in-district
    area_weight: 0.5975
  - to: "us/states/me/districts/house/73"
    rel: in-district
    area_weight: 0.2351
  - to: "us/states/me/districts/house/69"
    rel: in-district
    area_weight: 0.0469
  - to: "us/states/me/districts/house/71"
    rel: in-district
    area_weight: 0.0355
  - to: "us/states/me/districts/house/66"
    rel: in-district
    area_weight: 0.0203
  - to: "us/states/me/districts/house/70"
    rel: in-district
    area_weight: 0.0146
  - to: "us/states/me/districts/house/30"
    rel: in-district
    area_weight: 0.0145
  - to: "us/states/me/districts/house/67"
    rel: in-district
    area_weight: 0.0131
  - to: "us/states/me/districts/house/68"
    rel: in-district
    area_weight: 0.0117
  - to: "us/states/me/districts/house/74"
    rel: in-district
    area_weight: 0.0107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Somerset County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50959 |
| Under 18 | 9389 |
| 18–64 | 29847 |
| 65+ | 11723 |
| Median household income | 58179 |
| Poverty rate | 14.19 |
| Homeownership rate | 77.42 |
| Unemployment rate | 3.5 |
| Median home value | 166900 |
| Gini index | 0.4465 |
| Vacancy rate | 22.99 |
| White | 48140 |
| Black | 249 |
| Asian | 192 |
| Native | 108 |
| Hispanic/Latino | 787 |
| Bachelor's or higher | 10290 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 100% (congressional)
- [ME Senate District 5](/us/states/me/districts/senate/5.md) — 91% (state senate)
- [ME Senate District 3](/us/states/me/districts/senate/3.md) — 8% (state senate)
- [ME Senate District 16](/us/states/me/districts/senate/16.md) — 1% (state senate)
- [ME House District 72](/us/states/me/districts/house/72.md) — 60% (state house)
- [ME House District 73](/us/states/me/districts/house/73.md) — 24% (state house)
- [ME House District 69](/us/states/me/districts/house/69.md) — 5% (state house)
- [ME House District 71](/us/states/me/districts/house/71.md) — 4% (state house)
- [ME House District 66](/us/states/me/districts/house/66.md) — 2% (state house)
- [ME House District 70](/us/states/me/districts/house/70.md) — 1% (state house)
- [ME House District 30](/us/states/me/districts/house/30.md) — 1% (state house)
- [ME House District 67](/us/states/me/districts/house/67.md) — 1% (state house)
- [ME House District 68](/us/states/me/districts/house/68.md) — 1% (state house)
- [ME House District 74](/us/states/me/districts/house/74.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
