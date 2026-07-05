---
type: Jurisdiction
title: "Knox County, TN"
classification: county
fips: "47093"
state: "TN"
demographics:
  population: 494148
  population_under_18: 103518
  population_18_64: 310238
  population_65_plus: 80392
  median_household_income: 74222
  poverty_rate: 12.2
  homeownership_rate: 65.18
  unemployment_rate: 3.52
  median_home_value: 320900
  gini_index: 0.4798
  vacancy_rate: 8.01
  race_white: 395602
  race_black: 39839
  race_asian: 11422
  race_native: 747
  hispanic: 31276
  bachelors_plus: 189644
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.9956
  - to: "us/states/tn/districts/senate/6"
    rel: in-district
    area_weight: 0.6261
  - to: "us/states/tn/districts/senate/7"
    rel: in-district
    area_weight: 0.2587
  - to: "us/states/tn/districts/senate/5"
    rel: in-district
    area_weight: 0.1149
  - to: "us/states/tn/districts/house/19"
    rel: in-district
    area_weight: 0.4187
  - to: "us/states/tn/districts/house/89"
    rel: in-district
    area_weight: 0.1275
  - to: "us/states/tn/districts/house/18"
    rel: in-district
    area_weight: 0.1272
  - to: "us/states/tn/districts/house/16"
    rel: in-district
    area_weight: 0.1107
  - to: "us/states/tn/districts/house/14"
    rel: in-district
    area_weight: 0.1048
  - to: "us/states/tn/districts/house/15"
    rel: in-district
    area_weight: 0.0578
  - to: "us/states/tn/districts/house/90"
    rel: in-district
    area_weight: 0.0529
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Knox County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 494148 |
| Under 18 | 103518 |
| 18–64 | 310238 |
| 65+ | 80392 |
| Median household income | 74222 |
| Poverty rate | 12.2 |
| Homeownership rate | 65.18 |
| Unemployment rate | 3.52 |
| Median home value | 320900 |
| Gini index | 0.4798 |
| Vacancy rate | 8.01 |
| White | 395602 |
| Black | 39839 |
| Asian | 11422 |
| Native | 747 |
| Hispanic/Latino | 31276 |
| Bachelor's or higher | 189644 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 100% (congressional)
- [TN Senate District 6](/us/states/tn/districts/senate/6.md) — 63% (state senate)
- [TN Senate District 7](/us/states/tn/districts/senate/7.md) — 26% (state senate)
- [TN Senate District 5](/us/states/tn/districts/senate/5.md) — 11% (state senate)
- [TN House District 19](/us/states/tn/districts/house/19.md) — 42% (state house)
- [TN House District 89](/us/states/tn/districts/house/89.md) — 13% (state house)
- [TN House District 18](/us/states/tn/districts/house/18.md) — 13% (state house)
- [TN House District 16](/us/states/tn/districts/house/16.md) — 11% (state house)
- [TN House District 14](/us/states/tn/districts/house/14.md) — 10% (state house)
- [TN House District 15](/us/states/tn/districts/house/15.md) — 6% (state house)
- [TN House District 90](/us/states/tn/districts/house/90.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
