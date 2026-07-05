---
type: Jurisdiction
title: "Douglas County, OR"
classification: county
fips: "41019"
state: "OR"
demographics:
  population: 112072
  population_under_18: 21389
  population_18_64: 60989
  population_65_plus: 29694
  median_household_income: 61310
  poverty_rate: 16.27
  homeownership_rate: 72.74
  unemployment_rate: 5.38
  median_home_value: 310300
  gini_index: 0.4553
  vacancy_rate: 6.02
  race_white: 96864
  race_black: 392
  race_asian: 959
  race_native: 1190
  hispanic: 7444
  bachelors_plus: 21982
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.558
  - to: "us/states/or/districts/04"
    rel: in-district
    area_weight: 0.4295
  - to: "us/states/or/districts/senate/1"
    rel: in-district
    area_weight: 0.7211
  - to: "us/states/or/districts/senate/2"
    rel: in-district
    area_weight: 0.1649
  - to: "us/states/or/districts/senate/5"
    rel: in-district
    area_weight: 0.1015
  - to: "us/states/or/districts/house/2"
    rel: in-district
    area_weight: 0.6188
  - to: "us/states/or/districts/house/4"
    rel: in-district
    area_weight: 0.1649
  - to: "us/states/or/districts/house/1"
    rel: in-district
    area_weight: 0.1024
  - to: "us/states/or/districts/house/9"
    rel: in-district
    area_weight: 0.1015
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Douglas County, OR

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 112072 |
| Under 18 | 21389 |
| 18–64 | 60989 |
| 65+ | 29694 |
| Median household income | 61310 |
| Poverty rate | 16.27 |
| Homeownership rate | 72.74 |
| Unemployment rate | 5.38 |
| Median home value | 310300 |
| Gini index | 0.4553 |
| Vacancy rate | 6.02 |
| White | 96864 |
| Black | 392 |
| Asian | 959 |
| Native | 1190 |
| Hispanic/Latino | 7444 |
| Bachelor's or higher | 21982 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 56% (congressional)
- [OR-04](/us/states/or/districts/04.md) — 43% (congressional)
- [OR Senate District 1](/us/states/or/districts/senate/1.md) — 72% (state senate)
- [OR Senate District 2](/us/states/or/districts/senate/2.md) — 16% (state senate)
- [OR Senate District 5](/us/states/or/districts/senate/5.md) — 10% (state senate)
- [OR House District 2](/us/states/or/districts/house/2.md) — 62% (state house)
- [OR House District 4](/us/states/or/districts/house/4.md) — 16% (state house)
- [OR House District 1](/us/states/or/districts/house/1.md) — 10% (state house)
- [OR House District 9](/us/states/or/districts/house/9.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
