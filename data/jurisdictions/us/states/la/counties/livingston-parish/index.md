---
type: Jurisdiction
title: "Livingston Parish, LA"
classification: county
fips: "22063"
state: "LA"
demographics:
  population: 148115
  population_under_18: 38220
  population_18_64: 89404
  population_65_plus: 20491
  median_household_income: 80122
  poverty_rate: 12.86
  homeownership_rate: 80.72
  unemployment_rate: 4.19
  median_home_value: 230600
  gini_index: 0.4042
  vacancy_rate: 10.65
  race_white: 120280
  race_black: 13284
  race_asian: 1081
  race_native: 280
  hispanic: 9830
  bachelors_plus: 26729
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.6446
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.3541
  - to: "us/states/la/districts/senate/13"
    rel: in-district
    area_weight: 0.5303
  - to: "us/states/la/districts/senate/6"
    rel: in-district
    area_weight: 0.277
  - to: "us/states/la/districts/senate/18"
    rel: in-district
    area_weight: 0.1794
  - to: "us/states/la/districts/senate/37"
    rel: in-district
    area_weight: 0.0132
  - to: "us/states/la/districts/house/95"
    rel: in-district
    area_weight: 0.4436
  - to: "us/states/la/districts/house/81"
    rel: in-district
    area_weight: 0.3757
  - to: "us/states/la/districts/house/64"
    rel: in-district
    area_weight: 0.0963
  - to: "us/states/la/districts/house/71"
    rel: in-district
    area_weight: 0.0841
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Livingston Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 148115 |
| Under 18 | 38220 |
| 18–64 | 89404 |
| 65+ | 20491 |
| Median household income | 80122 |
| Poverty rate | 12.86 |
| Homeownership rate | 80.72 |
| Unemployment rate | 4.19 |
| Median home value | 230600 |
| Gini index | 0.4042 |
| Vacancy rate | 10.65 |
| White | 120280 |
| Black | 13284 |
| Asian | 1081 |
| Native | 280 |
| Hispanic/Latino | 9830 |
| Bachelor's or higher | 26729 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 64% (congressional)
- [LA-01](/us/states/la/districts/01.md) — 35% (congressional)
- [LA Senate District 13](/us/states/la/districts/senate/13.md) — 53% (state senate)
- [LA Senate District 6](/us/states/la/districts/senate/6.md) — 28% (state senate)
- [LA Senate District 18](/us/states/la/districts/senate/18.md) — 18% (state senate)
- [LA Senate District 37](/us/states/la/districts/senate/37.md) — 1% (state senate)
- [LA House District 95](/us/states/la/districts/house/95.md) — 44% (state house)
- [LA House District 81](/us/states/la/districts/house/81.md) — 38% (state house)
- [LA House District 64](/us/states/la/districts/house/64.md) — 10% (state house)
- [LA House District 71](/us/states/la/districts/house/71.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
