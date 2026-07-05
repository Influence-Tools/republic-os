---
type: Jurisdiction
title: "Dunn County, WI"
classification: county
fips: "55033"
state: "WI"
demographics:
  population: 45527
  population_under_18: 8776
  population_18_64: 29028
  population_65_plus: 7723
  median_household_income: 74824
  poverty_rate: 10.68
  homeownership_rate: 67.05
  unemployment_rate: 4.39
  median_home_value: 243200
  gini_index: 0.4207
  vacancy_rate: 8.13
  race_white: 41442
  race_black: 400
  race_asian: 1405
  race_native: 49
  hispanic: 1124
  bachelors_plus: 11505
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 0.4601
  - to: "us/states/wi/districts/senate/31"
    rel: in-district
    area_weight: 0.3509
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.189
  - to: "us/states/wi/districts/house/67"
    rel: in-district
    area_weight: 0.4601
  - to: "us/states/wi/districts/house/93"
    rel: in-district
    area_weight: 0.1965
  - to: "us/states/wi/districts/house/28"
    rel: in-district
    area_weight: 0.189
  - to: "us/states/wi/districts/house/92"
    rel: in-district
    area_weight: 0.1544
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Dunn County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45527 |
| Under 18 | 8776 |
| 18–64 | 29028 |
| 65+ | 7723 |
| Median household income | 74824 |
| Poverty rate | 10.68 |
| Homeownership rate | 67.05 |
| Unemployment rate | 4.39 |
| Median home value | 243200 |
| Gini index | 0.4207 |
| Vacancy rate | 8.13 |
| White | 41442 |
| Black | 400 |
| Asian | 1405 |
| Native | 49 |
| Hispanic/Latino | 1124 |
| Bachelor's or higher | 11505 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 46% (state senate)
- [WI Senate District 31](/us/states/wi/districts/senate/31.md) — 35% (state senate)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 19% (state senate)
- [WI House District 67](/us/states/wi/districts/house/67.md) — 46% (state house)
- [WI House District 93](/us/states/wi/districts/house/93.md) — 20% (state house)
- [WI House District 28](/us/states/wi/districts/house/28.md) — 19% (state house)
- [WI House District 92](/us/states/wi/districts/house/92.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
