---
type: Jurisdiction
title: "Boulder County, CO"
classification: county
fips: "08013"
state: "CO"
demographics:
  population: 328961
  population_under_18: 57715
  population_18_64: 217304
  population_65_plus: 53942
  median_household_income: 103994
  poverty_rate: 11.16
  homeownership_rate: 61.97
  unemployment_rate: 4.83
  median_home_value: 756300
  gini_index: 0.4918
  vacancy_rate: 5.33
  race_white: 255881
  race_black: 2770
  race_asian: 15523
  race_native: 1121
  hispanic: 48466
  bachelors_plus: 207696
districts:
  - to: "us/states/co/districts/02"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/co/districts/senate/15"
    rel: in-district
    area_weight: 0.7811
  - to: "us/states/co/districts/senate/18"
    rel: in-district
    area_weight: 0.1111
  - to: "us/states/co/districts/senate/17"
    rel: in-district
    area_weight: 0.1076
  - to: "us/states/co/districts/house/49"
    rel: in-district
    area_weight: 0.774
  - to: "us/states/co/districts/house/12"
    rel: in-district
    area_weight: 0.1063
  - to: "us/states/co/districts/house/19"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/co/districts/house/11"
    rel: in-district
    area_weight: 0.0394
  - to: "us/states/co/districts/house/10"
    rel: in-district
    area_weight: 0.0343
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Boulder County, CO

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 328961 |
| Under 18 | 57715 |
| 18–64 | 217304 |
| 65+ | 53942 |
| Median household income | 103994 |
| Poverty rate | 11.16 |
| Homeownership rate | 61.97 |
| Unemployment rate | 4.83 |
| Median home value | 756300 |
| Gini index | 0.4918 |
| Vacancy rate | 5.33 |
| White | 255881 |
| Black | 2770 |
| Asian | 15523 |
| Native | 1121 |
| Hispanic/Latino | 48466 |
| Bachelor's or higher | 207696 |

## Districts

- [CO-02](/us/states/co/districts/02.md) — 100% (congressional)
- [CO Senate District 15](/us/states/co/districts/senate/15.md) — 78% (state senate)
- [CO Senate District 18](/us/states/co/districts/senate/18.md) — 11% (state senate)
- [CO Senate District 17](/us/states/co/districts/senate/17.md) — 11% (state senate)
- [CO House District 49](/us/states/co/districts/house/49.md) — 77% (state house)
- [CO House District 12](/us/states/co/districts/house/12.md) — 11% (state house)
- [CO House District 19](/us/states/co/districts/house/19.md) — 5% (state house)
- [CO House District 11](/us/states/co/districts/house/11.md) — 4% (state house)
- [CO House District 10](/us/states/co/districts/house/10.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
