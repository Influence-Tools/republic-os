---
type: Jurisdiction
title: "Tooele County, UT"
classification: county
fips: "49045"
state: "UT"
demographics:
  population: 79347
  population_under_18: 24582
  population_18_64: 47489
  population_65_plus: 7276
  median_household_income: 106587
  poverty_rate: 5.19
  homeownership_rate: 81.76
  unemployment_rate: 3.58
  median_home_value: 431600
  gini_index: 0.3732
  vacancy_rate: 4.17
  race_white: 66774
  race_black: 790
  race_asian: 581
  race_native: 456
  hispanic: 11935
  bachelors_plus: 14545
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ut/districts/senate/11"
    rel: in-district
    area_weight: 0.7528
  - to: "us/states/ut/districts/senate/1"
    rel: in-district
    area_weight: 0.2471
  - to: "us/states/ut/districts/house/29"
    rel: in-district
    area_weight: 0.9854
  - to: "us/states/ut/districts/house/28"
    rel: in-district
    area_weight: 0.0145
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Tooele County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 79347 |
| Under 18 | 24582 |
| 18–64 | 47489 |
| 65+ | 7276 |
| Median household income | 106587 |
| Poverty rate | 5.19 |
| Homeownership rate | 81.76 |
| Unemployment rate | 3.58 |
| Median home value | 431600 |
| Gini index | 0.3732 |
| Vacancy rate | 4.17 |
| White | 66774 |
| Black | 790 |
| Asian | 581 |
| Native | 456 |
| Hispanic/Latino | 11935 |
| Bachelor's or higher | 14545 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 11](/us/states/ut/districts/senate/11.md) — 75% (state senate)
- [UT Senate District 1](/us/states/ut/districts/senate/1.md) — 25% (state senate)
- [UT House District 29](/us/states/ut/districts/house/29.md) — 99% (state house)
- [UT House District 28](/us/states/ut/districts/house/28.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
