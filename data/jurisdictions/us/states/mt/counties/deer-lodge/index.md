---
type: Jurisdiction
title: "Deer Lodge County, MT"
classification: county
fips: "30023"
state: "MT"
demographics:
  population: 9597
  population_under_18: 1155
  population_18_64: 5914
  population_65_plus: 2528
  median_household_income: 57527
  poverty_rate: 16.29
  homeownership_rate: 73.04
  unemployment_rate: 3.42
  median_home_value: 231700
  gini_index: 0.4231
  vacancy_rate: 19.26
  race_white: 8619
  race_black: 34
  race_asian: 23
  race_native: 198
  hispanic: 335
  bachelors_plus: 2500
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/senate/36"
    rel: in-district
    area_weight: 0.9489
  - to: "us/states/mt/districts/senate/38"
    rel: in-district
    area_weight: 0.0508
  - to: "us/states/mt/districts/house/71"
    rel: in-district
    area_weight: 0.9489
  - to: "us/states/mt/districts/house/76"
    rel: in-district
    area_weight: 0.0508
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Deer Lodge County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9597 |
| Under 18 | 1155 |
| 18–64 | 5914 |
| 65+ | 2528 |
| Median household income | 57527 |
| Poverty rate | 16.29 |
| Homeownership rate | 73.04 |
| Unemployment rate | 3.42 |
| Median home value | 231700 |
| Gini index | 0.4231 |
| Vacancy rate | 19.26 |
| White | 8619 |
| Black | 34 |
| Asian | 23 |
| Native | 198 |
| Hispanic/Latino | 335 |
| Bachelor's or higher | 2500 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 36](/us/states/mt/districts/senate/36.md) — 95% (state senate)
- [MT Senate District 38](/us/states/mt/districts/senate/38.md) — 5% (state senate)
- [MT House District 71](/us/states/mt/districts/house/71.md) — 95% (state house)
- [MT House District 76](/us/states/mt/districts/house/76.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
