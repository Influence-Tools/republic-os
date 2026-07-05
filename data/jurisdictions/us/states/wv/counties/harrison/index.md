---
type: Jurisdiction
title: "Harrison County, WV"
classification: county
fips: "54033"
state: "WV"
demographics:
  population: 64984
  population_under_18: 13769
  population_18_64: 37993
  population_65_plus: 13222
  median_household_income: 60377
  poverty_rate: 14.36
  homeownership_rate: 73.57
  unemployment_rate: 4.0
  median_home_value: 166200
  gini_index: 0.4639
  vacancy_rate: 13.7
  race_white: 60111
  race_black: 974
  race_asian: 553
  race_native: 77
  hispanic: 1472
  bachelors_plus: 17457
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/12"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/69"
    rel: in-district
    area_weight: 0.5097
  - to: "us/states/wv/districts/house/72"
    rel: in-district
    area_weight: 0.3555
  - to: "us/states/wv/districts/house/71"
    rel: in-district
    area_weight: 0.1142
  - to: "us/states/wv/districts/house/70"
    rel: in-district
    area_weight: 0.0202
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Harrison County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64984 |
| Under 18 | 13769 |
| 18–64 | 37993 |
| 65+ | 13222 |
| Median household income | 60377 |
| Poverty rate | 14.36 |
| Homeownership rate | 73.57 |
| Unemployment rate | 4.0 |
| Median home value | 166200 |
| Gini index | 0.4639 |
| Vacancy rate | 13.7 |
| White | 60111 |
| Black | 974 |
| Asian | 553 |
| Native | 77 |
| Hispanic/Latino | 1472 |
| Bachelor's or higher | 17457 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 12](/us/states/wv/districts/senate/12.md) — 100% (state senate)
- [WV House District 69](/us/states/wv/districts/house/69.md) — 51% (state house)
- [WV House District 72](/us/states/wv/districts/house/72.md) — 36% (state house)
- [WV House District 71](/us/states/wv/districts/house/71.md) — 11% (state house)
- [WV House District 70](/us/states/wv/districts/house/70.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
