---
type: Jurisdiction
title: "Marion County, WV"
classification: county
fips: "54049"
state: "WV"
demographics:
  population: 55909
  population_under_18: 11105
  population_18_64: 33568
  population_65_plus: 11236
  median_household_income: 67370
  poverty_rate: 13.56
  homeownership_rate: 76.68
  unemployment_rate: 4.78
  median_home_value: 166700
  gini_index: 0.4144
  vacancy_rate: 11.18
  race_white: 51194
  race_black: 1428
  race_asian: 323
  race_native: 12
  hispanic: 919
  bachelors_plus: 14388
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/2"
    rel: in-district
    area_weight: 0.693
  - to: "us/states/wv/districts/senate/13"
    rel: in-district
    area_weight: 0.3068
  - to: "us/states/wv/districts/house/74"
    rel: in-district
    area_weight: 0.518
  - to: "us/states/wv/districts/house/76"
    rel: in-district
    area_weight: 0.2344
  - to: "us/states/wv/districts/house/75"
    rel: in-district
    area_weight: 0.188
  - to: "us/states/wv/districts/house/73"
    rel: in-district
    area_weight: 0.0591
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Marion County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 55909 |
| Under 18 | 11105 |
| 18–64 | 33568 |
| 65+ | 11236 |
| Median household income | 67370 |
| Poverty rate | 13.56 |
| Homeownership rate | 76.68 |
| Unemployment rate | 4.78 |
| Median home value | 166700 |
| Gini index | 0.4144 |
| Vacancy rate | 11.18 |
| White | 51194 |
| Black | 1428 |
| Asian | 323 |
| Native | 12 |
| Hispanic/Latino | 919 |
| Bachelor's or higher | 14388 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 2](/us/states/wv/districts/senate/2.md) — 69% (state senate)
- [WV Senate District 13](/us/states/wv/districts/senate/13.md) — 31% (state senate)
- [WV House District 74](/us/states/wv/districts/house/74.md) — 52% (state house)
- [WV House District 76](/us/states/wv/districts/house/76.md) — 23% (state house)
- [WV House District 75](/us/states/wv/districts/house/75.md) — 19% (state house)
- [WV House District 73](/us/states/wv/districts/house/73.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
