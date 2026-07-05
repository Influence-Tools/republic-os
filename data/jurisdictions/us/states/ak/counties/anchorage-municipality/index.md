---
type: Jurisdiction
title: "Anchorage Municipality, AK"
classification: county
fips: "02020"
state: "AK"
demographics:
  population: 289600
  population_under_18: 72888
  population_18_64: 112934
  population_65_plus: 103778
  median_household_income: 105356
  poverty_rate: 8.33
  homeownership_rate: 61.96
  unemployment_rate: 4.84
  median_home_value: 429600
  gini_index: 0.4463
  vacancy_rate: 9.68
  race_white: 161675
  race_black: 11072
  race_asian: 28057
  race_native: 22259
  hispanic: 28654
  bachelors_plus: 110116
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.8953
  - to: "us/states/ak/districts/senate/l"
    rel: in-district
    area_weight: 0.5114
  - to: "us/states/ak/districts/senate/e"
    rel: in-district
    area_weight: 0.3192
  - to: "us/states/ak/districts/senate/i"
    rel: in-district
    area_weight: 0.0216
  - to: "us/states/ak/districts/senate/h"
    rel: in-district
    area_weight: 0.0134
  - to: "us/states/ak/districts/senate/f"
    rel: in-district
    area_weight: 0.0113
  - to: "us/states/ak/districts/senate/g"
    rel: in-district
    area_weight: 0.0052
  - to: "us/states/ak/districts/house/24"
    rel: in-district
    area_weight: 0.3512
  - to: "us/states/ak/districts/house/9"
    rel: in-district
    area_weight: 0.3148
  - to: "us/states/ak/districts/house/23"
    rel: in-district
    area_weight: 0.1601
  - to: "us/states/ak/districts/house/18"
    rel: in-district
    area_weight: 0.0195
  - to: "us/states/ak/districts/house/16"
    rel: in-district
    area_weight: 0.0109
  - to: "us/states/ak/districts/house/12"
    rel: in-district
    area_weight: 0.0064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Anchorage Municipality, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 289600 |
| Under 18 | 72888 |
| 18–64 | 112934 |
| 65+ | 103778 |
| Median household income | 105356 |
| Poverty rate | 8.33 |
| Homeownership rate | 61.96 |
| Unemployment rate | 4.84 |
| Median home value | 429600 |
| Gini index | 0.4463 |
| Vacancy rate | 9.68 |
| White | 161675 |
| Black | 11072 |
| Asian | 28057 |
| Native | 22259 |
| Hispanic/Latino | 28654 |
| Bachelor's or higher | 110116 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 90% (congressional)
- [AK Senate District L](/us/states/ak/districts/senate/l.md) — 51% (state senate)
- [AK Senate District E](/us/states/ak/districts/senate/e.md) — 32% (state senate)
- [AK Senate District I](/us/states/ak/districts/senate/i.md) — 2% (state senate)
- [AK Senate District H](/us/states/ak/districts/senate/h.md) — 1% (state senate)
- [AK Senate District F](/us/states/ak/districts/senate/f.md) — 1% (state senate)
- [AK Senate District G](/us/states/ak/districts/senate/g.md) — 1% (state senate)
- [AK House District 24](/us/states/ak/districts/house/24.md) — 35% (state house)
- [AK House District 9](/us/states/ak/districts/house/9.md) — 31% (state house)
- [AK House District 23](/us/states/ak/districts/house/23.md) — 16% (state house)
- [AK House District 18](/us/states/ak/districts/house/18.md) — 2% (state house)
- [AK House District 16](/us/states/ak/districts/house/16.md) — 1% (state house)
- [AK House District 12](/us/states/ak/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
