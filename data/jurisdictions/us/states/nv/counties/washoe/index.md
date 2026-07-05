---
type: Jurisdiction
title: "Washoe County, NV"
classification: county
fips: "32031"
state: "NV"
demographics:
  population: 497200
  population_under_18: 102934
  population_18_64: 306256
  population_65_plus: 88010
  median_household_income: 88096
  poverty_rate: 10.65
  homeownership_rate: 59.87
  unemployment_rate: 5.13
  median_home_value: 539900
  gini_index: 0.4711
  vacancy_rate: 8.65
  race_white: 311168
  race_black: 11837
  race_asian: 28668
  race_native: 6690
  hispanic: 129643
  bachelors_plus: 166909
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nv/districts/senate/14"
    rel: in-district
    area_weight: 0.9311
  - to: "us/states/nv/districts/senate/16"
    rel: in-district
    area_weight: 0.0521
  - to: "us/states/nv/districts/senate/15"
    rel: in-district
    area_weight: 0.0113
  - to: "us/states/nv/districts/senate/13"
    rel: in-district
    area_weight: 0.0053
  - to: "us/states/nv/districts/house/32"
    rel: in-district
    area_weight: 0.9175
  - to: "us/states/nv/districts/house/26"
    rel: in-district
    area_weight: 0.0394
  - to: "us/states/nv/districts/house/31"
    rel: in-district
    area_weight: 0.0136
  - to: "us/states/nv/districts/house/40"
    rel: in-district
    area_weight: 0.0127
  - to: "us/states/nv/districts/house/27"
    rel: in-district
    area_weight: 0.0066
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Washoe County, NV

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 497200 |
| Under 18 | 102934 |
| 18–64 | 306256 |
| 65+ | 88010 |
| Median household income | 88096 |
| Poverty rate | 10.65 |
| Homeownership rate | 59.87 |
| Unemployment rate | 5.13 |
| Median home value | 539900 |
| Gini index | 0.4711 |
| Vacancy rate | 8.65 |
| White | 311168 |
| Black | 11837 |
| Asian | 28668 |
| Native | 6690 |
| Hispanic/Latino | 129643 |
| Bachelor's or higher | 166909 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 100% (congressional)
- [NV Senate District 14](/us/states/nv/districts/senate/14.md) — 93% (state senate)
- [NV Senate District 16](/us/states/nv/districts/senate/16.md) — 5% (state senate)
- [NV Senate District 15](/us/states/nv/districts/senate/15.md) — 1% (state senate)
- [NV Senate District 13](/us/states/nv/districts/senate/13.md) — 1% (state senate)
- [NV House District 32](/us/states/nv/districts/house/32.md) — 92% (state house)
- [NV House District 26](/us/states/nv/districts/house/26.md) — 4% (state house)
- [NV House District 31](/us/states/nv/districts/house/31.md) — 1% (state house)
- [NV House District 40](/us/states/nv/districts/house/40.md) — 1% (state house)
- [NV House District 27](/us/states/nv/districts/house/27.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
