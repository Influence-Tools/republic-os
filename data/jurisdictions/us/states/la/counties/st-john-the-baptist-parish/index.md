---
type: Jurisdiction
title: "St. John the Baptist Parish, LA"
classification: county
fips: "22095"
state: "LA"
demographics:
  population: 40743
  population_under_18: 9799
  population_18_64: 24556
  population_65_plus: 6388
  median_household_income: 66630
  poverty_rate: 14.42
  homeownership_rate: 77.46
  unemployment_rate: 10.86
  median_home_value: 193200
  gini_index: 0.4259
  vacancy_rate: 14.98
  race_white: 12614
  race_black: 23210
  race_asian: 362
  race_native: 147
  hispanic: 3646
  bachelors_plus: 6833
districts:
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/la/districts/senate/19"
    rel: in-district
    area_weight: 0.7383
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.2616
  - to: "us/states/la/districts/house/57"
    rel: in-district
    area_weight: 0.6421
  - to: "us/states/la/districts/house/58"
    rel: in-district
    area_weight: 0.3561
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. John the Baptist Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40743 |
| Under 18 | 9799 |
| 18–64 | 24556 |
| 65+ | 6388 |
| Median household income | 66630 |
| Poverty rate | 14.42 |
| Homeownership rate | 77.46 |
| Unemployment rate | 10.86 |
| Median home value | 193200 |
| Gini index | 0.4259 |
| Vacancy rate | 14.98 |
| White | 12614 |
| Black | 23210 |
| Asian | 362 |
| Native | 147 |
| Hispanic/Latino | 3646 |
| Bachelor's or higher | 6833 |

## Districts

- [LA-02](/us/states/la/districts/02.md) — 100% (congressional)
- [LA Senate District 19](/us/states/la/districts/senate/19.md) — 74% (state senate)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 26% (state senate)
- [LA House District 57](/us/states/la/districts/house/57.md) — 64% (state house)
- [LA House District 58](/us/states/la/districts/house/58.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
