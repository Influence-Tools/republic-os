---
type: Jurisdiction
title: "Ouachita Parish, LA"
classification: county
fips: "22073"
state: "LA"
demographics:
  population: 158480
  population_under_18: 38938
  population_18_64: 94423
  population_65_plus: 25119
  median_household_income: 54688
  poverty_rate: 23.17
  homeownership_rate: 60.97
  unemployment_rate: 6.5
  median_home_value: 194400
  gini_index: 0.5179
  vacancy_rate: 13.61
  race_white: 89400
  race_black: 59054
  race_asian: 1819
  race_native: 322
  hispanic: 5878
  bachelors_plus: 41597
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.5906
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.4094
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.3133
  - to: "us/states/la/districts/senate/34"
    rel: in-district
    area_weight: 0.26
  - to: "us/states/la/districts/senate/35"
    rel: in-district
    area_weight: 0.2571
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.1696
  - to: "us/states/la/districts/house/15"
    rel: in-district
    area_weight: 0.3656
  - to: "us/states/la/districts/house/14"
    rel: in-district
    area_weight: 0.2267
  - to: "us/states/la/districts/house/20"
    rel: in-district
    area_weight: 0.2033
  - to: "us/states/la/districts/house/17"
    rel: in-district
    area_weight: 0.1305
  - to: "us/states/la/districts/house/16"
    rel: in-district
    area_weight: 0.0737
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Ouachita Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 158480 |
| Under 18 | 38938 |
| 18–64 | 94423 |
| 65+ | 25119 |
| Median household income | 54688 |
| Poverty rate | 23.17 |
| Homeownership rate | 60.97 |
| Unemployment rate | 6.5 |
| Median home value | 194400 |
| Gini index | 0.5179 |
| Vacancy rate | 13.61 |
| White | 89400 |
| Black | 59054 |
| Asian | 1819 |
| Native | 322 |
| Hispanic/Latino | 5878 |
| Bachelor's or higher | 41597 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 59% (congressional)
- [LA-05](/us/states/la/districts/05.md) — 41% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 31% (state senate)
- [LA Senate District 34](/us/states/la/districts/senate/34.md) — 26% (state senate)
- [LA Senate District 35](/us/states/la/districts/senate/35.md) — 26% (state senate)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 17% (state senate)
- [LA House District 15](/us/states/la/districts/house/15.md) — 37% (state house)
- [LA House District 14](/us/states/la/districts/house/14.md) — 23% (state house)
- [LA House District 20](/us/states/la/districts/house/20.md) — 20% (state house)
- [LA House District 17](/us/states/la/districts/house/17.md) — 13% (state house)
- [LA House District 16](/us/states/la/districts/house/16.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
