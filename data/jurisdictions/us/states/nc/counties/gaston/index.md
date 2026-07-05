---
type: Jurisdiction
title: "Gaston County, NC"
classification: county
fips: "37071"
state: "NC"
demographics:
  population: 234881
  population_under_18: 52696
  population_18_64: 143418
  population_65_plus: 38767
  median_household_income: 67478
  poverty_rate: 13.52
  homeownership_rate: 66.85
  unemployment_rate: 4.76
  median_home_value: 266000
  gini_index: 0.4683
  vacancy_rate: 7.96
  race_white: 160677
  race_black: 41145
  race_asian: 4032
  race_native: 912
  hispanic: 23213
  bachelors_plus: 57085
districts:
  - to: "us/states/nc/districts/14"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/senate/43"
    rel: in-district
    area_weight: 0.8192
  - to: "us/states/nc/districts/senate/44"
    rel: in-district
    area_weight: 0.1802
  - to: "us/states/nc/districts/house/108"
    rel: in-district
    area_weight: 0.3948
  - to: "us/states/nc/districts/house/110"
    rel: in-district
    area_weight: 0.3612
  - to: "us/states/nc/districts/house/109"
    rel: in-district
    area_weight: 0.2433
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Gaston County, NC

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 234881 |
| Under 18 | 52696 |
| 18–64 | 143418 |
| 65+ | 38767 |
| Median household income | 67478 |
| Poverty rate | 13.52 |
| Homeownership rate | 66.85 |
| Unemployment rate | 4.76 |
| Median home value | 266000 |
| Gini index | 0.4683 |
| Vacancy rate | 7.96 |
| White | 160677 |
| Black | 41145 |
| Asian | 4032 |
| Native | 912 |
| Hispanic/Latino | 23213 |
| Bachelor's or higher | 57085 |

## Districts

- [NC-14](/us/states/nc/districts/14.md) — 100% (congressional)
- [NC Senate District 43](/us/states/nc/districts/senate/43.md) — 82% (state senate)
- [NC Senate District 44](/us/states/nc/districts/senate/44.md) — 18% (state senate)
- [NC House District 108](/us/states/nc/districts/house/108.md) — 39% (state house)
- [NC House District 110](/us/states/nc/districts/house/110.md) — 36% (state house)
- [NC House District 109](/us/states/nc/districts/house/109.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
