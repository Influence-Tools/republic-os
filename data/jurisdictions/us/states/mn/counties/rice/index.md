---
type: Jurisdiction
title: "Rice County, MN"
classification: county
fips: "27131"
state: "MN"
demographics:
  population: 67917
  population_under_18: 14556
  population_18_64: 42057
  population_65_plus: 11304
  median_household_income: 83181
  poverty_rate: 10.2
  homeownership_rate: 76.27
  unemployment_rate: 4.55
  median_home_value: 320200
  gini_index: 0.4276
  vacancy_rate: 7.12
  race_white: 53994
  race_black: 4589
  race_asian: 1545
  race_native: 349
  hispanic: 7105
  bachelors_plus: 18375
districts:
  - to: "us/states/mn/districts/02"
    rel: in-district
    area_weight: 0.5634
  - to: "us/states/mn/districts/01"
    rel: in-district
    area_weight: 0.4366
  - to: "us/states/mn/districts/senate/19"
    rel: in-district
    area_weight: 0.5589
  - to: "us/states/mn/districts/senate/58"
    rel: in-district
    area_weight: 0.3709
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.0702
  - to: "us/states/mn/districts/house/19a"
    rel: in-district
    area_weight: 0.5589
  - to: "us/states/mn/districts/house/58a"
    rel: in-district
    area_weight: 0.2957
  - to: "us/states/mn/districts/house/58b"
    rel: in-district
    area_weight: 0.0752
  - to: "us/states/mn/districts/house/22b"
    rel: in-district
    area_weight: 0.0702
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Rice County, MN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67917 |
| Under 18 | 14556 |
| 18–64 | 42057 |
| 65+ | 11304 |
| Median household income | 83181 |
| Poverty rate | 10.2 |
| Homeownership rate | 76.27 |
| Unemployment rate | 4.55 |
| Median home value | 320200 |
| Gini index | 0.4276 |
| Vacancy rate | 7.12 |
| White | 53994 |
| Black | 4589 |
| Asian | 1545 |
| Native | 349 |
| Hispanic/Latino | 7105 |
| Bachelor's or higher | 18375 |

## Districts

- [MN-02](/us/states/mn/districts/02.md) — 56% (congressional)
- [MN-01](/us/states/mn/districts/01.md) — 44% (congressional)
- [MN Senate District 19](/us/states/mn/districts/senate/19.md) — 56% (state senate)
- [MN Senate District 58](/us/states/mn/districts/senate/58.md) — 37% (state senate)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 7% (state senate)
- [MN House District 19A](/us/states/mn/districts/house/19a.md) — 56% (state house)
- [MN House District 58A](/us/states/mn/districts/house/58a.md) — 30% (state house)
- [MN House District 58B](/us/states/mn/districts/house/58b.md) — 8% (state house)
- [MN House District 22B](/us/states/mn/districts/house/22b.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
