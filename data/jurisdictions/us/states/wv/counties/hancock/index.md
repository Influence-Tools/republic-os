---
type: Jurisdiction
title: "Hancock County, WV"
classification: county
fips: "54029"
state: "WV"
demographics:
  population: 28431
  population_under_18: 5221
  population_18_64: 16209
  population_65_plus: 7001
  median_household_income: 61466
  poverty_rate: 14.51
  homeownership_rate: 74.49
  unemployment_rate: 8.42
  median_home_value: 130800
  gini_index: 0.4659
  vacancy_rate: 9.65
  race_white: 26330
  race_black: 501
  race_asian: 146
  race_native: 7
  hispanic: 496
  bachelors_plus: 5422
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/wv/districts/senate/1"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/wv/districts/house/1"
    rel: in-district
    area_weight: 0.8888
  - to: "us/states/wv/districts/house/2"
    rel: in-district
    area_weight: 0.1096
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Hancock County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28431 |
| Under 18 | 5221 |
| 18–64 | 16209 |
| 65+ | 7001 |
| Median household income | 61466 |
| Poverty rate | 14.51 |
| Homeownership rate | 74.49 |
| Unemployment rate | 8.42 |
| Median home value | 130800 |
| Gini index | 0.4659 |
| Vacancy rate | 9.65 |
| White | 26330 |
| Black | 501 |
| Asian | 146 |
| Native | 7 |
| Hispanic/Latino | 496 |
| Bachelor's or higher | 5422 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 1](/us/states/wv/districts/senate/1.md) — 100% (state senate)
- [WV House District 1](/us/states/wv/districts/house/1.md) — 89% (state house)
- [WV House District 2](/us/states/wv/districts/house/2.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
