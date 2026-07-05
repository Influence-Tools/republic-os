---
type: Jurisdiction
title: "Cache County, UT"
classification: county
fips: "49005"
state: "UT"
demographics:
  population: 140046
  population_under_18: 40870
  population_18_64: 85179
  population_65_plus: 13997
  median_household_income: 81665
  poverty_rate: 11.95
  homeownership_rate: 63.66
  unemployment_rate: 2.59
  median_home_value: 444400
  gini_index: 0.4283
  vacancy_rate: 4.77
  race_white: 117444
  race_black: 1318
  race_asian: 2460
  race_native: 323
  hispanic: 16428
  bachelors_plus: 41982
districts:
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/2"
    rel: in-district
    area_weight: 0.6156
  - to: "us/states/ut/districts/senate/1"
    rel: in-district
    area_weight: 0.3843
  - to: "us/states/ut/districts/house/5"
    rel: in-district
    area_weight: 0.4331
  - to: "us/states/ut/districts/house/3"
    rel: in-district
    area_weight: 0.3547
  - to: "us/states/ut/districts/house/2"
    rel: in-district
    area_weight: 0.1385
  - to: "us/states/ut/districts/house/1"
    rel: in-district
    area_weight: 0.0736
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Cache County, UT

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 140046 |
| Under 18 | 40870 |
| 18–64 | 85179 |
| 65+ | 13997 |
| Median household income | 81665 |
| Poverty rate | 11.95 |
| Homeownership rate | 63.66 |
| Unemployment rate | 2.59 |
| Median home value | 444400 |
| Gini index | 0.4283 |
| Vacancy rate | 4.77 |
| White | 117444 |
| Black | 1318 |
| Asian | 2460 |
| Native | 323 |
| Hispanic/Latino | 16428 |
| Bachelor's or higher | 41982 |

## Districts

- [UT-01](/us/states/ut/districts/01.md) — 100% (congressional)
- [UT Senate District 2](/us/states/ut/districts/senate/2.md) — 62% (state senate)
- [UT Senate District 1](/us/states/ut/districts/senate/1.md) — 38% (state senate)
- [UT House District 5](/us/states/ut/districts/house/5.md) — 43% (state house)
- [UT House District 3](/us/states/ut/districts/house/3.md) — 35% (state house)
- [UT House District 2](/us/states/ut/districts/house/2.md) — 14% (state house)
- [UT House District 1](/us/states/ut/districts/house/1.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
