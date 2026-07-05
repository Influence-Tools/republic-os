---
type: Jurisdiction
title: "McCracken County, KY"
classification: county
fips: "21145"
state: "KY"
demographics:
  population: 67564
  population_under_18: 14733
  population_18_64: 39006
  population_65_plus: 13825
  median_household_income: 64373
  poverty_rate: 15.16
  homeownership_rate: 68.93
  unemployment_rate: 3.24
  median_home_value: 188100
  gini_index: 0.4959
  vacancy_rate: 14.5
  race_white: 55375
  race_black: 6586
  race_asian: 583
  race_native: 114
  hispanic: 2314
  bachelors_plus: 19333
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/senate/2"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/house/1"
    rel: in-district
    area_weight: 0.5379
  - to: "us/states/ky/districts/house/2"
    rel: in-district
    area_weight: 0.1771
  - to: "us/states/ky/districts/house/3"
    rel: in-district
    area_weight: 0.1582
  - to: "us/states/ky/districts/house/6"
    rel: in-district
    area_weight: 0.1259
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# McCracken County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67564 |
| Under 18 | 14733 |
| 18–64 | 39006 |
| 65+ | 13825 |
| Median household income | 64373 |
| Poverty rate | 15.16 |
| Homeownership rate | 68.93 |
| Unemployment rate | 3.24 |
| Median home value | 188100 |
| Gini index | 0.4959 |
| Vacancy rate | 14.5 |
| White | 55375 |
| Black | 6586 |
| Asian | 583 |
| Native | 114 |
| Hispanic/Latino | 2314 |
| Bachelor's or higher | 19333 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 2](/us/states/ky/districts/senate/2.md) — 100% (state senate)
- [KY House District 1](/us/states/ky/districts/house/1.md) — 54% (state house)
- [KY House District 2](/us/states/ky/districts/house/2.md) — 18% (state house)
- [KY House District 3](/us/states/ky/districts/house/3.md) — 16% (state house)
- [KY House District 6](/us/states/ky/districts/house/6.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
