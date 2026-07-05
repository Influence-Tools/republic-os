---
type: Jurisdiction
title: "Denver County, CO"
classification: county
fips: "08031"
state: "CO"
demographics:
  population: 718877
  population_under_18: 129515
  population_18_64: 499651
  population_65_plus: 89711
  median_household_income: 94718
  poverty_rate: 11.24
  homeownership_rate: 48.76
  unemployment_rate: 4.88
  median_home_value: 616000
  gini_index: 0.4905
  vacancy_rate: 6.72
  race_white: 426585
  race_black: 64967
  race_asian: 26665
  race_native: 7263
  hispanic: 201140
  bachelors_plus: 419205
districts:
  - to: "us/states/co/districts/01"
    rel: in-district
    area_weight: 0.9767
  - to: "us/states/co/districts/06"
    rel: in-district
    area_weight: 0.0097
  - to: "us/states/co/districts/08"
    rel: in-district
    area_weight: 0.0067
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.0053
  - to: "us/states/co/districts/senate/33"
    rel: in-district
    area_weight: 0.4767
  - to: "us/states/co/districts/senate/34"
    rel: in-district
    area_weight: 0.1706
  - to: "us/states/co/districts/senate/32"
    rel: in-district
    area_weight: 0.1507
  - to: "us/states/co/districts/senate/31"
    rel: in-district
    area_weight: 0.1197
  - to: "us/states/co/districts/senate/26"
    rel: in-district
    area_weight: 0.0817
  - to: "us/states/co/districts/house/7"
    rel: in-district
    area_weight: 0.3732
  - to: "us/states/co/districts/house/8"
    rel: in-district
    area_weight: 0.1126
  - to: "us/states/co/districts/house/1"
    rel: in-district
    area_weight: 0.1049
  - to: "us/states/co/districts/house/5"
    rel: in-district
    area_weight: 0.0989
  - to: "us/states/co/districts/house/2"
    rel: in-district
    area_weight: 0.0807
  - to: "us/states/co/districts/house/4"
    rel: in-district
    area_weight: 0.0749
  - to: "us/states/co/districts/house/9"
    rel: in-district
    area_weight: 0.0588
  - to: "us/states/co/districts/house/6"
    rel: in-district
    area_weight: 0.0582
  - to: "us/states/co/districts/house/3"
    rel: in-district
    area_weight: 0.0371
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Denver County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 718877 |
| Under 18 | 129515 |
| 18–64 | 499651 |
| 65+ | 89711 |
| Median household income | 94718 |
| Poverty rate | 11.24 |
| Homeownership rate | 48.76 |
| Unemployment rate | 4.88 |
| Median home value | 616000 |
| Gini index | 0.4905 |
| Vacancy rate | 6.72 |
| White | 426585 |
| Black | 64967 |
| Asian | 26665 |
| Native | 7263 |
| Hispanic/Latino | 201140 |
| Bachelor's or higher | 419205 |

## Districts

- [CO-01](/us/states/co/districts/01.md) — 98% (congressional)
- [CO-06](/us/states/co/districts/06.md) — 1% (congressional)
- [CO-08](/us/states/co/districts/08.md) — 1% (congressional)
- [CO-07](/us/states/co/districts/07.md) — 1% (congressional)
- [CO Senate District 33](/us/states/co/districts/senate/33.md) — 48% (state senate)
- [CO Senate District 34](/us/states/co/districts/senate/34.md) — 17% (state senate)
- [CO Senate District 32](/us/states/co/districts/senate/32.md) — 15% (state senate)
- [CO Senate District 31](/us/states/co/districts/senate/31.md) — 12% (state senate)
- [CO Senate District 26](/us/states/co/districts/senate/26.md) — 8% (state senate)
- [CO House District 7](/us/states/co/districts/house/7.md) — 37% (state house)
- [CO House District 8](/us/states/co/districts/house/8.md) — 11% (state house)
- [CO House District 1](/us/states/co/districts/house/1.md) — 10% (state house)
- [CO House District 5](/us/states/co/districts/house/5.md) — 10% (state house)
- [CO House District 2](/us/states/co/districts/house/2.md) — 8% (state house)
- [CO House District 4](/us/states/co/districts/house/4.md) — 7% (state house)
- [CO House District 9](/us/states/co/districts/house/9.md) — 6% (state house)
- [CO House District 6](/us/states/co/districts/house/6.md) — 6% (state house)
- [CO House District 3](/us/states/co/districts/house/3.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
