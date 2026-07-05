---
type: Jurisdiction
title: "Elmore County, AL"
classification: county
fips: "01051"
state: "AL"
demographics:
  population: 89526
  population_under_18: 19313
  population_18_64: 55410
  population_65_plus: 14803
  median_household_income: 78243
  poverty_rate: 10.32
  homeownership_rate: 76.97
  unemployment_rate: 4.65
  median_home_value: 223900
  gini_index: 0.4334
  vacancy_rate: 11.97
  race_white: 65175
  race_black: 18939
  race_asian: 450
  race_native: 170
  hispanic: 3034
  bachelors_plus: 21446
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.9927
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.006
  - to: "us/states/al/districts/senate/25"
    rel: in-district
    area_weight: 0.8644
  - to: "us/states/al/districts/senate/30"
    rel: in-district
    area_weight: 0.1354
  - to: "us/states/al/districts/house/31"
    rel: in-district
    area_weight: 0.6959
  - to: "us/states/al/districts/house/75"
    rel: in-district
    area_weight: 0.2376
  - to: "us/states/al/districts/house/88"
    rel: in-district
    area_weight: 0.0662
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Elmore County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 89526 |
| Under 18 | 19313 |
| 18–64 | 55410 |
| 65+ | 14803 |
| Median household income | 78243 |
| Poverty rate | 10.32 |
| Homeownership rate | 76.97 |
| Unemployment rate | 4.65 |
| Median home value | 223900 |
| Gini index | 0.4334 |
| Vacancy rate | 11.97 |
| White | 65175 |
| Black | 18939 |
| Asian | 450 |
| Native | 170 |
| Hispanic/Latino | 3034 |
| Bachelor's or higher | 21446 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 99% (congressional)
- [AL-02](/us/states/al/districts/02.md) — 1% (congressional)
- [AL Senate District 25](/us/states/al/districts/senate/25.md) — 86% (state senate)
- [AL Senate District 30](/us/states/al/districts/senate/30.md) — 14% (state senate)
- [AL House District 31](/us/states/al/districts/house/31.md) — 70% (state house)
- [AL House District 75](/us/states/al/districts/house/75.md) — 24% (state house)
- [AL House District 88](/us/states/al/districts/house/88.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
