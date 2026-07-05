---
type: Jurisdiction
title: "Mercer County, NJ"
classification: county
fips: "34021"
state: "NJ"
demographics:
  population: 385864
  population_under_18: 84828
  population_18_64: 239479
  population_65_plus: 61557
  median_household_income: 100645
  poverty_rate: 10.27
  homeownership_rate: 62.15
  unemployment_rate: 6.31
  median_home_value: 377700
  gini_index: 0.4926
  vacancy_rate: 4.65
  race_white: 178342
  race_black: 71211
  race_asian: 48018
  race_native: 5214
  hispanic: 89099
  bachelors_plus: 174244
districts:
  - to: "us/states/nj/districts/12"
    rel: in-district
    area_weight: 0.5666
  - to: "us/states/nj/districts/03"
    rel: in-district
    area_weight: 0.4332
  - to: "us/states/nj/districts/senate/15"
    rel: in-district
    area_weight: 0.5796
  - to: "us/states/nj/districts/senate/14"
    rel: in-district
    area_weight: 0.3395
  - to: "us/states/nj/districts/senate/16"
    rel: in-district
    area_weight: 0.0806
  - to: "us/states/nj/districts/house/15"
    rel: in-district
    area_weight: 0.5796
  - to: "us/states/nj/districts/house/14"
    rel: in-district
    area_weight: 0.3395
  - to: "us/states/nj/districts/house/16"
    rel: in-district
    area_weight: 0.0806
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Mercer County, NJ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 385864 |
| Under 18 | 84828 |
| 18–64 | 239479 |
| 65+ | 61557 |
| Median household income | 100645 |
| Poverty rate | 10.27 |
| Homeownership rate | 62.15 |
| Unemployment rate | 6.31 |
| Median home value | 377700 |
| Gini index | 0.4926 |
| Vacancy rate | 4.65 |
| White | 178342 |
| Black | 71211 |
| Asian | 48018 |
| Native | 5214 |
| Hispanic/Latino | 89099 |
| Bachelor's or higher | 174244 |

## Districts

- [NJ-12](/us/states/nj/districts/12.md) — 57% (congressional)
- [NJ-03](/us/states/nj/districts/03.md) — 43% (congressional)
- [NJ Senate District 15](/us/states/nj/districts/senate/15.md) — 58% (state senate)
- [NJ Senate District 14](/us/states/nj/districts/senate/14.md) — 34% (state senate)
- [NJ Senate District 16](/us/states/nj/districts/senate/16.md) — 8% (state senate)
- [NJ House District 15](/us/states/nj/districts/house/15.md) — 58% (state house)
- [NJ House District 14](/us/states/nj/districts/house/14.md) — 34% (state house)
- [NJ House District 16](/us/states/nj/districts/house/16.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
