---
type: Jurisdiction
title: "Warren County, KY"
classification: county
fips: "21227"
state: "KY"
demographics:
  population: 140918
  population_under_18: 33379
  population_18_64: 88919
  population_65_plus: 18620
  median_household_income: 65794
  poverty_rate: 17.01
  homeownership_rate: 55.65
  unemployment_rate: 4.44
  median_home_value: 258000
  gini_index: 0.4796
  vacancy_rate: 7.06
  race_white: 106634
  race_black: 12936
  race_asian: 7201
  race_native: 726
  hispanic: 10010
  bachelors_plus: 38896
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/senate/9"
    rel: in-district
    area_weight: 0.4052
  - to: "us/states/ky/districts/senate/16"
    rel: in-district
    area_weight: 0.318
  - to: "us/states/ky/districts/senate/32"
    rel: in-district
    area_weight: 0.2767
  - to: "us/states/ky/districts/house/19"
    rel: in-district
    area_weight: 0.5946
  - to: "us/states/ky/districts/house/17"
    rel: in-district
    area_weight: 0.2891
  - to: "us/states/ky/districts/house/22"
    rel: in-district
    area_weight: 0.071
  - to: "us/states/ky/districts/house/20"
    rel: in-district
    area_weight: 0.0452
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Warren County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 140918 |
| Under 18 | 33379 |
| 18–64 | 88919 |
| 65+ | 18620 |
| Median household income | 65794 |
| Poverty rate | 17.01 |
| Homeownership rate | 55.65 |
| Unemployment rate | 4.44 |
| Median home value | 258000 |
| Gini index | 0.4796 |
| Vacancy rate | 7.06 |
| White | 106634 |
| Black | 12936 |
| Asian | 7201 |
| Native | 726 |
| Hispanic/Latino | 10010 |
| Bachelor's or higher | 38896 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 9](/us/states/ky/districts/senate/9.md) — 41% (state senate)
- [KY Senate District 16](/us/states/ky/districts/senate/16.md) — 32% (state senate)
- [KY Senate District 32](/us/states/ky/districts/senate/32.md) — 28% (state senate)
- [KY House District 19](/us/states/ky/districts/house/19.md) — 59% (state house)
- [KY House District 17](/us/states/ky/districts/house/17.md) — 29% (state house)
- [KY House District 22](/us/states/ky/districts/house/22.md) — 7% (state house)
- [KY House District 20](/us/states/ky/districts/house/20.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
