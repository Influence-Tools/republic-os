---
type: Jurisdiction
title: "Weld County, CO"
classification: county
fips: "08123"
state: "CO"
demographics:
  population: 369745
  population_under_18: 102268
  population_18_64: 136428
  population_65_plus: 131049
  median_household_income: 101563
  poverty_rate: 9.81
  homeownership_rate: 76.32
  unemployment_rate: 3.86
  median_home_value: 496100
  gini_index: 0.4159
  vacancy_rate: 4.77
  race_white: 266678
  race_black: 5502
  race_asian: 5739
  race_native: 4118
  hispanic: 118337
  bachelors_plus: 113601
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.8027
  - to: "us/states/co/districts/08"
    rel: in-district
    area_weight: 0.1869
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.0102
  - to: "us/states/co/districts/senate/1"
    rel: in-district
    area_weight: 0.8745
  - to: "us/states/co/districts/senate/23"
    rel: in-district
    area_weight: 0.08
  - to: "us/states/co/districts/senate/13"
    rel: in-district
    area_weight: 0.0386
  - to: "us/states/co/districts/senate/17"
    rel: in-district
    area_weight: 0.0068
  - to: "us/states/co/districts/house/63"
    rel: in-district
    area_weight: 0.7746
  - to: "us/states/co/districts/house/48"
    rel: in-district
    area_weight: 0.119
  - to: "us/states/co/districts/house/64"
    rel: in-district
    area_weight: 0.0412
  - to: "us/states/co/districts/house/65"
    rel: in-district
    area_weight: 0.0293
  - to: "us/states/co/districts/house/19"
    rel: in-district
    area_weight: 0.0278
  - to: "us/states/co/districts/house/50"
    rel: in-district
    area_weight: 0.0079
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Weld County, CO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 369745 |
| Under 18 | 102268 |
| 18–64 | 136428 |
| 65+ | 131049 |
| Median household income | 101563 |
| Poverty rate | 9.81 |
| Homeownership rate | 76.32 |
| Unemployment rate | 3.86 |
| Median home value | 496100 |
| Gini index | 0.4159 |
| Vacancy rate | 4.77 |
| White | 266678 |
| Black | 5502 |
| Asian | 5739 |
| Native | 4118 |
| Hispanic/Latino | 118337 |
| Bachelor's or higher | 113601 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 80% (congressional)
- [CO-08](/us/states/co/districts/08.md) — 19% (congressional)
- [CO-02](/us/states/co/districts/02.md) — 1% (congressional)
- [CO Senate District 1](/us/states/co/districts/senate/1.md) — 87% (state senate)
- [CO Senate District 23](/us/states/co/districts/senate/23.md) — 8% (state senate)
- [CO Senate District 13](/us/states/co/districts/senate/13.md) — 4% (state senate)
- [CO Senate District 17](/us/states/co/districts/senate/17.md) — 1% (state senate)
- [CO House District 63](/us/states/co/districts/house/63.md) — 77% (state house)
- [CO House District 48](/us/states/co/districts/house/48.md) — 12% (state house)
- [CO House District 64](/us/states/co/districts/house/64.md) — 4% (state house)
- [CO House District 65](/us/states/co/districts/house/65.md) — 3% (state house)
- [CO House District 19](/us/states/co/districts/house/19.md) — 3% (state house)
- [CO House District 50](/us/states/co/districts/house/50.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
