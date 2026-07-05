---
type: Jurisdiction
title: "Hardin County, KY"
classification: county
fips: "21093"
state: "KY"
demographics:
  population: 111942
  population_under_18: 27635
  population_18_64: 67385
  population_65_plus: 16922
  median_household_income: 67647
  poverty_rate: 13.06
  homeownership_rate: 62.57
  unemployment_rate: 6.59
  median_home_value: 225800
  gini_index: 0.4639
  vacancy_rate: 7.25
  race_white: 84992
  race_black: 12535
  race_asian: 2471
  race_native: 238
  hispanic: 7273
  bachelors_plus: 25948
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/10"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/18"
    rel: in-district
    area_weight: 0.4165
  - to: "us/states/ky/districts/house/10"
    rel: in-district
    area_weight: 0.2477
  - to: "us/states/ky/districts/house/25"
    rel: in-district
    area_weight: 0.1663
  - to: "us/states/ky/districts/house/26"
    rel: in-district
    area_weight: 0.1549
  - to: "us/states/ky/districts/house/27"
    rel: in-district
    area_weight: 0.0145
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Hardin County, KY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 111942 |
| Under 18 | 27635 |
| 18–64 | 67385 |
| 65+ | 16922 |
| Median household income | 67647 |
| Poverty rate | 13.06 |
| Homeownership rate | 62.57 |
| Unemployment rate | 6.59 |
| Median home value | 225800 |
| Gini index | 0.4639 |
| Vacancy rate | 7.25 |
| White | 84992 |
| Black | 12535 |
| Asian | 2471 |
| Native | 238 |
| Hispanic/Latino | 7273 |
| Bachelor's or higher | 25948 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 10](/us/states/ky/districts/senate/10.md) — 100% (state senate)
- [KY House District 18](/us/states/ky/districts/house/18.md) — 42% (state house)
- [KY House District 10](/us/states/ky/districts/house/10.md) — 25% (state house)
- [KY House District 25](/us/states/ky/districts/house/25.md) — 17% (state house)
- [KY House District 26](/us/states/ky/districts/house/26.md) — 15% (state house)
- [KY House District 27](/us/states/ky/districts/house/27.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
