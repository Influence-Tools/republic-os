---
type: Jurisdiction
title: "McHenry County, IL"
classification: county
fips: "17111"
state: "IL"
demographics:
  population: 312591
  population_under_18: 71089
  population_18_64: 189990
  population_65_plus: 51512
  median_household_income: 104802
  poverty_rate: 6.23
  homeownership_rate: 82.71
  unemployment_rate: 4.69
  median_home_value: 308100
  gini_index: 0.4162
  vacancy_rate: 3.08
  race_white: 248630
  race_black: 4755
  race_asian: 9760
  race_native: 1185
  hispanic: 50243
  bachelors_plus: 102254
districts:
  - to: "us/states/il/districts/11"
    rel: in-district
    area_weight: 0.4848
  - to: "us/states/il/districts/10"
    rel: in-district
    area_weight: 0.2194
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.2172
  - to: "us/states/il/districts/09"
    rel: in-district
    area_weight: 0.0785
  - to: "us/states/il/districts/senate/35"
    rel: in-district
    area_weight: 0.6214
  - to: "us/states/il/districts/senate/32"
    rel: in-district
    area_weight: 0.3251
  - to: "us/states/il/districts/senate/26"
    rel: in-district
    area_weight: 0.0271
  - to: "us/states/il/districts/senate/33"
    rel: in-district
    area_weight: 0.0262
  - to: "us/states/il/districts/house/69"
    rel: in-district
    area_weight: 0.6117
  - to: "us/states/il/districts/house/63"
    rel: in-district
    area_weight: 0.2075
  - to: "us/states/il/districts/house/64"
    rel: in-district
    area_weight: 0.1176
  - to: "us/states/il/districts/house/52"
    rel: in-district
    area_weight: 0.0271
  - to: "us/states/il/districts/house/66"
    rel: in-district
    area_weight: 0.0262
  - to: "us/states/il/districts/house/70"
    rel: in-district
    area_weight: 0.0097
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# McHenry County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 312591 |
| Under 18 | 71089 |
| 18–64 | 189990 |
| 65+ | 51512 |
| Median household income | 104802 |
| Poverty rate | 6.23 |
| Homeownership rate | 82.71 |
| Unemployment rate | 4.69 |
| Median home value | 308100 |
| Gini index | 0.4162 |
| Vacancy rate | 3.08 |
| White | 248630 |
| Black | 4755 |
| Asian | 9760 |
| Native | 1185 |
| Hispanic/Latino | 50243 |
| Bachelor's or higher | 102254 |

## Districts

- [IL-11](/us/states/il/districts/11.md) — 48% (congressional)
- [IL-10](/us/states/il/districts/10.md) — 22% (congressional)
- [IL-16](/us/states/il/districts/16.md) — 22% (congressional)
- [IL-09](/us/states/il/districts/09.md) — 8% (congressional)
- [IL Senate District 35](/us/states/il/districts/senate/35.md) — 62% (state senate)
- [IL Senate District 32](/us/states/il/districts/senate/32.md) — 33% (state senate)
- [IL Senate District 26](/us/states/il/districts/senate/26.md) — 3% (state senate)
- [IL Senate District 33](/us/states/il/districts/senate/33.md) — 3% (state senate)
- [IL House District 69](/us/states/il/districts/house/69.md) — 61% (state house)
- [IL House District 63](/us/states/il/districts/house/63.md) — 21% (state house)
- [IL House District 64](/us/states/il/districts/house/64.md) — 12% (state house)
- [IL House District 52](/us/states/il/districts/house/52.md) — 3% (state house)
- [IL House District 66](/us/states/il/districts/house/66.md) — 3% (state house)
- [IL House District 70](/us/states/il/districts/house/70.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
