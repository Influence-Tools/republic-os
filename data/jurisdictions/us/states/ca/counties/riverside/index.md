---
type: Jurisdiction
title: "Riverside County, CA"
classification: county
fips: "06065"
state: "CA"
demographics:
  population: 2478600
  population_under_18: 597369
  population_18_64: 1498343
  population_65_plus: 382888
  median_household_income: 93074
  poverty_rate: 10.62
  homeownership_rate: 69.13
  unemployment_rate: 6.5
  median_home_value: 557300
  gini_index: 0.4381
  vacancy_rate: 10.82
  race_white: 932298
  race_black: 157724
  race_asian: 175644
  race_native: 33504
  hispanic: 1270563
  bachelors_plus: 574063
districts:
  - to: "us/states/ca/districts/25"
    rel: in-district
    area_weight: 0.7218
  - to: "us/states/ca/districts/41"
    rel: in-district
    area_weight: 0.184
  - to: "us/states/ca/districts/48"
    rel: in-district
    area_weight: 0.052
  - to: "us/states/ca/districts/39"
    rel: in-district
    area_weight: 0.039
  - to: "us/states/ca/districts/senate/18"
    rel: in-district
    area_weight: 0.4151
  - to: "us/states/ca/districts/senate/19"
    rel: in-district
    area_weight: 0.326
  - to: "us/states/ca/districts/senate/32"
    rel: in-district
    area_weight: 0.2125
  - to: "us/states/ca/districts/senate/31"
    rel: in-district
    area_weight: 0.0463
  - to: "us/states/ca/districts/house/36"
    rel: in-district
    area_weight: 0.5354
  - to: "us/states/ca/districts/house/47"
    rel: in-district
    area_weight: 0.3074
  - to: "us/states/ca/districts/house/63"
    rel: in-district
    area_weight: 0.0501
  - to: "us/states/ca/districts/house/71"
    rel: in-district
    area_weight: 0.0473
  - to: "us/states/ca/districts/house/60"
    rel: in-district
    area_weight: 0.0419
  - to: "us/states/ca/districts/house/58"
    rel: in-district
    area_weight: 0.0178
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Riverside County, CA

County jurisdiction — 8 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2478600 |
| Under 18 | 597369 |
| 18–64 | 1498343 |
| 65+ | 382888 |
| Median household income | 93074 |
| Poverty rate | 10.62 |
| Homeownership rate | 69.13 |
| Unemployment rate | 6.5 |
| Median home value | 557300 |
| Gini index | 0.4381 |
| Vacancy rate | 10.82 |
| White | 932298 |
| Black | 157724 |
| Asian | 175644 |
| Native | 33504 |
| Hispanic/Latino | 1270563 |
| Bachelor's or higher | 574063 |

## Districts

- [CA-25](/us/states/ca/districts/25.md) — 72% (congressional)
- [CA-41](/us/states/ca/districts/41.md) — 18% (congressional)
- [CA-48](/us/states/ca/districts/48.md) — 5% (congressional)
- [CA-39](/us/states/ca/districts/39.md) — 4% (congressional)
- [CA Senate District 18](/us/states/ca/districts/senate/18.md) — 42% (state senate)
- [CA Senate District 19](/us/states/ca/districts/senate/19.md) — 33% (state senate)
- [CA Senate District 32](/us/states/ca/districts/senate/32.md) — 21% (state senate)
- [CA Senate District 31](/us/states/ca/districts/senate/31.md) — 5% (state senate)
- [CA House District 36](/us/states/ca/districts/house/36.md) — 54% (state house)
- [CA House District 47](/us/states/ca/districts/house/47.md) — 31% (state house)
- [CA House District 63](/us/states/ca/districts/house/63.md) — 5% (state house)
- [CA House District 71](/us/states/ca/districts/house/71.md) — 5% (state house)
- [CA House District 60](/us/states/ca/districts/house/60.md) — 4% (state house)
- [CA House District 58](/us/states/ca/districts/house/58.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
