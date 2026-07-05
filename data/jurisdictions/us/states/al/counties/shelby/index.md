---
type: Jurisdiction
title: "Shelby County, AL"
classification: county
fips: "01117"
state: "AL"
demographics:
  population: 235969
  population_under_18: 58029
  population_18_64: 75546
  population_65_plus: 102394
  median_household_income: 102265
  poverty_rate: 6.34
  homeownership_rate: 80.99
  unemployment_rate: 2.74
  median_home_value: 349200
  gini_index: 0.4183
  vacancy_rate: 3.93
  race_white: 175573
  race_black: 33652
  race_asian: 5294
  race_native: 752
  hispanic: 18735
  bachelors_plus: 108456
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/al/districts/senate/15"
    rel: in-district
    area_weight: 0.3785
  - to: "us/states/al/districts/senate/11"
    rel: in-district
    area_weight: 0.2895
  - to: "us/states/al/districts/senate/14"
    rel: in-district
    area_weight: 0.2821
  - to: "us/states/al/districts/senate/16"
    rel: in-district
    area_weight: 0.0499
  - to: "us/states/al/districts/house/41"
    rel: in-district
    area_weight: 0.548
  - to: "us/states/al/districts/house/49"
    rel: in-district
    area_weight: 0.1703
  - to: "us/states/al/districts/house/45"
    rel: in-district
    area_weight: 0.1235
  - to: "us/states/al/districts/house/43"
    rel: in-district
    area_weight: 0.0653
  - to: "us/states/al/districts/house/73"
    rel: in-district
    area_weight: 0.0637
  - to: "us/states/al/districts/house/15"
    rel: in-district
    area_weight: 0.0149
  - to: "us/states/al/districts/house/48"
    rel: in-district
    area_weight: 0.0143
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Shelby County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 235969 |
| Under 18 | 58029 |
| 18–64 | 75546 |
| 65+ | 102394 |
| Median household income | 102265 |
| Poverty rate | 6.34 |
| Homeownership rate | 80.99 |
| Unemployment rate | 2.74 |
| Median home value | 349200 |
| Gini index | 0.4183 |
| Vacancy rate | 3.93 |
| White | 175573 |
| Black | 33652 |
| Asian | 5294 |
| Native | 752 |
| Hispanic/Latino | 18735 |
| Bachelor's or higher | 108456 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 100% (congressional)
- [AL Senate District 15](/us/states/al/districts/senate/15.md) — 38% (state senate)
- [AL Senate District 11](/us/states/al/districts/senate/11.md) — 29% (state senate)
- [AL Senate District 14](/us/states/al/districts/senate/14.md) — 28% (state senate)
- [AL Senate District 16](/us/states/al/districts/senate/16.md) — 5% (state senate)
- [AL House District 41](/us/states/al/districts/house/41.md) — 55% (state house)
- [AL House District 49](/us/states/al/districts/house/49.md) — 17% (state house)
- [AL House District 45](/us/states/al/districts/house/45.md) — 12% (state house)
- [AL House District 43](/us/states/al/districts/house/43.md) — 7% (state house)
- [AL House District 73](/us/states/al/districts/house/73.md) — 6% (state house)
- [AL House District 15](/us/states/al/districts/house/15.md) — 1% (state house)
- [AL House District 48](/us/states/al/districts/house/48.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
