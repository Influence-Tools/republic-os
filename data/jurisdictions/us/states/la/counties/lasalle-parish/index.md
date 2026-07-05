---
type: Jurisdiction
title: "LaSalle Parish, LA"
classification: county
fips: "22059"
state: "LA"
demographics:
  population: 14789
  population_under_18: 3421
  population_18_64: 8860
  population_65_plus: 2508
  median_household_income: 68497
  poverty_rate: 16.01
  homeownership_rate: 80.55
  unemployment_rate: 4.88
  median_home_value: 119500
  gini_index: 0.44
  vacancy_rate: 18.59
  race_white: 11556
  race_black: 2174
  race_asian: 142
  race_native: 2
  hispanic: 1350
  bachelors_plus: 1768
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.993
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.0052
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/22"
    rel: in-district
    area_weight: 0.5967
  - to: "us/states/la/districts/house/20"
    rel: in-district
    area_weight: 0.4031
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# LaSalle Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14789 |
| Under 18 | 3421 |
| 18–64 | 8860 |
| 65+ | 2508 |
| Median household income | 68497 |
| Poverty rate | 16.01 |
| Homeownership rate | 80.55 |
| Unemployment rate | 4.88 |
| Median home value | 119500 |
| Gini index | 0.44 |
| Vacancy rate | 18.59 |
| White | 11556 |
| Black | 2174 |
| Asian | 142 |
| Native | 2 |
| Hispanic/Latino | 1350 |
| Bachelor's or higher | 1768 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 99% (congressional)
- [LA-04](/us/states/la/districts/04.md) — 1% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 100% (state senate)
- [LA House District 22](/us/states/la/districts/house/22.md) — 60% (state house)
- [LA House District 20](/us/states/la/districts/house/20.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
