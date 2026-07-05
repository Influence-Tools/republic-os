---
type: Jurisdiction
title: "Larimer County, CO"
classification: county
fips: "08069"
state: "CO"
demographics:
  population: 367368
  population_under_18: 67339
  population_18_64: 236265
  population_65_plus: 63764
  median_household_income: 93765
  poverty_rate: 11.2
  homeownership_rate: 64.02
  unemployment_rate: 4.75
  median_home_value: 569100
  gini_index: 0.4529
  vacancy_rate: 6.35
  race_white: 302769
  race_black: 3962
  race_asian: 8205
  race_native: 1914
  hispanic: 47521
  bachelors_plus: 184562
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.9316
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.0583
  - to: "us/states/co/districts/08"
    rel: in-district
    area_weight: 0.01
  - to: "us/states/co/districts/senate/15"
    rel: in-district
    area_weight: 0.9342
  - to: "us/states/co/districts/senate/23"
    rel: in-district
    area_weight: 0.0357
  - to: "us/states/co/districts/senate/14"
    rel: in-district
    area_weight: 0.0298
  - to: "us/states/co/districts/house/49"
    rel: in-district
    area_weight: 0.877
  - to: "us/states/co/districts/house/65"
    rel: in-district
    area_weight: 0.0575
  - to: "us/states/co/districts/house/51"
    rel: in-district
    area_weight: 0.0281
  - to: "us/states/co/districts/house/52"
    rel: in-district
    area_weight: 0.0167
  - to: "us/states/co/districts/house/53"
    rel: in-district
    area_weight: 0.0125
  - to: "us/states/co/districts/house/64"
    rel: in-district
    area_weight: 0.0079
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Larimer County, CO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 367368 |
| Under 18 | 67339 |
| 18–64 | 236265 |
| 65+ | 63764 |
| Median household income | 93765 |
| Poverty rate | 11.2 |
| Homeownership rate | 64.02 |
| Unemployment rate | 4.75 |
| Median home value | 569100 |
| Gini index | 0.4529 |
| Vacancy rate | 6.35 |
| White | 302769 |
| Black | 3962 |
| Asian | 8205 |
| Native | 1914 |
| Hispanic/Latino | 47521 |
| Bachelor's or higher | 184562 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 93% (congressional)
- [CO-04](/us/states/co/districts/04.md) — 6% (congressional)
- [CO-08](/us/states/co/districts/08.md) — 1% (congressional)
- [CO Senate District 15](/us/states/co/districts/senate/15.md) — 93% (state senate)
- [CO Senate District 23](/us/states/co/districts/senate/23.md) — 4% (state senate)
- [CO Senate District 14](/us/states/co/districts/senate/14.md) — 3% (state senate)
- [CO House District 49](/us/states/co/districts/house/49.md) — 88% (state house)
- [CO House District 65](/us/states/co/districts/house/65.md) — 6% (state house)
- [CO House District 51](/us/states/co/districts/house/51.md) — 3% (state house)
- [CO House District 52](/us/states/co/districts/house/52.md) — 2% (state house)
- [CO House District 53](/us/states/co/districts/house/53.md) — 1% (state house)
- [CO House District 64](/us/states/co/districts/house/64.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
