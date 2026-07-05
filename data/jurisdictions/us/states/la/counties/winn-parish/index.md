---
type: Jurisdiction
title: "Winn Parish, LA"
classification: county
fips: "22127"
state: "LA"
demographics:
  population: 13467
  population_under_18: 2790
  population_18_64: 8231
  population_65_plus: 2446
  median_household_income: 48871
  poverty_rate: 24.26
  homeownership_rate: 71.17
  unemployment_rate: 5.15
  median_home_value: 108500
  gini_index: 0.4883
  vacancy_rate: 24.71
  race_white: 8380
  race_black: 3583
  race_asian: 244
  race_native: 2
  hispanic: 1054
  bachelors_plus: 1827
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/la/districts/senate/35"
    rel: in-district
    area_weight: 0.4124
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.331
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.2565
  - to: "us/states/la/districts/house/13"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Winn Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13467 |
| Under 18 | 2790 |
| 18–64 | 8231 |
| 65+ | 2446 |
| Median household income | 48871 |
| Poverty rate | 24.26 |
| Homeownership rate | 71.17 |
| Unemployment rate | 5.15 |
| Median home value | 108500 |
| Gini index | 0.4883 |
| Vacancy rate | 24.71 |
| White | 8380 |
| Black | 3583 |
| Asian | 244 |
| Native | 2 |
| Hispanic/Latino | 1054 |
| Bachelor's or higher | 1827 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 35](/us/states/la/districts/senate/35.md) — 41% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 33% (state senate)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 26% (state senate)
- [LA House District 13](/us/states/la/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
