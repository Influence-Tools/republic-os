---
type: Jurisdiction
title: "Clark County, NV"
classification: county
fips: "32003"
state: "NV"
demographics:
  population: 2329548
  population_under_18: 517221
  population_18_64: 1441908
  population_65_plus: 370419
  median_household_income: 76472
  poverty_rate: 13.04
  homeownership_rate: 57.78
  unemployment_rate: 7.59
  median_home_value: 431000
  gini_index: 0.4683
  vacancy_rate: 9.11
  race_white: 1016671
  race_black: 280163
  race_asian: 250287
  race_native: 27274
  hispanic: 742075
  bachelors_plus: 606317
districts:
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.6235
  - to: "us/states/nv/districts/03"
    rel: in-district
    area_weight: 0.2495
  - to: "us/states/nv/districts/01"
    rel: in-district
    area_weight: 0.1254
  - to: "us/states/nv/districts/senate/20"
    rel: in-district
    area_weight: 0.5383
  - to: "us/states/nv/districts/senate/19"
    rel: in-district
    area_weight: 0.4007
  - to: "us/states/nv/districts/senate/21"
    rel: in-district
    area_weight: 0.0087
  - to: "us/states/nv/districts/senate/11"
    rel: in-district
    area_weight: 0.006
  - to: "us/states/nv/districts/senate/1"
    rel: in-district
    area_weight: 0.0054
  - to: "us/states/nv/districts/senate/10"
    rel: in-district
    area_weight: 0.0053
  - to: "us/states/nv/districts/house/36"
    rel: in-district
    area_weight: 0.4006
  - to: "us/states/nv/districts/house/19"
    rel: in-district
    area_weight: 0.3345
  - to: "us/states/nv/districts/house/23"
    rel: in-district
    area_weight: 0.2039
  - to: "us/states/nv/districts/house/12"
    rel: in-district
    area_weight: 0.0077
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Clark County, NV

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2329548 |
| Under 18 | 517221 |
| 18–64 | 1441908 |
| 65+ | 370419 |
| Median household income | 76472 |
| Poverty rate | 13.04 |
| Homeownership rate | 57.78 |
| Unemployment rate | 7.59 |
| Median home value | 431000 |
| Gini index | 0.4683 |
| Vacancy rate | 9.11 |
| White | 1016671 |
| Black | 280163 |
| Asian | 250287 |
| Native | 27274 |
| Hispanic/Latino | 742075 |
| Bachelor's or higher | 606317 |

## Districts

- [NV-04](/us/states/nv/districts/04.md) — 62% (congressional)
- [NV-03](/us/states/nv/districts/03.md) — 25% (congressional)
- [NV-01](/us/states/nv/districts/01.md) — 13% (congressional)
- [NV Senate District 20](/us/states/nv/districts/senate/20.md) — 54% (state senate)
- [NV Senate District 19](/us/states/nv/districts/senate/19.md) — 40% (state senate)
- [NV Senate District 21](/us/states/nv/districts/senate/21.md) — 1% (state senate)
- [NV Senate District 11](/us/states/nv/districts/senate/11.md) — 1% (state senate)
- [NV Senate District 1](/us/states/nv/districts/senate/1.md) — 1% (state senate)
- [NV Senate District 10](/us/states/nv/districts/senate/10.md) — 1% (state senate)
- [NV House District 36](/us/states/nv/districts/house/36.md) — 40% (state house)
- [NV House District 19](/us/states/nv/districts/house/19.md) — 33% (state house)
- [NV House District 23](/us/states/nv/districts/house/23.md) — 20% (state house)
- [NV House District 12](/us/states/nv/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
