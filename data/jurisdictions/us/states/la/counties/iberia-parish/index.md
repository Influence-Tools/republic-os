---
type: Jurisdiction
title: "Iberia Parish, LA"
classification: county
fips: "22045"
state: "LA"
demographics:
  population: 68599
  population_under_18: 17415
  population_18_64: 39688
  population_65_plus: 11496
  median_household_income: 56961
  poverty_rate: 22.84
  homeownership_rate: 67.25
  unemployment_rate: 7.26
  median_home_value: 164500
  gini_index: 0.4941
  vacancy_rate: 14.45
  race_white: 38761
  race_black: 21426
  race_asian: 1775
  race_native: 256
  hispanic: 3837
  bachelors_plus: 8657
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.6011
  - to: "us/states/la/districts/senate/22"
    rel: in-district
    area_weight: 0.3448
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.253
  - to: "us/states/la/districts/house/49"
    rel: in-district
    area_weight: 0.2897
  - to: "us/states/la/districts/house/96"
    rel: in-district
    area_weight: 0.2096
  - to: "us/states/la/districts/house/48"
    rel: in-district
    area_weight: 0.0984
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Iberia Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68599 |
| Under 18 | 17415 |
| 18–64 | 39688 |
| 65+ | 11496 |
| Median household income | 56961 |
| Poverty rate | 22.84 |
| Homeownership rate | 67.25 |
| Unemployment rate | 7.26 |
| Median home value | 164500 |
| Gini index | 0.4941 |
| Vacancy rate | 14.45 |
| White | 38761 |
| Black | 21426 |
| Asian | 1775 |
| Native | 256 |
| Hispanic/Latino | 3837 |
| Bachelor's or higher | 8657 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 60% (congressional)
- [LA Senate District 22](/us/states/la/districts/senate/22.md) — 34% (state senate)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 25% (state senate)
- [LA House District 49](/us/states/la/districts/house/49.md) — 29% (state house)
- [LA House District 96](/us/states/la/districts/house/96.md) — 21% (state house)
- [LA House District 48](/us/states/la/districts/house/48.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
