---
type: Jurisdiction
title: "Knox County, IL"
classification: county
fips: "17095"
state: "IL"
demographics:
  population: 49046
  population_under_18: 9907
  population_18_64: 28232
  population_65_plus: 10907
  median_household_income: 57030
  poverty_rate: 14.57
  homeownership_rate: 70.82
  unemployment_rate: 5.1
  median_home_value: 111900
  gini_index: 0.4542
  vacancy_rate: 11.73
  race_white: 40178
  race_black: 3962
  race_asian: 617
  race_native: 29
  hispanic: 3161
  bachelors_plus: 9734
districts:
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.7986
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.2014
  - to: "us/states/il/districts/house/93"
    rel: in-district
    area_weight: 0.598
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.2014
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.2006
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Knox County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49046 |
| Under 18 | 9907 |
| 18–64 | 28232 |
| 65+ | 10907 |
| Median household income | 57030 |
| Poverty rate | 14.57 |
| Homeownership rate | 70.82 |
| Unemployment rate | 5.1 |
| Median home value | 111900 |
| Gini index | 0.4542 |
| Vacancy rate | 11.73 |
| White | 40178 |
| Black | 3962 |
| Asian | 617 |
| Native | 29 |
| Hispanic/Latino | 3161 |
| Bachelor's or higher | 9734 |

## Districts

- [IL-17](/us/states/il/districts/17.md) — 100% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 80% (state senate)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 20% (state senate)
- [IL House District 93](/us/states/il/districts/house/93.md) — 60% (state house)
- [IL House District 71](/us/states/il/districts/house/71.md) — 20% (state house)
- [IL House District 94](/us/states/il/districts/house/94.md) — 20% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
