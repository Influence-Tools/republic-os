---
type: Jurisdiction
title: "Spokane County, WA"
classification: county
fips: "53063"
state: "WA"
demographics:
  population: 549056
  population_under_18: 118285
  population_18_64: 335244
  population_65_plus: 95527
  median_household_income: 78582
  poverty_rate: 11.68
  homeownership_rate: 64.48
  unemployment_rate: 5.33
  median_home_value: 410700
  gini_index: 0.4514
  vacancy_rate: 5.54
  race_white: 454089
  race_black: 11408
  race_asian: 12568
  race_native: 5459
  hispanic: 38877
  bachelors_plus: 172788
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.4828
  - to: "us/states/wa/districts/senate/6"
    rel: in-district
    area_weight: 0.2329
  - to: "us/states/wa/districts/senate/4"
    rel: in-district
    area_weight: 0.2247
  - to: "us/states/wa/districts/senate/7"
    rel: in-district
    area_weight: 0.0362
  - to: "us/states/wa/districts/senate/3"
    rel: in-district
    area_weight: 0.0232
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.4828
  - to: "us/states/wa/districts/house/6"
    rel: in-district
    area_weight: 0.2329
  - to: "us/states/wa/districts/house/4"
    rel: in-district
    area_weight: 0.2247
  - to: "us/states/wa/districts/house/7"
    rel: in-district
    area_weight: 0.0362
  - to: "us/states/wa/districts/house/3"
    rel: in-district
    area_weight: 0.0232
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Spokane County, WA

County jurisdiction — 6 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 549056 |
| Under 18 | 118285 |
| 18–64 | 335244 |
| 65+ | 95527 |
| Median household income | 78582 |
| Poverty rate | 11.68 |
| Homeownership rate | 64.48 |
| Unemployment rate | 5.33 |
| Median home value | 410700 |
| Gini index | 0.4514 |
| Vacancy rate | 5.54 |
| White | 454089 |
| Black | 11408 |
| Asian | 12568 |
| Native | 5459 |
| Hispanic/Latino | 38877 |
| Bachelor's or higher | 172788 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 48% (state senate)
- [WA Senate District 6](/us/states/wa/districts/senate/6.md) — 23% (state senate)
- [WA Senate District 4](/us/states/wa/districts/senate/4.md) — 22% (state senate)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 4% (state senate)
- [WA Senate District 3](/us/states/wa/districts/senate/3.md) — 2% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 48% (state house)
- [WA House District 6](/us/states/wa/districts/house/6.md) — 23% (state house)
- [WA House District 4](/us/states/wa/districts/house/4.md) — 22% (state house)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 4% (state house)
- [WA House District 3](/us/states/wa/districts/house/3.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
