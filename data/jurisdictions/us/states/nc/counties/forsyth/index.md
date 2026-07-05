---
type: Jurisdiction
title: "Forsyth County, NC"
classification: county
fips: "37067"
state: "NC"
demographics:
  population: 389977
  population_under_18: 88343
  population_18_64: 235500
  population_65_plus: 66134
  median_household_income: 67165
  poverty_rate: 14.52
  homeownership_rate: 63.56
  unemployment_rate: 5.05
  median_home_value: 250400
  gini_index: 0.4781
  vacancy_rate: 8.94
  race_white: 217688
  race_black: 98404
  race_asian: 9311
  race_native: 1613
  hispanic: 58888
  bachelors_plus: 140974
districts:
  - to: "us/states/nc/districts/10"
    rel: in-district
    area_weight: 0.6479
  - to: "us/states/nc/districts/06"
    rel: in-district
    area_weight: 0.352
  - to: "us/states/nc/districts/senate/31"
    rel: in-district
    area_weight: 0.7154
  - to: "us/states/nc/districts/senate/32"
    rel: in-district
    area_weight: 0.2844
  - to: "us/states/nc/districts/house/74"
    rel: in-district
    area_weight: 0.3193
  - to: "us/states/nc/districts/house/75"
    rel: in-district
    area_weight: 0.2909
  - to: "us/states/nc/districts/house/91"
    rel: in-district
    area_weight: 0.1831
  - to: "us/states/nc/districts/house/71"
    rel: in-district
    area_weight: 0.111
  - to: "us/states/nc/districts/house/72"
    rel: in-district
    area_weight: 0.0956
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Forsyth County, NC

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 389977 |
| Under 18 | 88343 |
| 18–64 | 235500 |
| 65+ | 66134 |
| Median household income | 67165 |
| Poverty rate | 14.52 |
| Homeownership rate | 63.56 |
| Unemployment rate | 5.05 |
| Median home value | 250400 |
| Gini index | 0.4781 |
| Vacancy rate | 8.94 |
| White | 217688 |
| Black | 98404 |
| Asian | 9311 |
| Native | 1613 |
| Hispanic/Latino | 58888 |
| Bachelor's or higher | 140974 |

## Districts

- [NC-10](/us/states/nc/districts/10.md) — 65% (congressional)
- [NC-06](/us/states/nc/districts/06.md) — 35% (congressional)
- [NC Senate District 31](/us/states/nc/districts/senate/31.md) — 72% (state senate)
- [NC Senate District 32](/us/states/nc/districts/senate/32.md) — 28% (state senate)
- [NC House District 74](/us/states/nc/districts/house/74.md) — 32% (state house)
- [NC House District 75](/us/states/nc/districts/house/75.md) — 29% (state house)
- [NC House District 91](/us/states/nc/districts/house/91.md) — 18% (state house)
- [NC House District 71](/us/states/nc/districts/house/71.md) — 11% (state house)
- [NC House District 72](/us/states/nc/districts/house/72.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
