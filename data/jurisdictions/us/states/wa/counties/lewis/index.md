---
type: Jurisdiction
title: "Lewis County, WA"
classification: county
fips: "53041"
state: "WA"
demographics:
  population: 85154
  population_under_18: 18423
  population_18_64: 48520
  population_65_plus: 18211
  median_household_income: 74796
  poverty_rate: 12.22
  homeownership_rate: 75.76
  unemployment_rate: 5.33
  median_home_value: 385800
  gini_index: 0.4243
  vacancy_rate: 9.85
  race_white: 70016
  race_black: 713
  race_asian: 1011
  race_native: 1203
  hispanic: 9810
  bachelors_plus: 17522
districts:
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/wa/districts/senate/20"
    rel: in-district
    area_weight: 0.7693
  - to: "us/states/wa/districts/senate/19"
    rel: in-district
    area_weight: 0.2305
  - to: "us/states/wa/districts/house/20"
    rel: in-district
    area_weight: 0.7693
  - to: "us/states/wa/districts/house/19"
    rel: in-district
    area_weight: 0.2305
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Lewis County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 85154 |
| Under 18 | 18423 |
| 18–64 | 48520 |
| 65+ | 18211 |
| Median household income | 74796 |
| Poverty rate | 12.22 |
| Homeownership rate | 75.76 |
| Unemployment rate | 5.33 |
| Median home value | 385800 |
| Gini index | 0.4243 |
| Vacancy rate | 9.85 |
| White | 70016 |
| Black | 713 |
| Asian | 1011 |
| Native | 1203 |
| Hispanic/Latino | 9810 |
| Bachelor's or higher | 17522 |

## Districts

- [WA-03](/us/states/wa/districts/03.md) — 100% (congressional)
- [WA Senate District 20](/us/states/wa/districts/senate/20.md) — 77% (state senate)
- [WA Senate District 19](/us/states/wa/districts/senate/19.md) — 23% (state senate)
- [WA House District 20](/us/states/wa/districts/house/20.md) — 77% (state house)
- [WA House District 19](/us/states/wa/districts/house/19.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
